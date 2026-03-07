


import pandas as pd

def analysis_by_days(file):
    df_group_days = (
        file.groupby('jour_semaine')
        .agg(
            {
                'Produit' : 'count',
                'Quantité' : 'sum',
                'Revenue' : 'sum',
                'Cost' : 'sum',
                'Profit' : 'sum'
            }
        )
    )
    df_group_days['Marge_totaux'] = (df_group_days['Profit'] / df_group_days['Revenue'])
    ordre_jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    df_group_days = df_group_days.reindex(ordre_jours)

    return df_group_days.reset_index()