


import pandas as pd 
from pathlib import Path
from datetime import datetime

dir_path = Path('rapport_excel')
dir_path.mkdir(parents=True, exist_ok=True)
today = datetime.now().strftime('%d-%m-%Y_%H-%M')
file = dir_path / f"rapport_excel_ventes_janvier_{today}.xlsx"



def generating_excel_rapport(onglets):
    with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
        workbook = writer.book
        base = {
        'align' : 'center',
        'valign' : 'center',
        'border' : 1
        }
        base_format = workbook.add_format(base)
        header_format = workbook.add_format(
            {
                **base,
                'bg_color' : '#4F81BD',
                'font_color' : 'white',
                'bold' : True,
                'italic' : True
            }
        )
        money_format = workbook.add_format({**base, 'num_format' : '#,##0 €'})
        marge_format = workbook.add_format({**base, 'num_format' : '0 %'})
        time_format = workbook.add_format({**base, 'num_format' : 'hh"H":mm"M":ss"S"'})
        red_format = workbook.add_format({**base, 'bg_color' : '#FFC7CE'})
        orange_format = workbook.add_format({**base, 'bg_color' : '#FFEB9C'})
        green_format = workbook.add_format({**base, 'bg_color' : '#13FF3A'})
        for name, data in onglets.items():
            data.to_excel(writer, sheet_name=name, index=False)
            worksheet = writer.sheets[name]
            for column_numb, value in enumerate(data.columns):
                worksheet.write(0, column_numb, value, header_format)
            worksheet.autofilter(0, 0, len(data), len(data.columns) - 1)
            worksheet.freeze_panes(1, 0)
            column_money = ['Revenue', 'Cost', 'Profit', 'Prix_Unitaire', 'Coût_Unitaire']
            column_marge = ['Marge', 'Marge %', 'Marge_totaux']
            for i, column in enumerate(data.columns):
                column_width = max(data[column].astype(str).str.len().max() , len(column)) + 3
                if column in column_marge:
                    worksheet.set_column(i, i, column_width, marge_format)
                elif column in column_money:
                    worksheet.set_column(i, i, column_width, money_format)
                #elif column == "Heure_d'achat":
                    #worksheet.set_column(i, i, column_width, time_format)
                else:
                    worksheet.set_column(i, i, column_width, base_format)


                if 'Profit' in data.columns:
                    profit_column = data.columns.get_loc('Profit')
                    worksheet.conditional_format(1, profit_column, len(data), profit_column, {
                        'type' : 'cell',
                        'criteria' : '<',
                        'value' : 0,
                        'format' : red_format
                    })

                    worksheet.conditional_format(1, profit_column, len(data), profit_column, {
                        'type' : 'cell',
                        'criteria' : 'between',
                        'minimum' : 0,
                        'maximum' : 500,
                        'format' : orange_format
                    })

                if 'Marge' in data.columns:
                    marge_column = data.columns.get_loc('Marge')
                    worksheet.conditional_format(1, marge_column, len(data), marge_column, {
                    'type' : 'cell',
                    'criteria' : '>',
                    'value' : 0.25,
                    'format' : green_format
                    })
                
                if 'Marge %' in data.columns:
                    marge_percent_column = data.columns.get_loc('Marge %')
                    worksheet.conditional_format(1, marge_percent_column, len(data), marge_percent_column, {
                        'type' : 'cell',
                        'criteria' : '>',
                        'value' : 0.25,
                        'format' : green_format
                    })
                if 'Marge_totaux' in data.columns:
                    marge_totaux_column = data.columns.get_loc('Marge_totaux')
                    worksheet.conditional_format(1, marge_totaux_column, len(data), marge_totaux_column, {
                        'type' : 'cell',
                        'criteria' : '>',
                        'value' : 0.25,
                        'format' : green_format
                    })
                if name == 'Données Néttoyées':
                    if column == "Heure_d'achat":
                        worksheet.set_column(i, i, column_width, time_format)
              
                if name == 'Données Par Produit':
                    chart_col = workbook.add_chart({'type' : 'column'})
                    chart_line = workbook.add_chart({'type' : 'line'})
                    produit_column = data.columns.get_loc('Produit')
                    revenue_column = data.columns.get_loc('Revenue')
            
                    chart_col.add_series(
                        {
                            'name' : 'Revenue Par Produit',
                            'categories' : [name, 1, produit_column, len(data), produit_column],
                            'values' : [name, 1, revenue_column, len(data), revenue_column]
                        }
                    )

                    chart_line.add_series(
                        {
                            'name' : 'Profit Par Produit',
                            'categories' : [name, 1, produit_column, len(data), produit_column],
                            'values' : [name, 1, profit_column, len(data), profit_column]
                        }
                    )
                    chart_col.combine(chart_line)
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_col)

                if name == 'Données Par Région':
                    chart_col = workbook.add_chart({'type' : 'column'})
                    chart_line = workbook.add_chart({'type' : 'line'})
                    region_column = data.columns.get_loc('Region')
                    marge_percent_column = data.columns.get_loc('Marge %')
                    profit_column = data.columns.get_loc('Profit')
            
                    chart_col.add_series(
                        {
                            'name' : 'Revenue Par Produit',
                            'categories' : [name, 1, region_column, len(data), region_column],
                            'values' : [name, 1, profit_column, len(data), profit_column]
                        }
                    )

                    chart_line.add_series(
                        {
                            'name' : 'Profit Par Produit',
                            'categories' : [name, 1, region_column, len(data), region_column],
                            'values' : [name, 1, marge_percent_column, len(data), marge_percent_column],
                            'y2_axis' : True
                        }
                    )
                    chart_col.combine(chart_line)
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_col)







    print(f"Fichier crée avec succée à : {file}")