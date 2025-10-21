# Hybride-IDS-intelligent Intrusion Dectection System

Un système de détection d'intrusions hybride combinant l'approche de
Machine Learning et Deep Learning pour la sécurité réseau.

## Objectifs

- Détection d'anomalies en temps réel
- Classification des types d'attaques
- Faible taux de faux positifs
- Explicabilité des décisions

## Architecture Hybride

###1. Module Machine Learning
- Random Forest
- XGBoost
- SVM
- Isolation Forest

###2. Module Deep Learning
- CNN pour features spatiales
- LSTM pour séquences temporelles
- Autoencodeurs pour détection d'anomalies

###3. Système de Fusion
- Votre majoritaire
- Stacking
- Méta-classificateur

## Intallation
''' bash
git clone https://github.com/Moumensalifou/hybrid-ml-dl-ids.git
cd hybrid-ml-dl-ids

# installation des dépendances
pip install -r requirements.txt

# Ou avec conda
conda env creat -f environment.yml
