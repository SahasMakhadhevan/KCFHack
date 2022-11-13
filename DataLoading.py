import pandas as pd
import streamlit as st


@st.cache
def load_data(path, num_rows):
    data = pd.read_csv(path, header=None, nrows=num_rows)
    data.columns = ["Time", "Value"]
    data["Time"] = pd.to_datetime(data["Time"], unit="ms")
    return data


@st.cache
def load_alerts_data(path):
    data = pd.read_csv(path, header=None)
    data.columns = ["Time", "Value"]
    data["Time"] = pd.to_datetime(data["Time"], unit="ms")
    return data
