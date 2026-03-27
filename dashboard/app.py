import streamlit as st
import pandas as pd
import os   # ✅ ADD HERE

st.title("🚕 Taxi Data Dashboard")

@st.cache_data
def load_data():   # ✅ REPLACE your existing function with this
    path = "../data/processed/taxi_data"

    st.write("Current working dir:", os.getcwd())
    st.write(
        "Files here:",
        os.listdir("../data/processed") if os.path.exists("../data/processed") else "No folder"
    )

    if not os.path.exists(path):
        st.error(f"Path not found: {path}")
        return pd.DataFrame()

    return pd.read_parquet(path)


# ✅ This stays as is
df = load_data()

st.write(df.head())
