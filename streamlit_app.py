import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_BASE = "http://localhost:8000"

st.title("Weather Dashboard (POC)")

city = st.text_input("City", "London")

if st.button("Load Data"):
    resp = requests.get(f"{API_BASE}/history/{city}?limit=100")
    if resp.status_code != 200:
        st.error(f"API error: {resp.status_code}")
    else:
        data = resp.json()
        records = data.get("records", [])
        if not records:
            st.info("No data found for that city.")
        else:
            df = pd.DataFrame(records)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df.set_index('timestamp', inplace=True)

            st.subheader(f"Latest readings for {city}")
            last = df.iloc[-1]
            st.write({
                "Temperature (°C)": float(last['temp_c']),
                "Humidity (%)": float(last['humidity']),
                "Pressure (hPa)": float(last['pressure']),
                "Description": last.get('description', "")
            })

            st.subheader("Temperature Trend")
            fig, ax = plt.subplots()
            df['temp_c'].plot(ax=ax)
            ax.set_ylabel("Temperature (°C)")
            ax.set_xlabel("Time")
            st.pyplot(fig)

            st.subheader("Humidity Trend")
            fig2, ax2 = plt.subplots()
            df['humidity'].plot(ax=ax2)
            ax2.set_ylabel("Humidity (%)")
            ax2.set_xlabel("Time")
            st.pyplot(fig2)

            st.subheader("Aggregations")
            st.write("Mean temperature:", round(df['temp_c'].mean(), 2))
            st.write("Max temperature:", round(df['temp_c'].max(), 2))
            st.write("Min temperature:", round(df['temp_c'].min(), 2))
