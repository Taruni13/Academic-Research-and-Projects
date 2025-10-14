import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # ensure types consistent with preprocess.py
    if "scheduledday" in df.columns:
        df["scheduledday"] = pd.to_datetime(df["scheduledday"], errors="coerce")
    if "appointmentday" in df.columns:
        df["appointmentday"] = pd.to_datetime(df["appointmentday"], errors="coerce")
    return df

def summary_stats(df: pd.DataFrame) -> dict:
    out = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_per_column": df.isna().sum().to_dict(),
        "unique_counts": df.nunique(dropna=False).to_dict(),
        "numeric_describe": df.select_dtypes(include=[np.number]).describe().to_dict()
    }
    return out

def plot_target_distribution(df: pd.DataFrame, target: str):
    if target not in df.columns:
        raise ValueError(f"{target} not in df")

    # create explicit figure/axes instead of relying on global plt
    fig, ax = plt.subplots(figsize=(6, 4))
    if df[target].dtype.kind in "biu" or df[target].nunique() <= 10:
        sns.countplot(x=target, data=df, ax=ax)
    else:
        sns.histplot(df[target].dropna(), kde=True, ax=ax)

    ax.set_title(f"Distribution: {target}")
    fig.tight_layout()
    return fig, ax