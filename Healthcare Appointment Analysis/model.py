import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score, classification_report
import joblib

MODEL_PATH = "model.joblib"

def _prepare_features(df: pd.DataFrame):
    # Select features available in cleaned_dataset.csv
    features = ["gender","age","scholarship","hipertension","diabetes","alcoholism","handcap","sms_received","wait_days","appointment_weekday","neighbourhood"]
    X = df[features].copy()
    y = df["no_show"].copy() if "no_show" in df.columns else None

    # simple cleaning
    X["appointment_weekday"] = X["appointment_weekday"].astype(str)
    X["neighbourhood"] = X["neighbourhood"].astype(str)
    X["gender"] = X["gender"].astype(str).str.upper().fillna("F")
    # ensure numeric columns exist
    for col in ["age","scholarship","hipertension","diabetes","alcoholism","handcap","sms_received","wait_days"]:
        if col not in X.columns:
            X[col] = 0
    return X, y

def _build_pipeline(categorical_cols, numeric_cols):
    num_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
    cat_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("ohe", OneHotEncoder(handle_unknown="ignore"))])
    pre = ColumnTransformer([("num", num_pipe, numeric_cols), ("cat", cat_pipe, categorical_cols)], remainder="drop")
    pipe = Pipeline([("pre", pre), ("clf", RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1))])
    return pipe

def train_model(csv_path: str, save_path: str = MODEL_PATH, test_size: float = 0.2, random_state: int = 42) -> dict:
    df = pd.read_csv(csv_path)
    X, y = _prepare_features(df)
    if y is None:
        raise ValueError("Target column 'no_show' not found in CSV.")
    numeric_cols = ["age","scholarship","hipertension","diabetes","alcoholism","handcap","sms_received","wait_days"]
    categorical_cols = ["gender","appointment_weekday","neighbourhood"]
    pipe = _build_pipeline(categorical_cols, numeric_cols)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    pipe.fit(X_train, y_train)

    preds = pipe.predict(X_test)
    probs = pipe.predict_proba(X_test)[:,1]
    metrics = {
        "accuracy": float(accuracy_score(y_test, preds)),
        "roc_auc": float(roc_auc_score(y_test, probs))
    }

    # save pipeline
    joblib.dump(pipe, save_path)
    return metrics

def load_trained_model(path: str = MODEL_PATH):
    p = Path(path)
    if not p.exists():
        return None
    return joblib.load(path)

def predict_from_df(model, df: pd.DataFrame):
    X, _ = _prepare_features(df)
    probs = model.predict_proba(X)
    return probs