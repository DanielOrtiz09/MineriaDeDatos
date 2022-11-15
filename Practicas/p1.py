import pandas as pd
from tabulate import tabulate
from kaggle.api.kaggle_api_extended import KaggleApi
import os

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, tablefmt='github', showindex=False, numalign='center', stralign='left',headers="keys"))

api = KaggleApi()
api.authenticate()
api.dataset_download_file('gregorut/videogamesales', file_name='vgsales.csv')
os.rename('vgsales.csv', 'VideoGamesDS.csv')

