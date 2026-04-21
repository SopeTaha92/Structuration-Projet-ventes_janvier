


import pandas as pd
from src.clean_data import cleanning_data
from config import CSV_TEST


def test_cleanning_data():
    data = {
        'date' : ['2026-01-07'],
        'produit' : [' Souris '], 
        'region' : [' paris '],
        'quantité' : ['11'], 
        'prix_unitaire' : ['894'], 
        'coût_unitaire' : ['1061'],
        'heure_achat' : ['27376']
    }
    fake_df = pd.DataFrame(data)
    result = cleanning_data(fake_df, CSV_TEST)

    assert result['date'][0] == pd.to_datetime('2026-01-07', format='mixed', dayfirst=True, errors='coerce')
    assert result['produit'][0] == 'Souris'
    assert result['region'][0] == 'Paris'
    assert result['quantité'][0] == 11
    assert result['prix_unitaire'][0] == 894
    assert result['coût_unitaire'][0] == 1061
    expected = (pd.to_datetime('2026-01-01') + pd.Timedelta(seconds=27376)).time()
    assert result['heure_achat'][0] == expected