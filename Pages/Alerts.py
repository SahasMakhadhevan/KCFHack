import streamlit as st
import pandas as pd
import DataLoading

def stats(data):
        mean = data.Value.mean()
        std = data.Value.std()
        return getOutliers(data, mean, std)

def getOutliers(data, mean, std):
        outliers = pd.DataFrame({"Timestamp": [], "Value": []})
        for index, row in data.iterrows():
                if (row[1] > (mean + (2 * std))) or (row[1] < (mean - (2 * std))):
                        outliers.loc[len(outliers.index)] = [row[0], row[1]]

        return outliers

def displayAcceleration(data):
        for index, row in data.iterrows():
                st.write(row[0] + " " + selected_fan + " has hit an outlying Acceleration of " + str(row[1]))


def displayVelocity(data):
        for index, row in data.iterrows():
                st.write(row[0] + " " + selected_fan + " has hit an outlying Velocity of " + str(row[1]))


st.title("Alerts")
selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
#selected_time = st.sidebar.selectbox("Time Units", ["Day", "Week", "Month"])
number = st.sidebar.number_input('Enter the Number of errors to display per section', value=10)

temperature_data = stats(DataLoading.load_temp(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv")).tail(number)
x_Peak_Acceleration = stats(DataLoading.load_Acceleration(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/Peak Acceleration.csv")).tail(number)
x_Peak_Velocity = stats(DataLoading.load_velocity(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/Peak Velocity.csv")).tail(number)
x_RMS_Acceleration = stats(DataLoading.load_Acceleration(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/RMS Acceleration.csv")).tail(number)
x_RMS_Velocity = stats(DataLoading.load_velocity(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/RMS Velocity.csv")).tail(number)
y_Peak_Acceleration = stats(DataLoading.load_Acceleration(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/Peak Acceleration.csv")).tail(number)
y_Peak_Velocity = stats(DataLoading.load_velocity(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/Peak Velocity.csv")).tail(number)
y_RMS_Acceleration = stats(DataLoading.load_Acceleration(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/RMS Acceleration.csv")).tail(number)
y_RMS_Velocity = stats(DataLoading.load_velocity(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/RMS Velocity.csv")).tail(number)

data_load_state = st.text('Loading data...')

for index, row in temperature_data.iterrows():
        st.write(row[0] + " " + selected_fan + " has hit an outlying temperature of " + str(row[1]))

displayAcceleration(x_Peak_Acceleration)
displayVelocity(x_Peak_Velocity)
displayAcceleration(x_RMS_Acceleration)
displayVelocity(x_RMS_Velocity)
displayAcceleration(y_Peak_Acceleration)
displayVelocity(y_Peak_Velocity)
displayAcceleration(y_RMS_Acceleration)
displayVelocity(y_RMS_Velocity)

data_load_state.text('Loading data...done!')


