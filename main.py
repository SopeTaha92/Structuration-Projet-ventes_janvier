

from loguru import logger 

from src import extracting_data
from src import cleanning_data
from src import add_feature
from src import logging_file
from src import analysis_by_product, analysis_by_region, analysis_by_days
from src import generating_excel_rapport
from config import FILE_POWER_BI_DATA


try:
    logging_file()
    df = extracting_data()
    clean_data = cleanning_data(df)
    complet_data = add_feature(clean_data)
    complet_data.to_excel(FILE_POWER_BI_DATA, index=False)
    logger.success(f"Données complet pour le Dashbord power BI généré avec succée {FILE_POWER_BI_DATA.name}")
    analyse_produit = analysis_by_product(complet_data)
    analyse_region = analysis_by_region(complet_data)
    analyse_jours = analysis_by_days(complet_data)

    onglets = {
        'Données Brutes' : df,
        'Données Néttoyées' : complet_data,
        'Données Par Produit' : analyse_produit,
        'Données Par Région' : analyse_region,
        'Données Par Jour' : analyse_jours
    }
    #print(complet_data["Heure_d'achat"].dtype)
    generating_excel_rapport(onglets)
    logger.success("Pipeline exécuté entièrement avec succès.")
except Exception as e:
    logger.exception(f"Echec du Pipeline : {e}")
    raise
