import pandas as pd
from tabulate import tabulate

def Ventas_Stats(df: pd.DataFrame)->pd.DataFrame:
    df_by_d = df.groupby(["Año"]).agg({'Ventas_Totales': ['sum', 'count', 'mean', 'min', 'max']})
    df_by_d = df_by_d.reset_index()
    return df_by_d

df = pd.read_csv("VideoGamesDS.csv")

VentasStats = Ventas_Stats(df)

VentasStats.to_csv("VentasTotalesStats.csv")