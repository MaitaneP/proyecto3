# pip install streamlit
# pip install streamlit-lottie
# en la terminal: streamlit hello
# en la terminal desde la carpeta donde está app.py: streamlit run app.py
# emojis: https://unicode.org/emoji/charts/emoji-list.html

import requests
import streamlit as st
# from streamlit_lottie import st_lottie

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
        # st_lottie(animacion, height=300, key="coding")
        st.empty()

# cuerpo, pedir variables
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        tipo_modelo = st.text_input("¿What kind of user are you interested in? Please, choose from the following: casual / registered / both")
        fecha = st.text_input("Date for the prediction (YYYY-MM-DD):")
        estacion = st.text_input("Select a season among the following options: winter / spring / autumn / summer")
        año = st.text_input("Write the year:")
        mes = st.text_input("Write the number corresponding to the month: 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12")
        festivo = st.text_input("Select among the following options: holiday / not holiday")

    with right_column:
        dia_semana = st.text_input("Select a weekday among the following options: Sunday / Monday / Tuesday / Wednesday / Thursday / Friday / Saturday")
        laborable = st.text_input("Select among the following options: workingday / weekend or holiday")
        clima = st.text_input("Select a weather type among the following options: clear / cloudy / stormy")
        temperatura = st.text_input("Write the temperature prediction (ºC):")
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