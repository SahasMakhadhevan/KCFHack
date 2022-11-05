import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("KCF Tech Dashboard")

@st.cache
def load_temps(nrows):
    data = pd.read_csv(r"/home/sahas/Documents/Git/KCFHack/Data_set/HackPSU/Fan 1/Temperature.csv", nrows=nrows, header=None)
    data.columns = ["Time", "Temp"]
    #data.drop(data[data[' DeltaP'] == 999999].index, inplace = True)
    return data

data_load_state = st.text('Loading data...')
temp_data = load_temps(17190)
data_load_state.text('Loading data...done!')

#Line chart for Temps
st.line_chart(data=temp_data, x="Time", y="Temp", width=0, height=0, use_container_width=True)
