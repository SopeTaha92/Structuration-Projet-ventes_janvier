


from dotenv import dotenv_values
from pathlib import Path
from datetime import datetime


TODAY = datetime.now().strftime('%d-%m-%Y_%H-%M')
MAX_RETRIES = 3
DELAY = 1


LOG_DIR = Path("log")
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / f"logging_file_{TODAY}.log"




env = dotenv_values(".env")

DB_CONFIG = {
    'host' : env['DB_HOST'],
    'port' : int(env['DB_PORT']),
    'dbname' : env['DB_NAME'],
    'user' : env['DB_USER'],
    'password' : env['DB_PASSWORD']
}

TABLE_NAME = env['DB_TABLE']
DATE_DEBUT = '2026-01-01'
DATE_FIN = '2026-01-31'



BRUTE_DATA = Path("data/raw")
BRUTE_DATA.mkdir(parents=True, exist_ok=True)
BRUTE_DATA_FILE = BRUTE_DATA / f"brute_data_ventes_janvier.csv"


CLEAN_DATA = Path("data/processed")
CLEAN_DATA.mkdir(parents=True, exist_ok=True)
CLEAN_DATA_FILE = CLEAN_DATA / f"clean_data_ventes_janvier_{TODAY}.csv"


EXCEL_DIR_PATH = Path('rapport_excel')
EXCEL_DIR_PATH.mkdir(parents=True, exist_ok=True)
EXCEL_FILE = EXCEL_DIR_PATH / f"rapport_excel_ventes_janvier_{TODAY}.xlsx"


CSV_TEST = "tests/out_put.csv"


EXCEL_COLOR = {
    'bg_header' : '#4F81BD',
    'red_color' : '#FFC7CE',
    'orange_color' : '#FFEB9C',
    'green_color' : '#13FF3A'
}

EXCEL_FORMATTING = {
    'Profit' : {
        'min_value' : 0,
        'max_value' : 500,
        'red_value' : 0
    },

    'Marge' : {
        'green_value' : 0.25
    },

    'Marge %' : {
        'green_value' : 0.25
    },

    'Marge_totaux' : {
        'green_value' : 0.25
    },
}


DIR_POWER_BI_DATA = Path('power_bi/data')
DIR_POWER_BI_DATA.mkdir(parents=True, exist_ok=True)
FILE_POWER_BI_DATA = DIR_POWER_BI_DATA / f"données_complet_vente_janvier.xlsx"