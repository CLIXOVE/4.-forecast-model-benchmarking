from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor

def ridge_model(alpha=1.0):
    return Pipeline([("scaler", StandardScaler()), ("model", Ridge(alpha=alpha))])

def histgbm_model():
    return HistGradientBoostingRegressor(max_depth=5, learning_rate=0.05, max_iter=300, random_state=42)

def rf_model():
    return RandomForestRegressor(n_estimators=300, min_samples_leaf=2, random_state=42, n_jobs=-1)
