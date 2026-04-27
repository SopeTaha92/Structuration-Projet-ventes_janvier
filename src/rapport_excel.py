


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
                    elif column == "heure_achat":
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
                            'values' : [name, 1, revenue_column, len(data), revenue_column],
                            'fill':   {'color': '#B6D7A8'}, # Un vert très clair (presque pastel)
                            'border': {'color': '#6aa84f', 'width': 1.5}, # Un contour vert plus foncé pour la propreté
                            'data_labels': {
                                'value': True, 
                                'position': 'outside_end', 
                                'num_format': '#,##0 €',
                                'font': {'bold': True} # Le gras aide énormément la lisibilité
                                            }
                        }
                    )

                    chart_line.add_series(
                        {
                            'name' : 'Profit Par Produit',
                            'categories' : [name, 1, produit_column, len(data), produit_column],
                            'values' : [name, 1, profit_column, len(data), profit_column],
                            'y2_axis' : True,
                            'line': {'color': 'red', 'width': 2}, # Force la ligne en rouge pour qu'on la voie
                            'marker': {'type': 'circle', 'size': 5, 'fill': {'color': 'white'}, 'border': {'color': 'red'}}, # Ajoute des points sur la ligne
                            'data_labels': {'value': True, 'position': 'above', 'font': {'bold': True}, 'num_format' : '#,##0 €'}
                         }
                    )
                    # Masquer les chiffres sur l'axe Y principal (Revenue)
                    chart_col.set_y_axis({'visible': False, 'major_gridlines': {'visible': False}})
                    chart_line.set_y2_axis({'visible': False, 'major_gridlines': {'visible': False}})
                    chart_col.combine(chart_line)
                    chart_col.set_legend({'position' : 'none'})
                    chart_col.set_title({'name' : 'Répartition Revenue/Profit'}) 
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_col)

                if name == 'Données Par Région':
                    chart_pie = workbook.add_chart({'type' : 'pie'})
                    chart_line = workbook.add_chart({'type' : 'line'})
                    region_column = data.columns.get_loc('region')
                    marge_percent_column = data.columns.get_loc('Marge %')
                    profit_column = data.columns.get_loc('Profit')
            
                    chart_pie.add_series(
                        {
                            'name' : 'Revenue Par Produit',
                            'categories' : [name, 1, region_column, len(data), region_column],
                            'values' : [name, 1, profit_column, len(data), profit_column],
                            'data_labels' : {'percentage' : True,'category' : True,'position' : 'outside_end'}
                        }
                    )

                    chart_pie.set_legend({'position' : 'none'})
                    chart_pie.set_title({'name' : 'Répartition du Profit par Région'})
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_pie)

                if name == 'Données Par Jour':
                    chart_col = workbook.add_chart({'type' : 'column'})
                    chart_line = workbook.add_chart({'type' : 'line'})
                    day_column = data.columns.get_loc('jour_semaine')
                    profit_column = data.columns.get_loc('Profit')
                    quantité_column = data.columns.get_loc('quantité')


                    chart_col.add_series(
                        {
                            'name' : 'Jour de la semaine',
                            'categories' : [name, 1, day_column, len(data), day_column],
                            'values' : [name, 1, profit_column, len(data), profit_column],
                            'fill':   {'color': '#B6D7A8'}, # Un vert très clair (presque pastel)
                            'border': {'color': '#6aa84f', 'width': 1.5}, # Un contour vert plus foncé pour la propreté
                            'data_labels': {
                                'value': True, 
                                'position': 'outside_end', 
                                'num_format': '#,##0 €',
                                'font': {'bold': True} # Le gras aide énormément la lisibilité
                                            }
                        }
                    )

                    chart_line.add_series(
                        {
                            'name' : 'Quantité vendu par Jour',
                            'categories' : [name, 1, day_column, len(data), day_column],
                            'values' : [name, 1, quantité_column, len(data), quantité_column],
                            'y2_axis' : True,
                            'line': {'color': 'red', 'width': 2}, # Force la ligne en rouge pour qu'on la voie
                            'marker': {'type': 'circle', 'size': 8, 'fill': {'color': 'white'}, 'border': {'color': 'red'}}, # Ajoute des points sur la ligne
                            'data_labels': {'value': True, 'position': 'above', 'font': {'bold': True}} # Affiche la quantité au-dessus du point
                        }
                    )
        

                    chart_col.set_y_axis({
                                            'visible': True,
                                            'major_tick_mark': 'none',
                                            'minor_tick_mark': 'none',
                                            'num_font': {'color': '#FFFFFF'},
                                            'line': {'none': True},
                                            'major_gridlines': {'visible': False},
                                            'max': data['Profit'].max() * 1.5  # ← % de marge
                                        })
                    chart_line.set_y2_axis({
                                            'visible': True,
                                            'major_tick_mark': 'none',
                                            'minor_tick_mark': 'none',
                                            'num_font': {'color': '#FFFFFF'},
                                            'line': {'none': True},
                                            'major_gridlines': {'visible': False}
                                        }) # On enlève aussi les lignes de grille pour le style)
                    chart_col.combine(chart_line)
                    chart_col.set_legend({'position' : 'none'})
                    chart_col.set_title({'name' : 'Répartition Profit/Quantité par Jour'})
                    """chart_col.set_plotarea({
                                                'border': {'none': True}
                                            })"""
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_col)

            
    logger.success(f"Fichier de rapport Excel crée avec succée à : {file}")


"""
“La visualisation met en évidence la relation entre profit et volume de ventes selon les jours, permettant d’identifier les jours à forte performance commerciale.”
que penses tu de mettre ça dans le readme
"""


