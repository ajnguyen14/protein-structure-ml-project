"""
Protein dataset selection and registry for the ML project.
"""

import pandas as pd
import json
from pathlib import Path
import logging
from src.data.sources import get_data_source

logger = logging.getLogger(__name__)

class ProteinDatasetRegistry:
    """Manages protein selection and dataset creation for the ML project."""
    
    def __init__(self, data_source=None, registry_file="../data/processed/protein_registry.json"):
        self.data_source = data_source or get_data_source("pdb")
        self.registry_file = Path(registry_file)
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        self.proteins = self.load_registry()
        
        # Selection criteria
        self.selection_criteria = {
            "max_resolution": 2.5,
            "min_length": 50,
            "max_length": 300,
            "require_ec": True
        }
    
    def load_registry(self):
        """Load existing protein registry or create empty one."""
        if self.registry_file.exists():
            with open(self.registry_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_registry(self):
        """Save the protein registry to file."""
        with open(self.registry_file, 'w') as f:
            json.dump(self.proteins, f, indent=2)
        logger.info(f"Saved {len(self.proteins)} proteins to registry")
    
    def add_protein(self, protein_id):
        """Add a protein to the registry after evaluation."""
        protein_id = protein_id.lower()
        
        if protein_id in self.proteins:
            return self.proteins[protein_id]
        
        try:
            # Validate structure
            is_valid, validation_info = self.data_source.validate_structure(
                protein_id,
                max_resolution=self.selection_criteria["max_resolution"],
                min_length=self.selection_criteria["min_length"],
                max_length=self.selection_criteria["max_length"]
            )
            
            # Get function info
            function_info = self.data_source.get_function(protein_id)
            
            evaluation = {
                "protein_id": protein_id,
                "meets_criteria": is_valid,
                "validation_info": validation_info,
                "function_info": function_info,
                "evaluation_date": pd.Timestamp.now().isoformat()
            }
            
            self.proteins[protein_id] = evaluation
            return evaluation
            
        except Exception as e:
            evaluation = {
                "protein_id": protein_id,
                "meets_criteria": False,
                "error": str(e),
                "evaluation_date": pd.Timestamp.now().isoformat()
            }
            self.proteins[protein_id] = evaluation
            return evaluation
    
    def get_valid_proteins(self):
        """Get all proteins that meet criteria."""
        return {pid: info for pid, info in self.proteins.items() 
                if info.get("meets_criteria", False)}
    
    def generate_summary_report(self):
        """Generate summary report."""
        total = len(self.proteins)
        valid = len(self.get_valid_proteins())
        
        return {
            "total_proteins_evaluated": total,
            "valid_proteins": valid,
            "invalid_proteins": total - valid,
            "proteins_by_ec_class": {},  # Simplified for now
            "selection_criteria": self.selection_criteria,
            "registry_file": str(self.registry_file)
        }

def recommend_initial_proteins():
    """Recommend good initial proteins for testing."""
    return [
        "1lyz",  # Lysozyme
        "1tim",  # Triose phosphate isomerase  
        "1crn",  # Crambin
        "1hrd",  # Horseradish peroxidase
        "1gox",  # Glucose oxidase
        "1cax",  # Carbonic anhydrase
    ]
