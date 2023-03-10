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

    #returns a DataFrame of one row with two columns : proba to be 0 & proba to be 1
    y_pred = model.predict(X_pred)[0]

    y_pred_proba_zero = model.predict_proba(X_pred)[0][0]
    y_pred_proba_one = model.predict_proba(X_pred)[0][1]

    return {'y_pred_proba_zero':y_pred_proba_zero,
        'y_pred_proba_one': y_pred_proba_one,
        'default':y_pred}

@app.get("/")
def root():
    return {'greeting':'Hihi'}
