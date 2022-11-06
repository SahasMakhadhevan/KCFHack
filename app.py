import streamlit as st
import pandas as pd
import time
import datetime
from time import gmtime
import _csv

st.title("KCF Tech Dashboard")

@st.cache

def convertTime(tmpTime):
    #return time.gettime(raw"%Y-%m-%d %H:%M:%S +0000", gmtime())
    #foo = time.gmtime(tmpTime)
    #bar = time.strftime("%a, %d %b %Y %H:%M:%S +0000", foo)
    yeet = datetime.datetime.fromtimestamp(tmpTime)
    print(yeet)
    return yeet

def load_temps():
    data = pd.read_csv(r"Data_set/HackPSU/Fan 1/Temperature.csv", header=None)
    data.columns = ["Time", "Temp"]

    for index, row in data.iterrows():
        data.loc[index, "Time"] = convertTime(row["Time"])

    return data

data_load_state = st.text('Loading data...')
temp_data = load_temps()
data_load_state.text('Loading data...done!')

#Line chart for Temps
st.line_chart(data=temp_data, x="Time", y="Temp", width=0, height=0, use_container_width=True)
