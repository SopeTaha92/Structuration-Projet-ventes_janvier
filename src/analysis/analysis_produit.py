


from loguru import logger
import pandas as pd 


def analysis_by_product(df_complet : pd.DataFrame) -> pd.DataFrame:
    """
    Cette fonction se charge de faire des aggégations par produits
    """
    logger.info("Début des aggrégations par produits")

    df_group_produit = (
        df_complet.groupby('produit')
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
    df_group_produit['Marge %'] = (df_group_produit['Profit'] / df_group_produit['Revenue']).round(2)

    logger.info("Aggrégations par produits éffectué avec succées")

    return df_group_produit