import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode

videogames = pd.read_csv("VideoGamesDS.csv")

def ClassificationFunc(position):   
    radioA = 3
    radioB = 5

    distancia = np.sqrt( videogames['Ventas_EU'][position]**2 + videogames['Ventas_NA'][position]**2 )
    
    if distancia <= radioA:
        return "Grupo A"
    elif distancia <= radioB and distancia > radioA:
        return "Grupo B"
    elif  distancia > radioB:
        return "Grupo C"
    
    return "GrupoC"

plt.scatter(videogames['Ventas_EU'], videogames['Ventas_NA'])
plt.title("Relacion entre las ventas de europa y las de america del norte")
plt.xlabel("Ventas de europa")
plt.ylabel("Ventas de america del norte")
plt.savefig("Relacion naeu.png")
plt.close()

videogames=videogames.reset_index()
videogames['group'] = videogames['index'].transform(ClassificationFunc)

def scatterClassification(file_path, df, x_column, y_column, label_column):
    colors = ["blue", "gray", "red"]
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=colors[i])
    
    ax.set_title("Relacion entre las ventas de europa y las de america del norte")
    ax.set_xlabel("Ventas de europa")
    ax.set_ylabel("Ventas de america del norte") 
    ax.legend()
    plt.savefig(file_path)
    plt.close()

def euclidean_distance(p_1, p_2) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neightbors(points, labels, input_data, k):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]

scatterClassification("RelacionVentas de europa y norte america", videogames, "Ventas_EU", "Ventas_NA", "group")

df = pd.DataFrame()
df['x'] = videogames['Ventas_EU']
df['y'] = videogames['Ventas_NA']
df['label'] = videogames['group']

list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]

points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_nearest_neightbors(
    points,
    labels,
    [np.array([5, 100]), np.array([8, 200]), np.array([10, 300]), np.array([12, 400])],
    5,
)
print(kn)