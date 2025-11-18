from fastapi import FastAPI
from pydantic import BaseModel
import joblib

modelo = joblib.load("modelo_sentimentos.pkl")
vetorizador = joblib.load("vetorizador_tfidf.pkl")

class Entrada(BaseModel):
    texto: str

app = FastAPI()

@app.post("/prever/")
def prever_sentimento(dados: Entrada):
    X = vetorizador.transform([dados.texto])
    pred = modelo.predict(X)[0]
    proba = modelo.predict_proba(X)[0]

    return {
        "sentimento": int(pred),
        "probabilidade": float(max(proba)),  # maior probabilidade (positivo ou negativo)
        "detalhes": {
            "negativo": float(proba[0]),
            "positivo": float(proba[1])
        }
    }
