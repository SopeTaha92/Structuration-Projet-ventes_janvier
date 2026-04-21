


import pandas as pd 
from loguru import logger
from typing import Dict
from config import EXCEL_FILE, EXCEL_COLOR, EXCEL_FORMATTING




def generating_excel_rapport(onglets : Dict[str, pd.DataFrame], file : str = EXCEL_FILE):
    """
    Cette fonction se charge de la génération du rapport sur un fichier Excel multi-onglets
    """
    logger.info("Lancement de la fonction de génération du rapport")
    with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
        logger.info("Création du contexte manager et création du fichier Excel")
        workbook = writer.book
        header_color = EXCEL_COLOR['bg_header']
        red_color = EXCEL_COLOR['red_color']
        orange_color = EXCEL_COLOR['orange_color']
        green_color = EXCEL_COLOR['green_color']
        base = {
        'align' : 'center',
        'valign' : 'center',
        'border' : 1
        }
        base_format = workbook.add_format(base)
        header_format = workbook.add_format(
            {
                **base,
                'bg_color' : header_color,
                'font_color' : 'white',
                'bold' : True,
                'italic' : True
            }
        )

        money_format = workbook.add_format({**base, 'num_format' : '#,##0 €'})
        marge_format = workbook.add_format({**base, 'num_format' : '0 %'})
        time_format = workbook.add_format({**base, 'num_format' : 'hh"H":mm"M":ss"S"'})
        red_format = workbook.add_format({**base, 'bg_color' : red_color})
        orange_format = workbook.add_format({**base, 'bg_color' : orange_color})
        green_format = workbook.add_format({**base, 'bg_color' : green_color})

        for name, data in onglets.items():
            logger.info(f"Création de la feuille {name}")
            data.to_excel(writer, sheet_name=name, index=False)
            worksheet = writer.sheets[name]

            for column_numb, value in enumerate(data.columns):
                worksheet.write(0, column_numb, value, header_format)
            logger.info(f"Application de la mise en forme du header pour la feuille {name}")

            worksheet.autofilter(0, 0, len(data), len(data.columns) - 1)
            logger.info(f"Application de l'auto filtre sur la feuille {name}")

            worksheet.freeze_panes(1, 0)
            logger.info(f"Fixation du header pour la feuille {name}")

            column_money = ['Revenue', 'Cost', 'Profit', 'Prix_Unitaire', 'Coût_Unitaire']
            column_marge = ['Marge', 'Marge %', 'Marge_totaux']
            if name != 'Données Brutes':
                for i, column in enumerate(data.columns):
                    column_width = max(data[column].astype(str).str.len().max() , len(column)) + 3
                    logger.info("Calcule de la largeur des cellules automatquement")
                    logger.info(f"Application des divers formatages pour la feuille {name}")
                    if column in column_marge:
                        worksheet.set_column(i, i, column_width, marge_format)
                    elif column in column_money:
                        worksheet.set_column(i, i, column_width, money_format)
                    elif column == "Heure_d'achat":
                        worksheet.set_column(i, i, column_width, time_format)
                    else:
                        worksheet.set_column(i, i, column_width, base_format)

                sheets = ['Profit', 'Marge', 'Marge %', 'Marge_totaux']
                for sheet in sheets:
                    if sheet in data.columns:
                        sheet_column = data.columns.get_loc(sheet)
                        seuil = EXCEL_FORMATTING[sheet]
                        if 'red_value' in seuil:
                            worksheet.conditional_format(1, sheet_column, len(data), sheet_column, {
                                'type' : 'cell',
                                'criteria' : '<',
                                'value' : seuil['red_value'],
                                'format' : red_format
                            })
                        if 'min_value' in seuil and 'max_value' in seuil:
                            worksheet.conditional_format(1, sheet_column, len(data), sheet_column, {
                                'type' : 'cell',
                                'criteria' : 'between',
                                'minimum' : seuil['min_value'],
                                'maximum' : seuil['max_value'],
                                'format' : orange_format
                            })
                        
                        if 'green_value' in seuil:
                            worksheet.conditional_format(1, sheet_column, len(data), sheet_column, {
                                'type' : 'cell',
                                'criteria' : '>',
                                'value' : seuil['green_value'],
                                'format' : green_format
                            })

                    
              
                if name == 'Données Par Produit':
                    chart_col = workbook.add_chart({'type' : 'column'})
                    chart_line = workbook.add_chart({'type' : 'line'})
                    produit_column = data.columns.get_loc('produit')
                    revenue_column = data.columns.get_loc('Revenue')
                    profit_column = data.columns.get_loc('Profit')
            
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
                    region_column = data.columns.get_loc('region')
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
            
    logger.success(f"Fichier de rapport Excel crée avec succée à : {file}")





