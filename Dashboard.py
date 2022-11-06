import streamlit as st
import DataLoading
import altair as alt


def getAggregate(num, span, path, type):
    if span == "Weeks":
        if type == "Temp":
            data = DataLoading.load_temp(path)
        elif type == "Acceleration":
            data = DataLoading.load_Acceleration(path)
        else:
            data = DataLoading.load_velocity(path)
        data = getWeeks(data)
        if num == 9:
            return data.Tail(9)
        return data
    elif span == "Days":
        if type == "Temp":
            data = DataLoading.load_temp(path)
        elif type == "Acceleration":
            data = DataLoading.load_Acceleration(path)
        else:
            data = DataLoading.load_velocity(path)
        data = getDays(data)
        if num == 7:
            return data.Tail(7)
        return data.Tail(30)
    else:
        if type == "Temp":
            data = DataLoading.load_temp(path)
        elif type == "Acceleration":
            data = DataLoading.load_Acceleration(path)
        else:
            data = DataLoading.load_velocity(path)
        data = getHours(data)
        return data.Tail(24)


def switchTime(time, path, type):
    if time == "1 Day":
        return getAggregate(24, "Hours", path, type)
    elif time == "1 Week":
        return getAggregate(7, "Days", path, type)
    elif time == "1 Month":
        return getAggregate(30, "Days", path, type)
    elif time == "2 Months":
        return getAggregate(9, "Weeks", path, type)
    else:
        return getAggregate(-999, "Weeks", path, type)


st.title("Dashboard")

selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
selected_time = st.sidebar.selectbox("Amount of Time", ["1 Day", "1 Week", "1 Month", "2 Months", "All Data"])



data_load_state = st.text('Loading data...')

temperature_data = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv", "Temp")
x_Peak_Acceleration = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/X-Axis/Peak Acceleration.csv", "Acceleration")
x_Peak_Velocity = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/X-Axis/Peak Velocity.csv", "Velocity")
x_RMS_Acceleration = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/X-Axis/RMA Acceleration.csv", "Acceleration")
x_RMS_Velocity = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/X-Axis/RMA Velocity.csv", "Velocity")
y_Peak_Acceleration = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/Peak Acceleration.csv", "Acceleration")
y_Peak_Velocity = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/Peak Velocity.csv", "Velocity")
y_RMS_Acceleration = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/RMA Acceleration.csv", "Acceleration")
y_RMS_Velocity = switchTime(selected_time, r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/RMA Velocity.csv", "Velocity")

data_load_state.text('Loading data...done!')

st.write(temperature_data.describe())

# Line chart for Temps
linechart = alt.Chart(temperature_data).mark_line().encode(y="Temp", x="Time")
st.altair_chart(linechart, use_container_width=True)

linechart = alt.Chart(x_Peak_Acceleration).mark_line().encode(y="Acceleration", x="Time")
st.altair_chart(linechart, use_container_width=True)

linechart = alt.Chart(x_Peak_Velocity).mark_line().encode(y="Velocity", x="Time")
st.altair_chart(linechart, use_container_width=True)

linechart = alt.Chart(x_RMS_Acceleration).mark_line().encode(y="Acceleration", x="Time")
st.altair_chart(linechart, use_container_width=True)

linechart = alt.Chart(x_RMS_Velocity).mark_line().encode(y="Velocity", x="Time")
st.altair_chart(linechart, use_container_width=True)

linechart = alt.Chart(y_Peak_Acceleration).mark_line().encode(y="Acceleration", x="Time")
st.altair_chart(linechart, use_container_width=True)

linechart = alt.Chart(y_Peak_Velocity).mark_line().encode(y="Velocity", x="Time")
st.altair_chart(linechart, use_container_width=True)

linechart = alt.Chart(y_RMS_Acceleration).mark_line().encode(y="Acceleration", x="Time")
st.altair_chart(linechart, use_container_width=True)

linechart = alt.Chart(y_RMS_Velocity).mark_line().encode(y="Velocity", x="Time")
st.altair_chart(linechart, use_container_width=True)
