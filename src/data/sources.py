"""
Data source abstraction for protein structure and function data.
"""

from abc import ABC, abstractmethod
import os
import requests
from pathlib import Path
from Bio import PDB
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProteinDataSource(ABC):
    """Abstract base class for all protein data sources."""
    
    @abstractmethod
    def get_structure(self, protein_id):
        """Retrieve structure for a protein."""
        pass
        
    @abstractmethod
    def get_function(self, protein_id):
        """Retrieve functional annotation for a protein."""
        pass

class PDBDataSource(ProteinDataSource):
    """Implementation of ProteinDataSource for the Protein Data Bank."""
    
    def __init__(self, cache_dir="../data/raw"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.pdb_url = "https://files.rcsb.org/download/{}.pdb"
        self.parser = PDB.PDBParser(QUIET=True)
        logger.info(f"PDB data source initialized with cache at {self.cache_dir}")
    
    def get_structure(self, protein_id, parser="biopython"):
        """Retrieve structure for a protein from PDB."""
        protein_id = protein_id.lower()
        pdb_file = self.cache_dir / f"{protein_id}.pdb"
        
        if not pdb_file.exists():
            url = self.pdb_url.format(protein_id)
            logger.info(f"Downloading {url}")
            response = requests.get(url)
            if response.status_code != 200:
                raise ValueError(f"Failed to download PDB: {protein_id}")
            with open(pdb_file, 'w') as f:
                f.write(response.text)
            logger.info(f"Saved PDB file to {pdb_file}")
        
        # For now, only support BioPython parser
        return self.parser.get_structure(protein_id, str(pdb_file))
    
    def get_function(self, protein_id):
        """Retrieve functional annotation for a protein from PDB."""
        structure = self.get_structure(protein_id)
        header = structure.header
        
        return {
            "id": protein_id,
            "description": header.get("name", ""),
            "resolution": header.get("resolution", None),
            "structure_method": header.get("structure_method", ""),
            "keywords": header.get("keywords", []),
            "ec_numbers": []
        }
    
    def validate_structure(self, protein_id, max_resolution=2.5, min_length=50, max_length=300):
        """Validate if a protein structure meets criteria."""
        try:
            structure = self.get_structure(protein_id)
            function_info = self.get_function(protein_id)
            
            # Check resolution
            resolution = function_info.get("resolution")
            if resolution is None or resolution > max_resolution:
                return False, {"reason": f"Resolution {resolution} > {max_resolution}"}
            
            # Count amino acids
            amino_acid_count = 0
            for model in structure:
                for chain in model:
                    for residue in chain:
                        if residue.id[0] == ' ':  # Standard amino acid
                            amino_acid_count += 1
            
            # Check length criteria
            if amino_acid_count < min_length:
                return False, {"reason": f"Too short: {amino_acid_count} < {min_length}"}
            if amino_acid_count > max_length:
                return False, {"reason": f"Too long: {amino_acid_count} > {max_length}"}
            
            validation_info = {
                "resolution": resolution,
                "amino_acid_count": amino_acid_count,
                "has_ec_number": False
            }
            
            return True, validation_info
            
        except Exception as e:
            return False, {"reason": f"Error: {str(e)}"}

def get_data_source(source_type="pdb", **kwargs):
    """Factory function to get an instance of a data source."""
    if source_type == "pdb":
        return PDBDataSource(**kwargs)
    else:
        raise ValueError(f"Unknown data source type: {source_type}")
