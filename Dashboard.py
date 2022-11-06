import streamlit as st
import pandas as pd
import DataLoading
import altair as alt

st.title("Dashboard")

selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
selected_aggregate = st.sidebar.selectbox("Aggregate", ["Day", "Week", "Month"])
#Aggregrating on Day

#switch selected_aggregate:



data_load_state = st.text('Loading data...')
temperature_data = DataLoading.load_temps(selected_fan)
data_load_state.text('Loading data...done!')

st.write(temperature_data.describe())

# Line chart for Temps
linechart = alt.Chart(temperature_data).mark_line().encode(y="Temp", x="Time")
st.altair_chart(linechart, use_container_width=True)

#st.write(temperature_data.plot.line())
#st.line_chart(data=temperature_data, x="Time", y="Temp", width=0, height=0, use_container_width=True)
