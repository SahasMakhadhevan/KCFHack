import streamlit as st
import pandas as pd

st.title("Dashboard")

selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
selected_time = st.sidebar.selectbox("Time Units", ["Day", "Week", "Month"])


@st.cache
def load_temps():
    data = pd.read_csv(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv", header=None)
    data.columns = ["Time", "Temp"]
    return data


data_load_state = st.text('Loading data...')
temp_data = load_temps()
data_load_state.text('Loading data...done!')

st.write(temp_data.describe())

# Line chart for Temps
st.line_chart(data=temp_data, x="Time", y="Temp", width=0, height=0, use_container_width=True)
