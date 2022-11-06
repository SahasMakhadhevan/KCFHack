import streamlit as st
import pandas as pd
import DataLoading

def stats(data):
        # TODO
        statistics = data.describe()
        mean = statistics[0][0]
        std = statistics[0][1]
        return getOutliers(data, mean, std)

def getOutliers(data, mean, std):
        outliers = pd.DataFrame()
        outliers.columns = ["Timestamp", "Value"]
        for index, row in data.iterrows():
                if row[1] > (mean + (2 * std)) or row[1] < (mean - (2 * std)):
                        outliers.append(row)

        return outliers

def displayAcceleration(data):
        for index, row in data:
                st.write(row[0] + " " + selected_fan + " has hit an outlying Acceleration of " + row[1])


def displayVelocity(data):
        for index, row in data:
                st.write(row[0] + " " + selected_fan + " has hit an outlying Velocity of " + row[1])


st.title("Alerts")

selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
selected_time = st.sidebar.selectbox("Time Units", ["Day", "Week", "Month"])

# Format of Data Frame:
# TimeStamp - Fan Number - Alert Text

temperature_data = stats(DataLoading.load_temp(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv"))
x_Peak_Acceleration = stats(DataLoading.load_Acceleration(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/Peak Acceleration.csv"))
x_Peak_Velocity = stats(DataLoading.load_velocity(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/Peak Velocity.csv"))
x_RMS_Acceleration = stats(DataLoading.load_Acceleration(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/RMS Acceleration.csv"))
x_RMS_Velocity = stats(DataLoading.load_velocity(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/RMS Velocity.csv"))
y_Peak_Acceleration = stats(DataLoading.load_Acceleration(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/Peak Acceleration.csv"))
y_Peak_Velocity = stats(DataLoading.load_velocity(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/Peak Velocity.csv"))
y_RMS_Acceleration = stats(DataLoading.load_Acceleration(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/RMS Acceleration.csv"))
y_RMS_Velocity = stats(DataLoading.load_velocity(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/RMS Velocity.csv"))

for index, row in temperature_data:
        st.write(row[0] + " " + selected_fan + " has hit an outlying temperature of " + row[1])

displayAcceleration(x_Peak_Acceleration)
displayVelocity(x_Peak_Velocity)
displayAcceleration(x_RMS_Acceleration)
displayVelocity(x_RMS_Velocity)
displayAcceleration(y_Peak_Acceleration)
displayVelocity(y_Peak_Velocity)
displayAcceleration(y_RMS_Acceleration)
displayVelocity(y_RMS_Velocity)



