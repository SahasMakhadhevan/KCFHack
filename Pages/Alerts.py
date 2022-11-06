import streamlit as st
import pandas as pd

st.title("Alerts")

selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
selected_time = st.sidebar.selectbox("Time Units", ["Day", "Week", "Month"])

# Format of Data Frame:
# TimeStamp - Fan Number - Alert Text
data = {'Timestamp': ['Tom', 'nick', 'krish', 'jack'],
        'Fan Number': [20, 21, 19, 18],
        "Alert Text": ["asdf", "asdfasdf", "qwer", "qwerqwer"]}
alerts = pd.DataFrame(data)  # This needs to be populated from Data Loading

st.write(alerts)
