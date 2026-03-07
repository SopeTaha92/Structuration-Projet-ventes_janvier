

import pandas as pd



def add_feature(df):
    df['jour_semaine'] = df['Date'].dt.day_name()#pour voir si c'est lundi ou autre 
    
    # 3. Optionnel : Traduire en français si tu préfères
    jours_fr = {
        'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi',
        'Thursday': 'Jeudi', 'Friday': 'Vendredi', 'Saturday': 'Samedi', 'Sunday': 'Dimanche'
    }
    df['jour_semaine'] = df['jour_semaine'].map(jours_fr)
    
    df['Date'] = df['Date'].dt.date
    df['Revenue'] = (df['Quantité'] * df['Prix_Unitaire']).astype(int)  
    df['Cost'] = (df['Quantité'] * df['Coût_Unitaire']).astype(int)
    df['Profit'] = (df['Revenue'] - df['Cost']).astype(int)
    df['Marge'] = ((df['Profit'] / df['Revenue'])).astype(float).round(2)
    df  = df.sort_values(by='Revenue', ascending=False)


    return df 
