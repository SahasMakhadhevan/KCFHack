import streamlit as st
import DataLoading
import data_norm

st.title("Home")

selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
selected_time = st.sidebar.selectbox("Time Units", ["Day", "Week", "Month"])

st.markdown(selected_fan)
st.markdown(selected_time)

data_load_state = st.text('Loading data...')
temp_data = DataLoading.load_temps()
data_load_state.text('Loading data...done!')

# Line chart for Temps
st.line_chart(data=temp_data, x="Time", y="Temp", width=0, height=0, use_container_width=True)
