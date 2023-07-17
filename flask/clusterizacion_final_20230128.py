import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Carga de datos desde API
fecha_ini = '1990-01-01'
fecha_fin = '1990-01-31'
df = pd.read_json(f'http://200.89.81.42:8100/api/HistoricosProcesados/{fecha_ini}/{fecha_fin}')

df["fecha"]= pd.to_datetime(df["fecha"]) # convertir fecha a tipo fecha
df.set_index("fecha", inplace = True) # establecer fecha como indice

le_estacion = LabelEncoder()
le_indice = LabelEncoder()

df['estacion_encoded'] = le_estacion.fit_transform(df['estacion'])
df['confort_encoded'] = le_indice.fit_transform(df['confort'])

# Selección de variables para clustering
X = df[['estacion_encoded', 'confort_encoded']]

# Inicializar lista vacía para guardar las inercias
inercias = []

# Probar diferentes valores de k
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inercias.append(kmeans.inertia_)

# determinar el numero optimo de clusters utilizando la tecnica del codo
n_clusters = range(1, 11)
slope = [i - inercias[i - 1] for i in range(1, len(inercias))]
opt_n_clusters = slope.index(max(slope)) + 1

#print(f'El número óptimo de clusters es: {opt_n_clusters}')
print(opt_n_clusters)

# Aplicación de k-means con número óptimo de clusters
kmeans = KMeans(n_clusters=opt_n_clusters)
kmeans.fit(X)
df['cluster'] = kmeans.predict(X)

# Recuperar los valores originales en el eje X y eje Y
estaciones_originales = le_estacion.inverse_transform(df['estacion_encoded'])
indices_originales = le_indice.inverse_transform(df['confort_encoded'])

df["estacion"] = estaciones_originales
df["confort"] = indices_originales

# Visualización de resultados
plt.figure(figsize=(10,8))
sns.heatmap(df.pivot_table(values='cluster',index='estacion',columns='confort'), cmap='Reds')
plt.title(f'Clusters por Estaciones e Indice de Confort Térmico {fecha_ini} a {fecha_fin}')
plt.xlabel('Indice de Confort Térmico')
plt.ylabel('Estacion')
plt.show()