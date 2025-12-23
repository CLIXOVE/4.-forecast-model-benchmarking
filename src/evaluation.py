import pandas as pd
from .metrics import wape, mae, p90_abs_error, max_abs_error

def evaluate(df: pd.DataFrame, ycol: str, pred_col: str) -> dict:
    y = df[ycol].values
    yhat = df[pred_col].values
    return {
        "wape": wape(y, yhat),
        "mae": mae(y, yhat),
        "p90_abs_err": p90_abs_error(y, yhat),
        "max_abs_err": max_abs_error(y, yhat),
        "n": int(len(df))
    }
