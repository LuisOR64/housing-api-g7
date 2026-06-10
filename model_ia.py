import joblib
import numpy as np
import sklearn
from pydantic import BaseModel, Field

model = joblib.load('model/model.pkl')
sc_x = joblib.load('model/scaler_x.pkl')
sc_y = joblib.load('model/scaler_y.pkl')

class HousingIA(BaseModel):
    rooms:int = Field(ge=1)

def predictIA(housingIA: HousingIA):

    rooms_sc = sc_x.transform(np.array([[housingIA.rooms]]))

    prediction_sc = model.predict(rooms_sc)
    prediction = sc_y.inverse_transform(prediction_sc) * 10000

    return prediction[0][0]
