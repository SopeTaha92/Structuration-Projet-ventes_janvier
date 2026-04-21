



from loguru import logger
import pandas as pd


def analysis_by_region(df_complet : pd.DataFrame) -> pd.DataFrame:
    """
    Cette fonction se charge de faire des aggégations par régions
    """
    logger.info("Début des aggrégations par régions")

    df_group_region = (
        df_complet.groupby('region')
        .agg(
            {
                'quantité' : 'sum',
                'Revenue' : 'sum',
                'Cost' : 'sum',
                'Profit'  : 'sum' 
            }
        )
        .sort_values(by=['Revenue', 'Cost', 'Profit'], ascending=False)
        .reset_index()
    )
    df_group_region['Marge %'] = (df_group_region['Profit'] / df_group_region['Revenue']).round(2)

    logger.info("Aggrégations par régions éffectué avec succées")

    return df_group_region