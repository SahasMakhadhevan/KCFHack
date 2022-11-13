import streamlit as st
import DataLoading


def stats(data):
    # Because the data is not normalized, we cannot use the mean and standard deviation to find outliers (Z-Score)
    # Instead, we will use the median and the interquartile range (IQR)

    # calculating outliers using IQR
    q1 = float(data.quantile(0.25))
    q3 = float(data.quantile(0.75))
    iqr = float(q3 - q1)
    return data[(data.Value > (q3 + (1.5 * iqr))) | (data.Value < (q1 - (1.5 * iqr)))].dropna().reset_index(drop=True)

    # Calculating outliers using Z-score
    # mean = data.Value.mean()
    # std = data.Value.std()
    # return data[(data.Value > (mean + (2 * std))) | (data.Value < (mean - (2 * std)))].dropna().reset_index(drop=True)


# TODO: Don't use iterrrows, it's slow.
def display_acceleration(data):
    for acc_index, acc_row in data.iterrows():
        st.write(str(acc_row[0]) + " " + selected_fan + " has hit an outlying Acceleration of " + str(acc_row[1]))


# TODO: Don't use iterrrows, it's slow.
def display_velocity(data):
    for vel_index, vel_row in data.iterrows():
        st.write(str(vel_row[0]) + " " + selected_fan + " has hit an outlying Velocity of " + str(vel_row[1]))


st.title("Alerts")
selected_fan = st.sidebar.selectbox("Fan Selector", ["Fan 1", "Fan 2", "Fan 3", "Fan 4", "Fan 5", "Fan 6", "Fan 7"])
number = st.sidebar.number_input('Enter the Number of errors to display per section', value=10)

data_load_state = st.text('Loading data...')

temperature_data = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv")).tail(number).reset_index(drop=True)
x_Peak_Acceleration = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/Peak Acceleration.csv")).tail(number).reset_index(drop=True)
x_Peak_Velocity = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/Peak Velocity.csv")).tail(number).reset_index(drop=True)
x_RMS_Acceleration = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/RMS Acceleration.csv")).tail(number).reset_index(drop=True)
x_RMS_Velocity = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/X-Axis/RMS Velocity.csv")).tail(number).reset_index(drop=True)
y_Peak_Acceleration = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/Peak Acceleration.csv")).tail(number).reset_index(drop=True)
y_Peak_Velocity = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/Peak Velocity.csv")).tail(number).reset_index(drop=True)
y_RMS_Acceleration = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/RMS Acceleration.csv")).tail(number).reset_index(drop=True)
y_RMS_Velocity = stats(DataLoading.load_alerts_data(r"Data_set/HackPSU/" + selected_fan + "/Y-Axis/RMS Velocity.csv")).tail(number).reset_index(drop=True)

data_load_state.text('Loading data...done!')


st.subheader("Temperature")
# TODO: Don't use iterrrows, it's slow.
for index, row in temperature_data.iterrows():
    st.write(str(row[0]) + " " + selected_fan + " has hit an outlying Temperature of " + str(row[1]))

col1, col2 = st.columns(2)

with col1:
    st.subheader("X-Axis Peak Acceleration")
    display_acceleration(x_Peak_Acceleration)

    st.subheader("X-Axis Peak Velocity")
    display_velocity(x_Peak_Velocity)

    st.subheader("X-Axis RMS Acceleration")
    display_acceleration(x_RMS_Acceleration)

    st.subheader("X-Axis RMS Velocity")
    display_velocity(x_RMS_Velocity)

with col2:
    st.subheader("Y-Axis Peak Acceleration")
    display_acceleration(y_Peak_Acceleration)

    st.subheader("Y-Axis Peak Velocity")
    display_velocity(y_Peak_Velocity)

    st.subheader("Y-Axis RMS Acceleration")
    display_acceleration(y_RMS_Acceleration)

    st.subheader("Y-Axis RMS Velocity")
    display_velocity(y_RMS_Velocity)
