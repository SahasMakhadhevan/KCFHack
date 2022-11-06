import streamlit as st
import pandas as pd
import DataLoading

st.title("Dashboard")

selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
selected_time = st.sidebar.selectbox("Time Units", ["Day", "Week", "Month"])


data_load_state = st.text('Loading data...')
temperature_data = DataLoading.load_temps(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv")
data_load_state.text('Loading data...done!')

st.write(temperature_data.describe())

# Line chart for Temps
st.line_chart(data=temperature_data, x="Time", y="Temp", width=0, height=0, use_container_width=True)
