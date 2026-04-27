


import pandas as pd
import pytest 
from src.features import add_feature

def test_add_feature():
    data = {
        'date' : pd.to_datetime(['2026-01-07'], format='mixed', dayfirst=True, errors='coerce'),
        'quantité' : [11], 
        'prix_unitaire' : [894], 
        'coût_unitaire' : [1061]
    }
    fake_df = pd.DataFrame(data)
    result = add_feature(fake_df)

    date = data['date'][0]
    jours_fr = {
        'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi',
        'Thursday': 'Jeudi', 'Friday': 'Vendredi', 'Saturday': 'Samedi', 'Sunday': 'Dimanche'
    }
    
    jour_attendu = jours_fr[date.day_name()] # Traduit "Wednesday" en "Mercredi"
    revenue = (11*894)
    cost = (11*1061)
    profit = revenue-cost
    marge = profit / revenue

    assert result['jour_semaine'][0] == jour_attendu
    assert result['Revenue'][0] == revenue
    assert result['Cost'][0] == cost
    assert result['Profit'][0] == profit
    assert result['Marge'][0] == round(marge, 2)


    