# Protein Structure-Function ML Project

## Project Overview

This project develops a machine learning framework to predict protein function from structural features. Using a modular architecture, it focuses on extracting informative features from protein structures and building ML models to classify proteins into enzyme functional categories (EC classes).

## Table of Contents

- [Installation](#installation)
- [Repository Structure](#repository-structure)
- [Environment Setup](#environment-setup)
- [Code Architecture](#code-architecture)
- [Project Workflow](#project-workflow)
- [Usage](#usage)
- [Expansion Framework](#expansion-framework)
- [Documentation](#documentation)

## Installation

### Prerequisites

- Python 3.9 or higher
- Conda package manager

### Clone the Repository

```bash
git clone https://github.com/yourusername/protein-structure-function-ml-project.git
cd protein-structure-function-ml-project
```

### Environment Setup

```bash
# Create and activate the conda environment
conda env create -f environment.yml
conda activate protein-ml

# For developers: Set up pre-commit hooks (optional)
pre-commit install
```

## Repository Structure

```
protein-ml-project/
├── README.md                     # Project overview
├── CONTRIBUTING.md               # Contribution guidelines
├── .gitignore                    # Git ignore patterns
├── environment.yml               # Conda environment specification
├── data/
│   ├── raw/                      # Raw PDB files
│   ├── raw_alphafold/            # AlphaFold structures (expansion)
│   ├── processed/                # Processed features
│   └── processed_advanced/       # Advanced features (expansion)
├── notebooks/                    # Jupyter notebooks
│   ├── 01_data_collection.ipynb  # Data acquisition workflow
│   ├── 02_feature_extraction.ipynb  # Feature engineering
│   ├── 03_model_training.ipynb   # ML model training
│   └── 04_analysis.ipynb         # Results analysis
├── src/                          # Source code
│   ├── data/                     # Data handling
│   ├── features/                 # Feature extraction
│   ├── models/                   # ML models
│   └── visualization/            # Visualization utilities
├── models/                       # Saved ML models
├── reports/                      # Results and visualizations
├── tests/                        # Unit tests
└── docs/                         # Project documentation
```

## Environment Setup

The project environment includes the following key dependencies:

- **Data Processing**: NumPy, Pandas, BioPython
- **Machine Learning**: scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **Development**: pytest, Sphinx, Black

For the complete environment specification, see the `environment.yml` file.

## Code Architecture

The project follows a modular architecture with clearly defined interfaces for extensibility:

### Data Module (`src/data/`)

- `sources.py`: Abstract classes for protein data sources (PDB, AlphaFold)
- `loaders.py`: Functions for loading and processing datasets

### Features Module (`src/features/`)

- `base.py`: Abstract feature extractor interface
- `sequence.py`: Sequence-based feature extractors (amino acid composition, physicochemical properties)
- `structure.py`: Structure-based feature extractors (secondary structure, solvent accessibility, contacts)

### Models Module (`src/models/`)

- `base.py`: Abstract model interface
- `classifiers.py`: Implementation of ML models (Random Forest, SVM)

### Visualization Module (`src/visualization/`)

- `plots.py`: Visualization functions for features, models, and structure-function relationships

## Project Workflow

The project follows a structured workflow divided into four phases:

1. **Data Collection**: Query and download protein structures from PDB, filtering for high-quality enzymes
2. **Feature Extraction**: Process structures to extract sequence and structural features
3. **Model Training**: Train and optimize ML models to predict enzyme classes
4. **Analysis**: Evaluate model performance and analyze structure-function relationships

Each phase is implemented in a corresponding Jupyter notebook.

## Usage

### Data Collection

```python
from src.data.sources import PDBDataSource

# Initialize data source
pdb_source = PDBDataSource()

# Download a structure
structure_path = pdb_source.get_structure("1abc")
```

### Feature Extraction

```python
from src.features.sequence import SequenceFeatureExtractor
from src.features.structure import StructureFeatureExtractor

# Extract sequence features
seq_extractor = SequenceFeatureExtractor()
seq_features = seq_extractor.extract("1abc", structure_path)

# Extract structural features
struct_extractor = StructureFeatureExtractor()
struct_features = struct_extractor.extract("1abc", structure_path)
```

### Model Training

```python
from src.models.classifiers import RandomForestModel

# Initialize and train model
model = RandomForestModel()
model.train(X_train, y_train)

# Evaluate model
metrics = model.evaluate(X_test, y_test)
```

### Visualization

```python
from src.visualization.plots import plot_feature_importance, plot_confusion_matrix

# Visualize feature importance
plot_feature_importance(model.feature_importance())

# Visualize model performance
plot_confusion_matrix(y_true, y_pred, class_names=ec_classes)
```

## Expansion Framework

This project is designed with clear extension points for future development:

- **Additional Data Sources**: Framework for integrating AlphaFold predictions and other structure sources
- **Advanced Features**: Placeholders for more complex structural representations
- **Hierarchical Classification**: Support for fine-grained EC classification beyond top-level classes
- **Advanced Models**: Framework for implementing neural networks and graph-based models

## Documentation

For more details, see the following documents:

- [Project Outline](docs/enhanced-project-outline.md): Detailed project structure and goals
- [Logistics Outline](docs/enhanced-logistics-outline.md): Infrastructure and setup details
- [Workflow Outline](docs/updated_workflow.md): Step-by-step tasks and objectives

## License

MIT License - See LICENSE file for details

## Acknowledgments

This project structure is based on the enhanced project outline developed for protein structure-function analysis, with a focus on modular design and future extensibility.