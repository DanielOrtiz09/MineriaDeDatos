import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt

data = pd.read_csv('VideoGamesDS.csv', index_col=0).sort_values(by='Ventas_EU', axis=0, ascending=False)
model = smf.ols(' Ventas_Totales~ Ventas_NA', data=data)
model = model.fit()

sales_pred = model.predict()

plt.figure(figsize=(12, 6))
plt.plot(data['Ventas_NA'], data['Ventas_Totales'], 'o')           
plt.plot(data['Ventas_NA'], sales_pred, 'r', linewidth=2)   
plt.xlabel('Ventas_NA ')
plt.ylabel('Ventas_Totales')
plt.title('Ventas_NA y Ventas_Totales')

plt.savefig('regresion.png')
plt.show()
plt.close()