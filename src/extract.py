





import sys
import time

import pandas as pd
import psycopg2
from loguru import logger
from config import DB_CONFIG, TABLE_NAME, MAX_RETRIES, DELAY, BRUTE_DATA_FILE


def extracting_data(max_retries : int = MAX_RETRIES, delay : int = DELAY, file : str = BRUTE_DATA_FILE) -> pd.DataFrame:
    """
    Cette fonction se charge d'extraire les données brutes depuis la base de donnée
    """
    logger.info("Début de l'extraction des données depuis la data base")
    for retry in range(max_retries):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            logger.info('testing connection !')
            df_brute = pd.read_sql(f"SELECT * FROM {TABLE_NAME};", conn)
            logger.success("✅ Connexion à la base de donnée éffectué avec succée")
            conn.close()
            logger.info("✅ Extraction des données depuis la base reussi")
            df_brute.to_csv(file)
            return df_brute
        except Exception as e:
            if retry < max_retries - 1 :
                logger.error(f"Echec de la tentative d'extraction {retry+1} / {max_retries}")
                logger.info(f"Nouvelle tentative dans {delay} secondes")
                time.sleep(delay)
                delay *= 2
            else:
                logger.critical(f"Echec total après {max_retries} tentatives : {e}")

    sys.exit(f"Arret du programme après {max_retries} tentatives")









