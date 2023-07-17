import pandas as pnd
import matplotlib.pyplot as mplt # Esta función es utilizada para mostrar los gráficos
import seaborn as sbn

fecha_ini = '1990-01-01'
fecha_fin = '2000-01-31'
estacion = 'Los Naranjos'
opsd_dia = pnd.read_json(f'http://200.89.81.42:8100/api/HistoricosProcesados/{estacion.replace(" ","%20")}/{fecha_ini}/{fecha_fin}')

opsd_dia['fecha'] = pnd.to_datetime(opsd_dia['fecha'])
opsd_dia = opsd_dia.set_index('fecha')

opsd_dia['Año'] = opsd_dia.index.year
opsd_dia['Mes'] = opsd_dia.index.month
opsd_dia['Dia'] = opsd_dia.index.day_name()

sbn.set(rc={'figure.figsize':(10, 5)})
opsd_dia['indice'].plot(linewidth=0.4)

col_graf = ['indice']
ejes = opsd_dia[col_graf].plot(marker='.', alpha=0.1, linestyle='None',figsize=(10,10),subplots=True)
for eje in ejes:
  eje.set_ylabel('Diario')

eje = opsd_dia.loc[fecha_ini:fecha_fin, 'indice'].plot(marker='o',linestyle='-')
eje.set_ylabel('Diario')

fig, ejes = mplt.subplots(3, 1, figsize=(11, 10), sharex=True)
for nombre, eje in zip(['indice'], ejes):
    sbn.boxplot(data=opsd_dia,x='Mes',y=nombre,ax=eje)
    eje.set_title(nombre)
    if eje != ejes[-1]:
        eje.set_xlabel('')

sbn.boxplot(data=opsd_dia, x='Dia', y='indice')

inicio, final = fecha_ini,fecha_fin
fig,eje = mplt.subplots()
eje.plot(opsd_dia.loc[inicio:final,'indice'],marker='.',linestyle='-',linewidth=0.5,label='Diario')
eje.plot(media_opsd_semanal.loc[inicio:final,'indice'],marker='o',markersize=5,label='Semanal')
eje.set_ylabel('Indice')
eje.legend()

fig,eje = mplt.subplots()
eje.plot(opsd_mensual['indice'],color='black',label='indice')
opsd_mensual[['temperatura','humedad']].plot.area(ax=eje,linewidth=0)
eje.legend()
eje.set_ylabel('Total Mensual')

##################################################################

import pandas as pnd
import matplotlib.pyplot as mplt
import seaborn as sbn

sbn.set(rc={'figure.figsize':(10, 5)})

opsd_dia = pnd.read_json(f'http://200.89.81.42:8100/api/HistoricosProcesados/{estacion.replace(" ","%20")}/{fecha_ini}/{fecha_fin}')
opsd_dia['fecha'] = pnd.to_datetime(opsd_dia['fecha'])
opsd_dia = opsd_dia.set_index('fecha')

opsd_7d = opsd_dia[columnas].rolling(7, center=True).mean()

#inicio, final='1995-06','1995-12'
inicio, final = fecha_ini,fecha_fin
fig, eje = mplt.subplots()
eje.plot(opsd_dia.loc[inicio:final, 'indice'],marker='.',linestyle='-', linewidth=0.5,label='Diario')
eje.plot(media_opsd_semanal.loc[inicio:final,'indice'],marker='o',linestyle='-', linewidth=0.5,label='Semanal')
eje.plot(opsd_7d.loc[inicio:final,'indice'],marker='.',linestyle='-', linewidth=0.5,label='Media Deslizante de 7 Dias')
eje.set_ylabel('Indice de Confort')
eje.legend()

import pandas as pnd
import matplotlib.pyplot as mplt
import seaborn as sbn

sbn.set(rc={'figure.figsize':(10, 5)})

opsd_dia = pnd.read_json(f'http://200.89.81.42:8100/api/HistoricosProcesados/{estacion.replace(" ","%20")}/{fecha_ini}/{fecha_fin}')
opsd_dia['fecha'] = pnd.to_datetime(opsd_dia['fecha'])
opsd_dia = opsd_dia.set_index('fecha')
opsd_365d = opsd_dia[columnas].rolling(window=365,center=True,min_periods=360).mean()
opsd_7d = opsd_dia[columnas].rolling(7, center=True).mean()

fig, eje = mplt.subplots()
eje.plot(opsd_dia['indice'], marker='.', markersize=2, color='0.6',linestyle='None', label='Diario')
eje.plot(opsd_7d['indice'], linewidth=2, label='Media deslizante semanal')
eje.plot(opsd_365d['indice'], color='0.2', linewidth=3,
label='Tendencia (Media deslizante anual)')
eje.legend()
eje.set_xlabel('Año')
eje.set_ylabel('Indice de confort')
eje.set_title('Tendencias en el Indice de Confort')