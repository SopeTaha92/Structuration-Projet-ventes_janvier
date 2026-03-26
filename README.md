
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Loguru](https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![XlsxWriter](https://img.shields.io/badge/XlsxWriter-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white) 


📊 Automatisation d'Analyse des Ventes - Janvier 2026
Ce projet est une solution complète de traitement de données (Pipeline ETL) développée en Python. Il permet d'extraire des données brutes, de les nettoyer, d'ajouter des indicateurs clés (Features) et de générer un rapport Excel multi-onglets formaté professionnellement.

🛠️ Fonctionnalités
Extraction : Lecture automatisée des sources de données brutes.

Nettoyage (Cleaning) : Suppression des doublons, gestion des valeurs manquantes et normalisation des textes (Produits, Régions).

Enrichissement (Feature Engineering) : Conversion des formats de date et gestion complexe des données temporelles (Heures d'achat).

Analyses : Calculs automatiques des performances par produit, par région et par jour.

Reporting : Génération d'un fichier Excel .xlsx avec mise en forme dynamique via XlsxWriter.

🏗️ Structure du Projet
Le projet suit une architecture modulaire pour faciliter la maintenance et l'évolution (ex: futur passage à PostgreSQL).

Plaintext

.
├── main.py                 # Point d'entrée du programme
├── src/                    # Modules de traitement
│   ├── extracting_data.py
│   ├── cleanning_data.py
│   ├── add_feature.py
│   ├── analysis_by_product.py
│   └── generating_excel_rapport.py
├── data/
│   ├── raw/                # Données sources (CSV)
│   └── processed/          # Données nettoyées (Backup)
├── logs/                   # Traces d'exécution (Loguru)
├── outputs/                # Rapports Excel finaux
└── requirements.txt        # Dépendances du projet
🚀 Installation et Utilisation
1. Prérequis
Assurez-vous d'avoir Python 3.10+ installé.

2. Installation
Clonez le dépôt et installez les dépendances :

Bash

git clone https://github.com/SopeTaha92/Structuration-Projet-ventes_janvier.git
cd Structuration-Projet-ventes_janvier
pip install -r requirements.txt
3. Exécution
Lancez simplement le script principal :

Bash

python main.py
🛡️ Gestion des Logs et Erreurs
Le projet utilise Loguru pour une traçabilité complète :

Les logs sont horodatés et stockés dans le dossier /logs. 

Une politique de rétention de 10 jours est appliquée pour optimiser l'espace disque.

Le système gère les erreurs critiques (fichiers manquants, erreurs de format) sans interrompre brutalement le système.

📝 À propos
Ce projet a été réalisé dans le cadre d'une spécialisation en Data Analysis et Python Development. Il démontre une capacité à structurer un projet de manière industrielle, prêt pour un déploiement ou une intégration avec des bases de données SQL (PostgreSQL).
