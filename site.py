import streamlit as st
import requests

st.title("Analisador de Sentimentos - IMDB")

texto = st.text_area("Digite seu review:")

if st.button("Analisar"):
    resposta = requests.post(
        "http://127.0.0.1:8000/prever/",
        params={"texto": texto}
    ).json()

    st.write("Sentimento:", resposta["sentimento"])
