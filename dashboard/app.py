import streamlit as st
import pandas as pd
import mysql.connector

st.title("🚕 Taxi Data Dashboard")

@st.cache_data
def load_data():
conn = mysql.connector.connect(
host="localhost",   # change if remote
user="root",
password="root",
database="taxi_db"
)

```
query = "SELECT * FROM taxi_trips LIMIT 10000"
df = pd.read_sql(query, conn)
conn.close()
return df
```

df = load_data()

st.subheader("📊 Sample Data")
st.dataframe(df)

st.subheader("📈 Trip Distance Distribution")
st.bar_chart(df["trip_distance"].value_counts().head(20))

st.subheader("⏱ Avg Trip Distance")
st.metric("Average Distance", round(df["trip_distance"].mean(), 2))
