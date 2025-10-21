# Contenu du fichier create_structure.py
structure = {
    "data/raw/.gitkeep": "",
    "data/processed/.gitkeep": "",
    "data/datasets/README.md": "# Datasets\n\nPlace your datasets here or download using the scripts.",
    "notebooks/.gitkeep": "",
    "src/data/.gitkeep": "",
    "src/models/.gitkeep": "",
    "src/evaluation/.gitkeep": "",
    "src/deployment/.gitkeep": "",
    "src/utils/.gitkeep": "",
    "models/.gitkeep": "",
    "tests/.gitkeep": "",
    "docs/.gitkeep": "",
    "logs/.gitkeep": "",
    "requirements.txt": """# Core Data Science
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
scipy>=1.7.0

# Deep Learning
tensorflow>=2.8.0
torch>=1.9.0

# Visualization
matplotlib>=3.5.0
seaborn>=0.11.0
plotly>=5.0.0

# Network & Security
scapy>=2.4.0
pyshark>=0.4.0

# Model Explainability
shap>=0.40.0
lime>=0.2.0

# Utilities
jupyter>=1.0.0
notebook>=6.4.0
tqdm>=4.62.0
pyyaml>=6.0
joblib>=1.2.0""",
    
    "config.yaml": """# Configuration du projet Hybrid IDS

data:
  datasets:
    nsl_kdd: "data/raw/NSL-KDD/"
    cic_ids2017: "data/raw/CIC-IDS2017/"
  processed_path: "data/processed/"
  
models:
  ml:
    random_forest:
      n_estimators: 100
      max_depth: 20
    xgboost:
      n_estimators: 100
      learning_rate: 0.1
  dl:
    cnn:
      filters: [64, 128, 256]
      kernel_size: 3
      dense_units: 128
    lstm:
      units: 100
      dropout: 0.2
  
training:
  test_size: 0.2
  validation_size: 0.1
  random_state: 42
  batch_size: 32
  epochs: 50
  
evaluation:
  metrics: ["accuracy", "precision", "recall", "f1", "auc"]
  threshold: 0.5"""
}

print("Structure created!")
