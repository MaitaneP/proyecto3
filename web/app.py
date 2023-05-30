# pip install streamlit
# pip install streamlit-lottie
# en la terminal: streamlit hello
# en la terminal desde la carpeta donde está app.py: streamlit run app.py
# emojis: https://unicode.org/emoji/charts/emoji-list.html

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd
import numpy as np
import sys
sys.path.append('../')
from web import prediccion as pdc


# crear la web
st.set_page_config(page_title="Rental Bikes Number Predictor", page_icon="\U0001F6B2", layout="wide")


# animaciones
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animacion = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_ZSqxIVbhtx.json")


# logo
logo = Image.open('images/logo.png')


# usar css local
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# sección encabezado y logo a dos columnas
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(logo)
    with text_column:
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
        st.write("##")
        st.subheader("Please, insert the information regarding the circunstances of the prediction date.")
        st.subheader("\U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4 \U0001F6B4")
    with right_column:
        st_lottie(animacion, height=350, key="coding")
        # st.empty()
    st.write("##") # fila en blanco


# cuerpo, pedir variables, a dos columnas
with st.form(key='form_predictoras'):
    left_column, right_column = st.columns(2)
    with left_column:
        #tipo_modelo = st.text_input("¿What kind of user are you interested in? Please, choose from the following: casual / registered / both")
        tipo_modelo = st.selectbox("¿What kind of user are you interested in?", ["casual", "registered", "both"])
        fecha = st.date_input("Select the date for the prediction. Please, be advised it needs to be a future date:")
        # fecha = st.text_input("Date for the prediction (YYYY-MM-DD). Please, be advised it needs to be a future date:")
        temperatura = st.text_input("Write the temperature prediction (ºC):")
        # temperatura = st.number_input("Write the temperature prediction (ºC):", format="%.3f", lang='en_EN')
    with right_column:
        humedad = st.text_input("Write the humidity prediction (%):")
        viento = st.text_input("Write the windspeed prediction:")
        # humedad = st.number_input("Write the humidity prediction (%):", format="%.3f", lang='en_EN')
        # viento = st.number_input("Write the windspeed prediction:", format="%.3f", lang='en_EN')
    submit_button = st.form_submit_button()

if submit_button:
    st.success(f"Thank you for inserting the data. Our model is working to give you ASAP a prediction for {fecha}.")
    casual_pred, casual_min, casual_max, regist_pred, regist_min, regist_max = pdc.predictor_bicis(fecha, temperatura, humedad, viento)
    if tipo_modelo == 'casual':
        with st.expander("Results"):
            df = pd.DataFrame({'User type': 'casual', 'Estimated value': casual_pred, 'Probable min': casual_min, 'Probable max': casual_max}, index = [0])
            st.dataframe(df)
    elif tipo_modelo == 'registered':
        with st.expander("Results"):
            df = pd.DataFrame({'User type': 'registered', 'Estimated value': regist_pred, 'Probable min': regist_min, 'Probable max': regist_max}, index = [0])
            st.dataframe(df)
    else:
        with st.expander("Results"):
            df = pd.DataFrame({'User type':['casual', 'registered'], 'Estimated value':[casual_pred, regist_pred], 'Probable min':[casual_min, regist_min], 'Probable max':[casual_max, regist_max]}, index = [0, 1])
            st.dataframe(df)


# formulario de contacto
with st.container():
    st.write("##") # fila en blanco
    st.write("##") # fila en blanco
    st.header("Get in touch with us!")
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



# en función del input damos la respuesta
# if tipo_modelo == '':
#     pass
# else:
#     if tipo_modelo == 'casual':
#         print(f'The estimated number of rental bikes for {fecha} for casual users would be between: {round(pdc.conteo_casual[0]-pdc.rmse_casual)} - {round(pdc.conteo_casual[0]+pdc.rmse_casual)}. The model estimates: {round(pdc.conteo_casual[0])}.')
#     elif tipo_modelo == 'registered':
#         print(f'The estimated number of rental bikes for {fecha} for registered users would be between: {round(pdc.conteo_registered[0]-pdc.rmse_registered)} - {round(pdc.conteo_registered[0]+pdc.rmse_registered)}. The model estimates: {round(pdc.conteo_registered[0])}.')
#     else:
#         print(f'The estimated number of rental bikes for {fecha} for casual users would be between: {round(pdc.conteo_casual[0]-pdc.rmse_casual)} - {round(pdc.conteo_casual[0]+pdc.rmse_casual)}. The model estimates: {round(pdc.conteo_casual[0])}.')
#         print(f'The estimated number of rental bikes for {fecha} for registered users would be between: {round(pdc.conteo_registered[0]-pdc.rmse_registered)} - {round(pdc.conteo_registered[0]+pdc.rmse_registered)}. The model estimates: {round(pdc.conteo_registered[0])}.')
