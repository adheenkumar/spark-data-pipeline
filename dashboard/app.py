import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Taxi Dashboard", layout="wide")

st.title("🚕 Taxi Data Dashboard")

# =========================
# Load Data
# =========================
@st.cache_data
def load_data():
    path = "data/processed/taxi_data"

    if not os.path.exists(path):
        st.error(f"Path not found: {path}")
        return pd.DataFrame()

    df = pd.read_parquet(path)

    # Convert datetime
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

    # Feature engineering
    df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
    df["pickup_date"] = df["tpep_pickup_datetime"].dt.date

    return df


df = load_data()

if df.empty:
    st.stop()

# =========================
# Sidebar Filters
# =========================
st.sidebar.header("🔎 Filters")

min_dist, max_dist = st.sidebar.slider(
    "Trip Distance Range",
    float(df["trip_distance"].min()),
    float(df["trip_distance"].max()),
    (float(df["trip_distance"].min()), float(df["trip_distance"].max()))
)

selected_hour = st.sidebar.multiselect(
    "Pickup Hour",
    options=sorted(df["pickup_hour"].unique()),
    default=sorted(df["pickup_hour"].unique())
)

# Apply filters
filtered_df = df[
    (df["trip_distance"] >= min_dist) &
    (df["trip_distance"] <= max_dist) &
    (df["pickup_hour"].isin(selected_hour))
]

# =========================
# KPIs
# =========================
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trips", len(filtered_df))
col2.metric("Avg Distance", round(filtered_df["trip_distance"].mean(), 2))
col3.metric("Max Distance", round(filtered_df["trip_distance"].max(), 2))

# =========================
# Charts
# =========================

st.subheader("📈 Trips by Pickup Hour")

hourly_trips = filtered_df.groupby("pickup_hour").size()
st.line_chart(hourly_trips)

# -------------------------

st.subheader("📊 Distance Distribution")

st.bar_chart(filtered_df["trip_distance"])

# -------------------------

st.subheader("📅 Trips Over Time")

daily_trips = filtered_df.groupby("pickup_date").size()
st.line_chart(daily_trips)

# =========================
# Data Table
# =========================

st.subheader("📄 Sample Data")
st.dataframe(filtered_df.head(100))
