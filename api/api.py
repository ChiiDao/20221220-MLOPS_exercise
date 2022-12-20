from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

modelpath = "model/model.sav"
app.state.model = pickle.load(open(modelpath, 'rb'))


@app.get("/predict")
def predict(sum_paid_inv_0_12m: int,  # 92027
            time_hours: float):    # 20.267500

    X_pred = pd.DataFrame(dict(
        sum_paid_inv_0_12m=[sum_paid_inv_0_12m],
        time_hours=[time_hours]))

    model = app.state.model

    y_pred = model.predict(X_pred)

    return {'default' : int(y_pred)}

@app.get("/")
def root():
    return {'greeting':'Hihi'}
