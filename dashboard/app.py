import streamlit as st
import pandas as pd

st.set_page_config(page_title="Taxi Dashboard", layout="wide")

st.title("🚕 Taxi Data Dashboard")

@st.cache_data
def load_data():
    df = pd.read_parquet("data/processed/taxi_data")
    return df

df = load_data()

# ---------------------------
# DATA PREVIEW
# ---------------------------
st.subheader("📊 Sample Data")
st.dataframe(df.head(100))

# ---------------------------
# METRICS
# ---------------------------
st.subheader("📈 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trips", len(df))
col2.metric("Avg Distance", round(df["trip_distance"].mean(), 2))
col3.metric("Max Distance", round(df["trip_distance"].max(), 2))

# ---------------------------
# VISUALS
# ---------------------------
st.subheader("📊 Trip Distance Distribution")

distance_counts = df["trip_distance"].value_counts().head(20)
st.bar_chart(distance_counts)

# ---------------------------
# TIME ANALYSIS
# ---------------------------
st.subheader("⏱ Trips Over Time")

df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
trips_by_day = df.groupby(df["tpep_pickup_datetime"].dt.date).size()

st.line_chart(trips_by_day)
