import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd

app = FastAPI()

import pickle


with open("/Users/akshitbansal/Desktop/anomaly-detection-stgi/regressor_model.pkl", 'rb') as file:
    model = pickle.load(file)

@app.get('/')
def index():
    return {'message': 'Hello, Worlddddd'}




