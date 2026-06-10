from fastapi import FastAPI
from model_ia import predictIA, HousingIA

app = FastAPI()

@app.get("/")
def index():
    return {
        "name": "kagari"
        }

@app.post("/housing_ia")
def housing_predict(housing: HousingIA):
    price = predictIA(housing)

    return {
        "rooms": housing.rooms,
        "price": price
    }