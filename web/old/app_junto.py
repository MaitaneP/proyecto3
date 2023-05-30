# pip install streamlit
# pip install streamlit-lottie
# en la terminal: streamlit hello
# en la terminal desde la carpeta donde está app.py: streamlit run app.py
# emojis: https://unicode.org/emoji/charts/emoji-list.html

import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import pickle 
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
from datetime import datetime 
# import sys
# sys.path.append('../')
# from web import prediccion as pdc

# crear la web
st.set_page_config(page_title="Rental Bikes Number Predictor", page_icon="\U0001F6B2", layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/


# animaciones
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animacion = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_ZSqxIVbhtx.json")

# usar css local
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# sección encabezado
with st.container():
    st.header("\U0001F6B2 RENTAL BIKES NUMBER PREDICTOR \U0001F52E")
    st.title("Welcome to the best \U0001F3C6 \U0001F947 rental bikes number predictor. \U0001F914")
    st.title("It will rock your world. \U0001F600 \U0001F4B6")
    st.subheader("Come on, check it out.")

# cuerpo, columna 1 y 2
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Let's start.")
        st.write("##")
        st.subheader("We need your help for the predictor to do its job.")
        st.write("Please, insert the information regarding the circunstances of the prediction date.")

    with right_column:
        st_lottie(animacion, height=300, key="coding")
        # st.empty()

# cuerpo, pedir variables
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        tipo_modelo = st.text_input("¿What kind of user are you interested in? Please, choose from the following: casual / registered / both")
        fecha = st.text_input("Date for the prediction (YYYY-MM-DD). Please, be advised it needs to be a future date:")
        # estacion = st.text_input("Select a season among the following options: winter / spring / autumn / summer")
        # año = st.text_input("Write the year:")
        # mes = st.text_input("Write the number corresponding to the month: 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12")
        # festivo = st.text_input("Select among the following options: holiday / not holiday")
        temperatura = st.text_input("Write the temperature prediction (ºC):")
    with right_column:
        # dia_semana = st.text_input("Select a weekday among the following options: Sunday / Monday / Tuesday / Wednesday / Thursday / Friday / Saturday")
        # laborable = st.text_input("Select among the following options: workingday / weekend or holiday")
        humedad = st.text_input("Write the humidity prediction (%):")
        viento = st.text_input("Write the windspeed prediction:")

# formulario de contacto
with st.container():
    st.write("---")
    st.header("Get in touch with us!")
    st.write("##")
    # https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/portillamaitane@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()



# TRATAMIENTO DATOS INPUTS
# creamos el df
nuevo_dato = {'date': fecha, 'temp': temperatura, 'hum': humedad, 'windspeed': viento}
fecha = fecha
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
holidays = cal.holidays(start=df['date'].min(), end=df['date'].max())
df['holiday'] = df['date'].isin(holidays)
mapa = {True: 'holiday', False: 'not holiday'}
df['holiday'] = df['holiday'].map(mapa)
# creamos la columna de workingday
def laborables(dato):
    laborables = pd.date_range(start= fecha, end=fecha, freq='B')
    if dato in laborables:
        return 'workingday'
    else:
        return 'weekend or holiday'
    
df['workingday'] = df['date'].apply(laborables)
df.loc[df["holiday"] == 'holiday', "workingday"] = 'weekend or holiday'

# función para obtener season
def estaciones(dato):
    año_func = int(dato[:4])
    primavera = pd.date_range(start= f'{año_func}-03-21', end=f'{año_func}-06-21')
    verano = pd.date_range(start= f'{año_func}-06-22', end=f'{año_func}-09-22')
    otoño = pd.date_range(start= f'{año_func}-09-23', end=f'{año_func}-12-21')
    invierno = pd.date_range(start= f'{año_func}-12-22', end=f'{año_func+1}-03-20')

    if dato in primavera:
        return 'spring'
    elif dato in verano:
        return 'summer'
    elif dato in otoño:
        return 'autumn'
    else:
        return 'winter'
    
df['season'] = estaciones(fecha)
# estadarizamos las numéricas
numericas = df.select_dtypes(include=np.number).drop(['year', 'month'], axis= 1)
with open("../datos/robust.pkl", "rb") as modelo:
    robust = pickle.load(modelo)

x_robust = robust.transform(numericas)
numericas_robust = pd.DataFrame(x_robust, columns=numericas.columns)
df[numericas_robust.columns] = numericas_robust

# transformamos el año
def año_binario(dato):
    if dato <=2018:
        return 0
    else:
        return 1
df['year'] = df['year'].apply(año_binario)
# mapas para encoding
mapa_wd_casual = {'weekend or holiday': 1.0258019525801954, 'workingday': 0.9923291492329149}
mapa_wd_registered = {'weekend or holiday': 1.0152817574021011, 'workingday': 0.9914040114613181}

mapa_se_casual = {'autumn': 0.7475592747559274, 'spring': 1.203626220362622, 'summer': 1.4665271966527196, 'winter': 0.30613668061366806}
mapa_se_registered = {'autumn': 1.039432391867922, 'spring': 1.053759039432392, 'summer': 1.1217082821667348, 'winter': 0.5063446582071224}

mapa_hol_casual = {'holiday': 1.7245467224546722, 'not holiday': 0.9923291492329149}
mapa_hol_registered = {'holiday': 0.7571292127166053, 'not holiday': 1.0081866557511256}

mapa_day_casual = {'Monday': 2.0, 'Thursday': 0.8765690376569037, 'Wednesday': 0.9295676429567643, 'Tuesday': 1.3695955369595536, 'Friday': 0.7496513249651325, 'Saturday': 0.8507670850767085, 'Sunday': 1.2224546722454672}
mapa_day_registered = {'Monday': 4.291492329149233, 'Thursday': 5.652022315202231, 'Wednesday': 5.160390516039052, 'Tuesday': 4.089260808926081, 'Friday': 5.527894002789401, 'Saturday': 5.347977684797769, 'Sunday': 5.182008368200837}

mapa_month_casual = {1: 0.17642956764295675, 2: 0.2824267782426778, 3: 0.7092050209205021, 4: 1.1610878661087867, 5: 1.2370990237099024, 6: 1.3507670850767086, 7: 1.4574616457461647, 8: 1.5495118549511855, 9: 1.3528591352859136, 10: 1.0760111576011158, 11: 0.6262203626220363, 12: 0.40794979079497906}
mapa_month_registered = {1: 2.311715481171548, 2: 2.822873082287308, 3: 3.273361227336123, 4: 4.735704323570432, 5: 5.416317991631799, 6: 6.079497907949791, 7: 5.5864714086471405, 8: 5.741283124128312, 9: 5.804741980474198, 10: 5.598326359832636, 11: 5.225244072524407, 12: 4.400278940027894}

mapa_yr_casual = {0: 0.8563458856345886, 1: 1.2622036262203626}
mapa_yr_registered = {0: 0.7954700504843771, 1: 1.3071360349297312}



# ejecutamos los modelos
# el de casual
df_casual = df.filter(['year', 'weekday', 'workingday', 'temp', 'hum', 'windspeed'], axis=1)
df_casual['year'] = df_casual['year'].map(mapa_yr_casual)
df_casual['weekday'] = df_casual['weekday'].map(mapa_day_casual)
df_casual['workingday'] = df_casual['workingday'].map(mapa_wd_casual)
with open("../datos/mejor_modelo_casual.pkl", "rb") as modelo_cas:
    mejor_modelo_casual = pickle.load(modelo_cas)
conteo_casual = mejor_modelo_casual.predict(df_casual)
rmse_casual = 322
# el de registered
df_registered = df.filter(['season', 'year', 'month', 'weekday', 'temp', 'hum'], axis=1)
df_registered['year'] = df_registered['year'].map(mapa_yr_registered)
df_registered['weekday'] = df_registered['weekday'].map(mapa_day_registered)
df_registered['season'] = df_registered['season'].map(mapa_se_registered)
df_registered['month'] = df_registered['month'].map(mapa_month_registered)
with open("../datos/mejor_modelo_registered.pkl", "rb") as modelo_reg:
    mejor_modelo_registered = pickle.load(modelo_reg)
conteo_registered = mejor_modelo_registered.predict(df_registered)
rmse_registered = 540

# en función del input damos la respuesta
if app.tipo_modelo == 'casual':
    print(f'The estimated number of rental bikes for {fecha} for casual users would be between: {round(conteo_casual[0]-rmse_casual)} - {round(conteo_casual[0]+rmse_casual)}. The model estimates: {round(conteo_casual[0])}.')
elif app.tipo_modelo == 'registered':
    print(f'The estimated number of rental bikes for {fecha} for registered users would be between: {round(conteo_registered[0]-rmse_registered)} - {round(conteo_registered[0]+rmse_registered)}. The model estimates: {round(conteo_registered[0])}.')
else:
    print(f'The estimated number of rental bikes for {fecha} for casual users would be between: {round(conteo_casual[0]-rmse_casual)} - {round(conteo_casual[0]+rmse_casual)}. The model estimates: {round(conteo_casual[0])}.')
    print(f'The estimated number of rental bikes for {fecha} for registered users would be between: {round(conteo_registered[0]-rmse_registered)} - {round(conteo_registered[0]+rmse_registered)}. The model estimates: {round(conteo_registered[0])}.')
