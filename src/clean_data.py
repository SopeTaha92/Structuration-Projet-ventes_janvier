


import pandas as pd
from loguru import logger 
from config import CLEAN_DATA_FILE

def cleanning_data(df_brute : pd.DataFrame, file : str = CLEAN_DATA_FILE) -> pd.DataFrame:
    """
    Cette fonction se charge du néttoye des données brutes
    """
    logger.info("Début du néttoyage des données brutes reçus")
    df_clean = df_brute.copy()
    logger.info('Copie des données brutes reçu effectué')
    df_clean = df_clean.dropna()
    df_clean = df_clean.drop_duplicates(keep='first')


    column_text = ['produit', 'region']
    column_int = ['quantité', 'prix_unitaire', 'coût_unitaire']

    df_clean[column_text] = df_clean[column_text].apply(lambda x: x.str.strip().str.title())

    df_clean[column_int] = df_clean[column_int].astype(int)

    df_clean['date'] = pd.to_datetime(df_clean['date'], format='mixed', dayfirst=True, errors='coerce')
    time_delta = pd.to_timedelta(pd.to_numeric(df_clean["heure_achat"], errors='coerce'), unit= 's')
    df_clean["heure_achat"] = (pd.to_datetime('2026-01-01') + time_delta).dt.time
    # Dans transform.py
    #file["Heure_d'achat"] = pd.to_timedelta(file["Heure_d'achat"], unit='s')


    df_clean.to_csv(file)
    logger.info(f"Création du fichier csv des données propres avec succée : {file.name}")

    return df_clean

