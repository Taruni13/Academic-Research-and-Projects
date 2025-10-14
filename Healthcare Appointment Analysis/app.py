import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from analysis import load_data, summary_stats, plot_target_distribution
from model import train_model, load_trained_model, predict_from_df, MODEL_PATH

st.set_page_config(page_title="Healthcare Appointment Dashboard", layout="wide")
st.title("Healthcare Appointment Analysis")

DATA_PATH = "cleaned_dataset.csv"

@st.cache_data
def load_cached(path):
    return load_data(path)

df = load_cached(DATA_PATH)

# Sidebar filters
st.sidebar.header("Filters & Actions")
age_min, age_max = st.sidebar.slider("Age range", int(df.age.min()), int(df.age.max()), (0, 100))
weekday = st.sidebar.multiselect("Appointment weekday", sorted(df.appointment_weekday.unique().tolist()), default=sorted(df.appointment_weekday.unique().tolist()))
neigh_sel = st.sidebar.multiselect("Neighbourhood (top 10)", df.neighbourhood.value_counts().nlargest(10).index.tolist(), default=None)

btn_train = st.sidebar.button("Train model")
btn_reload_model = st.sidebar.button("Load model")

# Apply filters
filtered = df[(df.age >= age_min) & (df.age <= age_max) & (df.appointment_weekday.isin(weekday if weekday else df.appointment_weekday.unique()))]
if neigh_sel:
    filtered = filtered[filtered.neighbourhood.isin(neigh_sel)]

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Dataset sample")
    st.dataframe(filtered.sample(min(200, len(filtered))))

    st.subheader("Summary statistics")
    st.write(summary_stats(filtered))

    st.subheader("Target distribution (no_show)")
    fig, ax = plot_target_distribution(filtered, "no_show")
    st.pyplot(fig)

with col2:
    st.subheader("Quick charts")
    fig, ax = plt.subplots(2, 1, figsize=(4,6))
    sns.countplot(x="no_show", data=filtered, ax=ax[0])
    ax[0].set_title("No-show counts")
    sns.histplot(filtered.wait_days.dropna(), bins=20, ax=ax[1])
    ax[1].set_title("Wait days distribution")
    plt.tight_layout()
    st.pyplot(fig)

# Model actions
st.markdown("---")
st.subheader("Model")

if btn_train:
    with st.spinner("Training model..."):
        metrics = train_model(DATA_PATH, save_path=MODEL_PATH)
    st.success("Model trained")
    st.json(metrics)

if btn_reload_model:
    mdl = load_trained_model()
    if mdl is not None:
        st.success("Model loaded")
    else:
        st.error("No saved model found. Train first.")

# Simple prediction UI
st.subheader("Ad-hoc prediction")
mdl = load_trained_model()
if mdl is None:
    st.info("Train or load a model to enable predictions.")
else:
    sample = {}
    sample["gender"] = st.selectbox("Gender", ["F","M"])
    sample["age"] = st.number_input("Age", min_value=0, max_value=120, value=30)
    sample["scholarship"] = st.selectbox("Scholarship", [0,1])
    sample["hipertension"] = st.selectbox("Hipertension", [0,1])
    sample["diabetes"] = st.selectbox("Diabetes", [0,1])
    sample["alcoholism"] = st.selectbox("Alcoholism", [0,1])
    sample["handcap"] = st.selectbox("Handcap", [0,1,2,3,4])
    sample["sms_received"] = st.selectbox("SMS received", [0,1])
    sample["wait_days"] = st.number_input("Wait days", value=0)
    sample["appointment_weekday"] = st.selectbox("Weekday", sorted(df.appointment_weekday.unique()))
    sample["neighbourhood"] = st.selectbox("Neighbourhood (top)", df.neighbourhood.value_counts().nlargest(20).index.tolist())

    if st.button("Predict no-show"):
        sample_df = pd.DataFrame([sample])
        pred = predict_from_df(mdl, sample_df)
        st.write("Predicted probability of no-show:", float(pred[0,1]))