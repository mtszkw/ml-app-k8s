import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

from fastapi import FastAPI, Request
from pydantic import BaseModel


class BostonHouseFeatures(BaseModel):
    crim: float # per capita crime rate by town
    zn: float # proportion of residential land zoned for lots over 25,000 sq.ft.
    indus: float # proportion of non-retail business acres per town
    chas: float # Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
    nox: float # nitric oxides concentration (parts per 10 million)
    rm: float # average number of rooms per dwelling
    age: float # proportion of owner-occupied units built prior to 1940
    dis: float # weighted distances to five Boston employment centres
    rad: float # index of accessibility to radial highways
    tax: float # full-value property-tax rate per $10,000
    ptratio: float # pupil-teacher ratio by town
    b: float # 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
    lstat: float # % lower status of the population


# uvicorn boston_inference:app --reload
app = FastAPI()

xgb = XGBRegressor()
xgb.load_model("xgbregressor_boston.json")

@app.post("/predict")
async def predict_house_price(features: BostonHouseFeatures):
    
    X = np.array(list(features.dict().values()))
    y = float(xgb.predict(np.expand_dims(X, axis=0))[0])
    return {"price": y}