import streamlit as st
import pandas as pd
import os   # ✅ ADD HERE

st.title("🚕 Taxi Data Dashboard")

@st.cache_data
def load_data():
    path = "data/processed/taxi_data"

    if os.path.exists(path):
        return pd.read_parquet(path)

    st.warning("Using fallback dataset")
    return pd.DataFrame({
        "message": ["No data available"]
    })

# ✅ This stays as is
df = load_data()

st.write(df.head())
