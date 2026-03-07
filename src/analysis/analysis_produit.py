


import pandas as pd 


def analysis_by_product(df):
    df_group_produit = (
        df.groupby('Produit')
        .agg(
            {
                'Quantité' : 'sum',
                'Revenue' : 'sum',
                'Cost' : 'sum',
                'Profit'  : 'sum'
            }
        )
        .sort_values(by=['Revenue', 'Cost', 'Profit'], ascending=False)
        .reset_index()
    )
    df_group_produit['Marge %'] = (df_group_produit['Profit'] / df_group_produit['Revenue']).round(2)


    return df_group_produit