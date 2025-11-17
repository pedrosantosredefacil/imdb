from fastapi import FastAPI
import joblib

# Carregar modelo e vetorizador
modelo = joblib.load("modelo_sentimentos.pkl")
vetorizador = joblib.load("vetorizador_tfidf.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API de Análise de Sentimentos IMDB está rodando!"}

@app.post("/prever/")
def prever_sentimento(texto: str):
    X = vetorizador.transform([texto])
    pred = modelo.predict(X)[0]
    return {"sentimento": pred}

