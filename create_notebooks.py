import os
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# Define the notebooks directory
notebooks_dir = "notebooks"

# Create the directory if it doesn't exist
os.makedirs(notebooks_dir, exist_ok=True)

# Define the content for each notebook
notebooks = {
    "01_data_collection.ipynb": {
        "title": "Protein Structure-Function ML Project: Data Collection",
        "description": "This notebook implements the data collection phase of the project, including retrieving protein structures from PDB and extracting functional annotations.",
        "cells": [
            new_markdown_cell("# Protein Structure-Function ML Project\n## 1. Data Collection\n\nThis notebook covers the acquisition of protein structure data and functional annotations from various sources."),
            new_code_cell("# Setup\nimport os\nimport sys\nimport pandas as pd\nimport numpy as np\nfrom Bio import PDB\n\n# Verify environment\nprint(f\"Python version: {sys.version}\")\nprint(f\"Working directory: {os.getcwd()}\")"),
            new_markdown_cell("## 1.1 Data Source Configuration\n\nImplement the data source abstraction layer for retrieving protein structures."),
            new_code_cell("# Implementation of data source abstraction\n# Add your code here"),
            new_markdown_cell("## 1.2 Protein Selection Criteria\n\nDefine and implement filtering criteria for protein selection:\n- Resolution < 2.5Å\n- Size: 50-300 amino acids\n- Clear EC number annotations"),
            new_code_cell("# Define selection criteria\n# Add your code here"),
            new_markdown_cell("## 1.3 Data Acquisition\n\nRetrieve protein structures and annotations."),
            new_code_cell("# Data acquisition code\n# Add your code here"),
            new_markdown_cell("## 1.4 Initial Data Analysis\n\nAnalyze the collected dataset."),
            new_code_cell("# Initial analysis\n# Add your code here")
        ]
    },
    "02_feature_extraction.ipynb": {
        "title": "Protein Structure-Function ML Project: Feature Extraction",
        "description": "This notebook implements the feature extraction phase, calculating sequence and structural features for proteins.",
        "cells": [
            new_markdown_cell("# Protein Structure-Function ML Project\n## 2. Feature Extraction\n\nThis notebook covers the extraction of sequence and structural features from protein structures."),
            new_code_cell("# Setup\nimport os\nimport sys\nimport pandas as pd\nimport numpy as np\nfrom Bio import PDB\nfrom Bio.SeqUtils.ProtParam import ProteinAnalysis\n\n# Verify environment\nprint(f\"Python version: {sys.version}\")\nprint(f\"Working directory: {os.getcwd()}\")"),
            new_markdown_cell("## 2.1 Feature Extraction Framework\n\nImplement the base feature extraction framework."),
            new_code_cell("# Feature extraction framework\n# Add your code here"),
            new_markdown_cell("## 2.2 Sequence Feature Extraction\n\nExtract sequence-based features:\n- Amino acid composition\n- Physicochemical properties"),
            new_code_cell("# Sequence feature extraction\n# Add your code here"),
            new_markdown_cell("## 2.3 Structural Feature Extraction\n\nExtract structure-based features:\n- Secondary structure content\n- Solvent accessibility\n- Contact map statistics"),
            new_code_cell("# Structural feature extraction\n# Add your code here"),
            new_markdown_cell("## 2.4 Feature Integration\n\nIntegrate sequence and structural features."),
            new_code_cell("# Feature integration\n# Add your code here")
        ]
    },
    "03_model_training.ipynb": {
        "title": "Protein Structure-Function ML Project: Model Training",
        "description": "This notebook implements the model training phase, developing and evaluating classification models.",
        "cells": [
            new_markdown_cell("# Protein Structure-Function ML Project\n## 3. Model Training\n\nThis notebook covers the development and evaluation of machine learning models for protein function prediction."),
            new_code_cell("# Setup\nimport os\nimport sys\nimport pandas as pd\nimport numpy as np\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.svm import SVC\nfrom sklearn.model_selection import train_test_split, GridSearchCV\nfrom sklearn.metrics import classification_report, confusion_matrix\n\n# Verify environment\nprint(f\"Python version: {sys.version}\")\nprint(f\"Working directory: {os.getcwd()}\")"),
            new_markdown_cell("## 3.1 Data Preparation\n\nPrepare features and labels for model training."),
            new_code_cell("# Data preparation\n# Add your code here"),
            new_markdown_cell("## 3.2 Model Implementation\n\nImplement baseline classification models."),
            new_code_cell("# Model implementation\n# Add your code here"),
            new_markdown_cell("## 3.3 Model Training\n\nTrain and evaluate models."),
            new_code_cell("# Model training\n# Add your code here"),
            new_markdown_cell("## 3.4 Hyperparameter Optimization\n\nOptimize model parameters."),
            new_code_cell("# Hyperparameter optimization\n# Add your code here")
        ]
    },
    "04_analysis.ipynb": {
        "title": "Protein Structure-Function ML Project: Analysis and Visualization",
        "description": "This notebook implements the analysis phase, visualizing results and interpreting models.",
        "cells": [
            new_markdown_cell("# Protein Structure-Function ML Project\n## 4. Analysis and Visualization\n\nThis notebook covers the analysis of results, model interpretation, and visualization of findings."),
            new_code_cell("# Setup\nimport os\nimport sys\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom sklearn.metrics import confusion_matrix\nfrom sklearn.decomposition import PCA\nfrom sklearn.manifold import TSNE\n\n# Set plotting style\nplt.style.use('seaborn-whitegrid')\nsns.set_context('notebook')\n\n# Verify environment\nprint(f\"Python version: {sys.version}\")\nprint(f\"Working directory: {os.getcwd()}\")"),
            new_markdown_cell("## 4.1 Model Evaluation\n\nComprehensive evaluation of model performance."),
            new_code_cell("# Model evaluation\n# Add your code here"),
            new_markdown_cell("## 4.2 Feature Importance Analysis\n\nAnalyze the importance of different features for classification."),
            new_code_cell("# Feature importance analysis\n# Add your code here"),
            new_markdown_cell("## 4.3 Structure-Function Visualization\n\nVisualize the relationship between structural features and functional classification."),
            new_code_cell("# Structure-function visualization\n# Add your code here"),
            new_markdown_cell("## 4.4 Case Studies\n\nExamine specific examples of structure-function relationships."),
            new_code_cell("# Case studies\n# Add your code here")
        ]
    }
}

# Create each notebook file
for filename, content in notebooks.items():
    nb = new_notebook()
    nb.cells = content["cells"]
    
    # Add metadata for kernel specification
    nb.metadata = {
        "kernelspec": {
            "display_name": "Python (Protein-ML)",
            "language": "python",
            "name": "protein-ml"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.9.0"
        },
        "title": content["title"],
        "description": content["description"]
    }
    
    # Write the notebook to file
    file_path = os.path.join(notebooks_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    
    print(f"Created notebook: {file_path}")

print("All notebooks created successfully!")