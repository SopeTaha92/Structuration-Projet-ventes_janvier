


import pandas as pd
from pathlib import Path
from datetime import datetime

def cleanning_data(file_brute):
    path = Path("data/processed")
    path.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime('%d-%m-%Y_%H-%M')
    file_path = path / f"clean_data_ventes_janvier_{today}.csv"

    file = file_brute.copy()
    file = file.dropna()
    file = file.dropduplicate(kepp='first')


    column_text = ['Produit', 'Region']
    column_int = ['Quantité', 'Prix_Unitaire', 'Coût_Unitaire']

    file[column_text] = file[column_text].apply(lambda x: x.str.strip().str.title())
    file[column_int] = file[column_int].astype(int)
    file['Date'] = pd.to_datetime(file['Date'], format='mixed', dayfirst=True, errors='coerce')
    time_delta = pd.to_timedelta(file["Heure_d'achat"], unit= 's')
    file["Heure_d'achat"] = (pd.to_datetime('2026-01-01') + time_delta).dt.time
    # Dans transform.py
    #file["Heure_d'achat"] = pd.to_timedelta(file["Heure_d'achat"], unit='s')


    #file.to_csv(file_path)

    return file

