import numpy as np

def wape(y, yhat):
    y = np.asarray(y); yhat = np.asarray(yhat)
    denom = np.sum(np.abs(y))
    return np.sum(np.abs(y-yhat))/denom if denom != 0 else np.nan

def mae(y, yhat):
    return float(np.mean(np.abs(np.asarray(y)-np.asarray(yhat))))

def p90_abs_error(y, yhat):
    return float(np.quantile(np.abs(np.asarray(y)-np.asarray(yhat)), 0.9))

def max_abs_error(y, yhat):
    return float(np.max(np.abs(np.asarray(y)-np.asarray(yhat))))
