import streamlit as st
import pandas as pd
import time

def convertTime(tmpTime):
    foo = time.gmtime(tmpTime)
    bar = time.strftime("%a, %d %b %Y %H:%M:%S", foo)
    return bar

def load_temps(selected_fan):
    data = pd.read_csv(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv", header=None, nrows=50)
    data.columns = ["Time", "Temp"]

    #Replaces epoch time in col 0 with formatted string dateTime
    for index, row in data.iterrows():
        data.loc[index, "Time"] = convertTime(int(str(row["Time"])[:-5]))

    return data


def load_X_Accelleration(selected_fan):
    data = pd.read_csv(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv", header=None)
    data.columns = ["Time", "Temp"]
    return data

def load_Y_Accelleration(selected_fan):
    data = pd.read_csv(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv", header=None)
    data.columns = ["Time", "Temp"]
    return data
def load_X_Velocity(selected_fan):
    data = pd.read_csv(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv", header=None)
    data.columns = ["Time", "Temp"]
    return data

def load_Y_Velocity(selected_fan):
    data = pd.read_csv(r"Data_set/HackPSU/" + selected_fan + "/Temperature.csv", header=None)
    data.columns = ["Time", "Temp"]

    #Replaces epoch time in col 0 with formatted string dateTime
    for index, row in data.iterrows():
        data.loc[index, "Time"] = convertTime(int(str(row["Time"])[:-5]))

    return data