


import pandas as pd
from loguru import logger

def analysis_by_days(df_complet : pd.DataFrame) -> pd.DataFrame:
    """
    Cette fonction se charge de faire des aggrégations par jours
    """
    logger.info("Début des aggrégations par jous")

    df_group_days = (
        df_complet.groupby('jour_semaine')
        .agg(
            {
                'produit' : 'count',
                'quantité' : 'sum',
                'Revenue' : 'sum',
                'Cost' : 'sum',
                'Profit' : 'sum'
            }
        )
    )
    df_group_days['Marge_totaux'] = (df_group_days['Profit'] / df_group_days['Revenue'])
    ordre_jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    df_group_days = df_group_days.reindex(ordre_jours)

    logger.info("Aggrégations par jours éffectué avec succées")

    return df_group_days.reset_index()