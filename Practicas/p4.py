import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from scipy import stats
import squarify as sq
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("VideoGamesDS.csv")

plt.figure(figsize = (40,12))
df.groupby('Empresa')['Nombre_Juego'].agg(len).sort_values(ascending = False).plot(kind = 'bar')
plt.ylabel('Juegos totales', fontsize = 10)
plt.title('Juegos por empresas ', fontsize = 15)
plt.savefig("Juegos por empresa en el dataframe.png")
plt.close()
plt.figure(figsize = (40,12))
df.groupby('Genero')['Nombre_Juego'].agg(len).sort_values(ascending = False).plot(kind = 'bar')
plt.ylabel('Numero de juegos', fontsize = 15)
plt.title('num de juegos por genero', fontsize = 15)
plt.savefig("Juegos por Genero.png")
plt.close()
labels = df.Consola.value_counts().index
sizes = df.Consola.value_counts().values
colors = ['red','cyan']
plt.figure(figsize = (10,10))
plt.pie(sizes, labels=labels, colors=colors)
autopct=('%1.1f%%')
plt.axis('equal')
plt.savefig("Grafico de consolas.png")
plt.close()

labels = df.Empresa.value_counts().index
sizes = df.Empresa.value_counts().values
colors = ['blue','black']
plt.figure(figsize = (10,10))
plt.pie(sizes, labels=labels, colors=colors)
autopct=('%1.1f%%')
plt.axis('equal')
plt.savefig("EmpresasMasFamosas.png")
plt.close()

colors = ['red']
plt.subplots(figsize=(10,10))
plt.title('Relacion entre las ventas de japon y ventas totales')
sns.regplot(x='Ventas_Totales', y='Ventas_Japon',
            ci=None, data=df.head)
plt.savefig("Relacion entre las ventas totales y las de japon.png")
plt.close()