





import pandas as pd
from pathlib import Path


def extracting_data():
    path = Path("data/raw/ventes_janvier.csv")
    df = pd.read_csv(path)
    #print(df)
    return df

#extracting_data()