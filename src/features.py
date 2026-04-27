

import pandas as pd
from loguru import logger

def add_feature(df_clean : pd.DataFrame) -> pd.DataFrame:
    """
    Cette fonction se charge des noubelles colonnes et d'ajouté de la valeurs
    """
    logger.info("Début des features pour l'enrichissement du dataframe")

    df_complet = df_clean.copy()
    df_complet['jour_semaine'] = df_clean['date'].dt.day_name()#pour voir si c'est lundi ou autre 
    
    # 3. Optionnel : Traduire en français si tu préfères
    jours_fr = {
        'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi',
        'Thursday': 'Jeudi', 'Friday': 'Vendredi', 'Saturday': 'Samedi', 'Sunday': 'Dimanche'
    }
    df_complet['jour_semaine'] = df_complet['jour_semaine'].map(jours_fr)
    
    df_complet['date'] = df_clean['date'].dt.date
    df_complet['Revenue'] = (df_clean['quantité'] * df_clean['prix_unitaire']).astype(int)  
    df_complet['Cost'] = (df_clean['quantité'] * df_clean['coût_unitaire']).astype(int)
    df_complet['Profit'] = (df_complet['Revenue'] - df_complet['Cost']).astype(int)
    df_complet['Marge'] = ((df_complet['Profit'] / df_complet['Revenue'])).astype(float).round(2)
    #df  = df.sort_values(by='Revenue', ascending=False)

    logger.info("Fini avec les features")
    return df_complet 
