import streamlit as st
import requests

st.title("Analisador de Sentimentos - IMDB")

texto = st.text_area("Digite seu review:")

if st.button("Analisar"):
    resp = requests.post(
        "http://127.0.0.1:8000/prever/",
        json={"texto": texto}
    )

    if resp.status_code != 200:
        st.error(f"Erro ao chamar a API: {resp.text}")
    else:
        resposta = resp.json()
        st.write("Sentimento:", resposta["sentimento"])
