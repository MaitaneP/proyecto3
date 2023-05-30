import pandas as pd
import numpy as np
import pickle 
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
from datetime import datetime 
# import sys
# sys.path.append('../')
# from web import app as app


# FUNCIÓN
def predictor_bicis(date, temperature, humidity, windspeed):
    # creamos el df
    nuevo_dato = {'date': date, 'temp': float(temperature), 'hum': float(humidity), 'windspeed': float(windspeed)}
    df = pd.DataFrame(nuevo_dato, index=[0])
    # pasamos la columna a formato datetime
    df['date'] = pd.to_datetime(df['date'])
    #creamos la columna year
    df['year'] = df['date'].dt.year
    #creamos la columna month
    df['month'] = df['date'].dt.month
    # creamos la columna weekday
    df["weekday"]= df["date"].dt.day_name()
    # comprobamos si es festivo
    cal = calendar() #llamada al calendario
    holidays = cal.holidays(start=df['date'].min(), end=df['date'].max()) # sacamos el listado de festivos
    df['holiday'] = df['date'].isin(holidays) # comprobamos si en la lista de festivos están nuestras fechas
    mapa = {True: 'holiday', False: 'not holiday'} # cambiamos el resultado con un map
    df['holiday'] = df['holiday'].map(mapa)
    # creamos la columna de workingday
    laborables = pd.date_range(start= date, end=date, freq='B')
    if date in laborables:
        df['workingday'] = 'workingday'
    else:
        df['workingday'] = 'weekend or holiday'
    # función para obtener season
    # año_func = int(date[:4])
    año_func = df['date'].dt.year[0]
    primavera = pd.date_range(start= f'{año_func}-03-21', end=f'{año_func}-06-21')
    verano = pd.date_range(start= f'{año_func}-06-22', end=f'{año_func}-09-22')
    otoño = pd.date_range(start= f'{año_func}-09-23', end=f'{año_func}-12-21')
    # invierno = pd.date_range(start= f'{año_func}-12-22', end=f'{año_func+1}-03-20')
    if date in primavera:
        df['season'] = 'spring'
    elif date in verano:
        df['season'] = 'summer'
    elif date in otoño:
        df['season'] = 'autumn'
    else:
        df['season'] = 'winter'
    # estandarizacion
    numericas = df.select_dtypes(include=np.number).drop(['year', 'month'], axis= 1)
    with open("../datos/robust.pkl", "rb") as modelo:
        robust = pickle.load(modelo)
    x_robust = robust.transform(numericas)
    numericas_robust = pd.DataFrame(x_robust, columns=numericas.columns)
    df[numericas_robust.columns] = numericas_robust
    # apañamos el año
    if df.loc[0, 'year'] <=2018:
        df['year'] = 0
    else:
        df['year'] = 1
    # mapas para el encoding
    mapa_wd_casual = {'weekend or holiday': 1.0258019525801954, 'workingday': 0.9923291492329149}
    # mapa_wd_registered = {'weekend or holiday': 1.0152817574021011, 'workingday': 0.9914040114613181}
    # mapa_se_casual = {'autumn': 0.7475592747559274, 'spring': 1.203626220362622, 'summer': 1.4665271966527196, 'winter': 0.30613668061366806}
    mapa_se_registered = {'autumn': 1.039432391867922, 'spring': 1.053759039432392, 'summer': 1.1217082821667348, 'winter': 0.5063446582071224}
    # mapa_hol_casual = {'holiday': 1.7245467224546722, 'not holiday': 0.9923291492329149}
    # mapa_hol_registered = {'holiday': 0.7571292127166053, 'not holiday': 1.0081866557511256}
    mapa_day_casual = {'Monday': 2.0, 'Thursday': 0.8765690376569037, 'Wednesday': 0.9295676429567643, 'Tuesday': 1.3695955369595536, 'Friday': 0.7496513249651325, 'Saturday': 0.8507670850767085, 'Sunday': 1.2224546722454672}
    mapa_day_registered = {'Monday': 4.291492329149233, 'Thursday': 5.652022315202231, 'Wednesday': 5.160390516039052, 'Tuesday': 4.089260808926081, 'Friday': 5.527894002789401, 'Saturday': 5.347977684797769, 'Sunday': 5.182008368200837}
    # mapa_month_casual = {1: 0.17642956764295675, 2: 0.2824267782426778, 3: 0.7092050209205021, 4: 1.1610878661087867, 5: 1.2370990237099024, 6: 1.3507670850767086, 7: 1.4574616457461647, 8: 1.5495118549511855, 9: 1.3528591352859136, 10: 1.0760111576011158, 11: 0.6262203626220363, 12: 0.40794979079497906}
    mapa_month_registered = {1: 2.311715481171548, 2: 2.822873082287308, 3: 3.273361227336123, 4: 4.735704323570432, 5: 5.416317991631799, 6: 6.079497907949791, 7: 5.5864714086471405, 8: 5.741283124128312, 9: 5.804741980474198, 10: 5.598326359832636, 11: 5.225244072524407, 12: 4.400278940027894}
    mapa_yr_casual = {0: 0.8563458856345886, 1: 1.2622036262203626}
    mapa_yr_registered = {0: 0.7954700504843771, 1: 1.3071360349297312}
    # creamos los df de casual y registered
    df_casual = df.filter(['year', 'weekday', 'workingday', 'temp', 'hum', 'windspeed'], axis=1)
    df_registered = df.filter(['season', 'year', 'month', 'weekday', 'temp', 'hum'], axis=1)
    # encoding
    df_casual['year'] = df_casual['year'].map(mapa_yr_casual)
    df_registered['year'] = df_registered['year'].map(mapa_yr_registered)
    df_casual['weekday'] = df_casual['weekday'].map(mapa_day_casual)
    df_registered['weekday'] = df_registered['weekday'].map(mapa_day_registered)
    df_casual['workingday'] = df_casual['workingday'].map(mapa_wd_casual)
    df_registered['season'] = df_registered['season'].map(mapa_se_registered)
    df_registered['month'] = df_registered['month'].map(mapa_month_registered)
    # abrimos los modelos
    with open("../datos/mejor_modelo_casual.pkl", "rb") as modelo_cas:
        mejor_modelo_casual = pickle.load(modelo_cas)
    with open("../datos/mejor_modelo_registered.pkl", "rb") as modelo_reg:
        mejor_modelo_registered = pickle.load(modelo_reg)
    # realizamos las predicciones
    conteo_casual = mejor_modelo_casual.predict(df_casual)
    conteo_registered = mejor_modelo_registered.predict(df_registered)
    rmse_casual = 322.167752
    rmse_registered = 540.794549
    cas_min = round(conteo_casual[0] - rmse_casual)
    cas_max = round(conteo_casual[0] + rmse_casual)
    reg_min = round(conteo_registered[0] - rmse_registered)
    reg_max = round(conteo_registered[0] + rmse_registered)
    return round(conteo_casual[0]), cas_min, cas_max, round(conteo_registered[0]), reg_min, reg_max
