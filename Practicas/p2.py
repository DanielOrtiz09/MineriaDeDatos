import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, tablefmt='github', showindex=False, numalign='center', stralign='left',headers="keys"))
df = pd.read_csv("VideoGamesDS.csv")

df.rename(columns={'Rank':'Posicion',
'Name':'Nombre_Juego','Platform':'Consola','Year':'Año','Genre':'Genero','Publisher':'Empresa','NA_Sales':'Ventas_NA','EU_Sales':'Ventas_EU','JP_Sales':'Ventas_Japon','Other_Sales':'Otras_Ventas','Global_Sales':'Ventas_Totales',},inplace=True)
df.to_csv("VideoGamesDS.csv")
print("\nEstadisticas utilizando la libreria pandas\n")
print("5 registros del inicio : \n",df.head())
print("5 registros del final :\n",df.tail())
print("Informacion acerca del dataframe:\n",df.info())
print("Resumen de datos\n",df.describe())