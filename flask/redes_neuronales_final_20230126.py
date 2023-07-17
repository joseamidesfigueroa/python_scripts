import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

# Carga de datos desde API
fecha_ini = '1990-01-01'
fecha_fin = '1990-01-31'
estacion = 'Los Naranjos'
df = pd.read_json(f'http://200.89.81.42:8100/api/HistoricosProcesados/{estacion.replace(" ","%20")}/{fecha_ini}/{fecha_fin}')

df["fecha"]= pd.to_datetime(df["fecha"]) # convertir fecha a tipo fecha
# establecer índice en columna fecha
cols_plot = ["fecha","temperatura","humedad","indice"]
df.set_index("fecha", inplace=True)

train_df = df
test_df = df

# escalar datos
scaler = MinMaxScaler()
train_scaled = scaler.fit_transform(train_df[["temperatura","humedad","indice"]])
test_scaled = scaler.transform(test_df[["temperatura","humedad","indice"]])

# crear y entrenar red neuronal
model = Sequential()
model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(3))
model.compile(loss='mse', optimizer='adam')
model.fit(train_scaled, train_scaled, epochs=100, batch_size=1, verbose=0)

# hacer pronósticos
test_predict = model.predict(test_scaled)

# invertir escalamiento para graficar
test_predict = scaler.inverse_transform(test_predict)

# graficar datos de entrenamiento y pronósticos
plt.figure(figsize=(12, 8))
plt.plot(train_df[cols_plot[3]], label='Indice de confort real', color='green')
plt.plot(train_df.index, test_predict[:,2], label='Indice de confort predicción', linestyle='--', color='gray')
plt.legend()
plt.xlabel("Fecha")
plt.ylabel("Indice")
plt.title(f'Indice de Confort Térmico Real vs Pronostico {estacion} ({fecha_ini} - {fecha_fin})')
plt.show()