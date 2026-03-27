import streamlit as st
import pandas as pd

st.title("🚕 Taxi Data Dashboard")

@st.cache_data
def load_data():
    return pd.read_parquet("../data/processed/taxi_data")

df = load_data()

st.subheader("📊 Sample Data")
st.dataframe(df)

st.subheader("📈 Trip Distance Distribution")
st.bar_chart(df["trip_distance"].value_counts().head(20))

st.subheader("⏱ Avg Trip Distance")
st.metric("Average Distance", round(df["trip_distance"].mean(), 2))
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
trips_by_day = df.groupby(df["tpep_pickup_datetime"].dt.date).size()

st.line_chart(trips_by_day)
