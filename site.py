import streamlit as st
import requests

st.set_page_config(page_title="Analisador de Sentimentos", page_icon="🎬", layout="wide")

st.title("🎬 Analisador de Sentimentos IMDB")

st.write("Digite abaixo um review de filme para analisar o sentimento:")

texto = st.text_area("Review:", height=150)

if st.button("🔍 Analisar Sentimento"):
    if not texto.strip():
        st.error("Digite um texto antes de analisar.")
    else:
        resp = requests.post("http://127.0.0.1:8000/prever/", json={"texto": texto})

        if resp.status_code != 200:
            st.error(f"Erro ao chamar a API: {resp.text}")
        else:
            resposta = resp.json()

            sentimento = resposta["sentimento"]
            prob = resposta["probabilidade"]
            detalhes = resposta["detalhes"]

            if sentimento == 1:
                st.success("🎉 Sentimento: **POSITIVO**")
            else:
                st.error("😞 Sentimento: **NEGATIVO**")

            st.subheader("Probabilidade do Modelo")
            st.progress(prob)

            st.write("🔎 **Detalhes:**")
            st.write(f"- Positivo: {detalhes['positivo']:.4f}")
            st.write(f"- Negativo: {detalhes['negativo']:.4f}")