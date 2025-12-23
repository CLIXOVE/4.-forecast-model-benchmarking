def add_time_features(df):
    d = df.copy()
    d["dow"] = d["date"].dt.dayofweek
    d["month"] = d["date"].dt.month
    return d
