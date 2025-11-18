import streamlit as st
import requests

st.title("Classificador de Sentimentos IMDB 🎬")

texto = st.text_area("Digite um texto para análise:")

API_URL = "https://imdb-1-t4lm.onrender.com/prever/"

if st.button("Analisar"):
    if not texto.strip():
        st.warning("Digite algum texto antes de analisar.")
    else:
        try:
            resp = requests.post(API_URL, json={"texto": texto})

            if resp.status_code == 200:
                dados = resp.json()

                sentimento = "👍 Positivo" if dados["sentimento"] == 1 else "👎 Negativo"

                st.success(f"Sentimento detectado: **{sentimento}**")
                st.write("### Probabilidade:")
                st.write(f"- Positivo: **{dados['detalhes']['positivo']:.4f}**")
                st.write(f"- Negativo: **{dados['detalhes']['negativo']:.4f}**")

            else:
                st.error(f"Erro ao chamar API: {resp.status_code}")
        except Exception as e:
            st.error(f"Erro: {str(e)}")
