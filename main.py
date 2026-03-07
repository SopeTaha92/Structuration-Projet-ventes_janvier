

from src import extracting_data
from src import cleanning_data
from src import add_feature
from src import analysis_by_product, analysis_by_region, analysis_by_days
from src import generating_excel_rapport


df = extracting_data()
clean_data = cleanning_data(df)
complet_data = add_feature(clean_data)
print(complet_data)
analyse_produit = analysis_by_product(complet_data)
analyse_region = analysis_by_region(complet_data)
analyse_jours = analysis_by_days(complet_data)

onglets = {
    'Données Brutes' : df,
    'Données Néttoyées' : clean_data,
    'Données Par Produit' : analyse_produit,
    'Données Par Région' : analyse_region,
    'Données Par Jour' : analyse_jours
}
#print(complet_data["Heure_d'achat"].dtype)
generating_excel_rapport(onglets)
