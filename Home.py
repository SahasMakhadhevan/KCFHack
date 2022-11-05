import streamlit as st
import pandas as pd

st.title("KCF Home")

selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2"])
selected_time = st.sidebar.selectbox("Time Units", ["Day", "Week", "Month"])

@st.cache
def load_temps():
    data = pd.read_csv(r"Data_set/HackPSU/Fan 1/Temperature.csv", header=None)
    data.columns = ["Time", "Temp"]
    return data


data_load_state = st.text('Loading data...')
temp_data = load_temps()
data_load_state.text('Loading data...done!')

# Line chart for Temps
st.line_chart(data=temp_data, x="Time", y="Temp", width=0, height=0, use_container_width=True)
