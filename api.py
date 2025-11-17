from fastapi import FastAPI
import joblib
import pandas as pd

# Carregar o modelo treinado
modelo = joblib.load("modelo_sentimentos.pkl")

# Carregar o TF-IDF usado no treino
vetorizador = joblib.load("vetorizador_tfidf.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API de Análise de Sentimentos IMDB está rodando!"}

@app.post("/prever/")
def prever_sentimento(texto: str):
    # Transformar texto recebido pela API em vetor TF-IDF
    X = vetorizador.transform([texto])
    # Fazer previsão
    pred = modelo.predict(X)[0]
    return {"sentimento": pred}

