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
    "requirements.txt": """# Core Data Science\nnumpy>=1.21.0\npandas>=1.3.0\nscikit-learn>=1.0.0\nscipy>=1.7.0\n\n# Deep Learning\ntensorflow>=2.8.0\ntorch>=1.9.0\n\n# Visualization\nmatplotlib>=3.5.0\nseaborn>=0.11.0\nplotly>=5.0.0\n\n# Network & Security\nscapy>=2.4.0\npyshark>=0.4.0\n\n# Model Explainability\nshap>=0.40.0\nlime>=0.2.0\n\n# Utilities\njupyter>=1.0.0\nnotebook>=6.4.0\ntqdm>=4.62.0\npyyaml>=6.0\njoblib>=1.2.0""",
    
    "config.yaml": """# Configuration du projet Hybrid IDS\n\ndata:\n  datasets:\n    nsl_kdd: \"data/raw/NSL-KDD/\"\n    cic_ids2017: \"data/raw/CIC-IDS2017/\"\n  processed_path: \"data/processed/\"\n  \nmodels:\n  ml:\n    random_forest:\n      n_estimators: 100\n      max_depth: 20\n    xgboost:\n      n_estimators: 100\n      learning_rate: 0.1\n  dl:\n    cnn:\n      filters: [64, 128, 256]\n      kernel_size: 3\n      dense_units: 128\n    lstm:\n      units: 100\n      dropout: 0.2\n  \ntraining:\n  test_size: 0.2\n  validation_size: 0.1\n  random_state: 42\n  batch_size: 32\n  epochs: 50\n  \nevaluation:\n  metrics: [\"accuracy\", \"precision\", \"recall\", \"f1\", \"auc\"]\n  threshold: 0.5"""}

print("Structure created!")
