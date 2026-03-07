



import pandas as pd


def analysis_by_region(df):
    df_group_region = (
        df.groupby('Region')
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
    df_group_region['Marge %'] = (df_group_region['Profit'] / df_group_region['Revenue']).round(2)


    return df_group_region