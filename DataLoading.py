import pandas as pd
import time

def convertTime(tmpTime):
    foo = time.gmtime(tmpTime)
    bar = time.strftime("%Y %b %d %H:%M:%S", foo)
    return bar

def load_temp(path):
    data = pd.read_csv(path, header=None)
    data.columns = ["Time", "Temp"]

    #Replaces epoch time in col 0 with formatted string dateTime
    for index, row in data.iterrows():
        data.loc[index, "Time"] = convertTime(int(str(row["Time"])[:-5]))

    return data


def load_Acceleration(path):
    data = pd.read_csv(path, header=None)
    data.columns = ["Time", "Acceleration"]

    #Replaces epoch time in col 0 with formatted string dateTime
    for index, row in data.iterrows():
        data.loc[index, "Time"] = convertTime(int(str(row["Time"])[:-5]))

    return data

def load_velocity(path):
    data = pd.read_csv(path, header=None)
    data.columns = ["Time", "Velocity"]

    #Replaces epoch time in col 0 with formatted string dateTime
    for index, row in data.iterrows():
        data.loc[index, "Time"] = convertTime(int(str(row["Time"])[:-5]))

    return data
