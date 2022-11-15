import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv("VideoGamesDS.csv")

df_por_genero = df.groupby(["Genero"]).agg({'Ventas_NA':['mean']})
df_por_genero.reset_index(inplace=True)
df_por_genero.columns = ['Genero', 'PromedioVentas_NA']
df_por_genero.set_index("Genero", inplace=True)


moore_lm = ols('Genero ~Ventas_NA', data=df_por_genero).fit()
table = sm.stats.anova_lm(moore_lm, typ=2) 
print(table)
