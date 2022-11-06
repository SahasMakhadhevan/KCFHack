import constants
import DataLoading
import pandas as pd

path = r"E:\Hackathon\KCFHack\Data_set\HackPSU\Fan 1\Temperature.csv"

data = DataLoading.load_temp(path)

def norm_oneweek():
    data.Time = pd.to_datetime(data.Time)
    data.Temp = pd.to_float(data.Temp)
    result = data.resample('W-FRI', on="Time").Temp.describe()
    end = result.head(10)
    return end

def norm_oneday():
    data['mean'] = data.groupby(pd.cut(data['Temp'], range(data.loc[0, "Time"], data.loc[0, "Time"] + constants.ONEDAY)))['Temp'].transform('mean')
    return(data)

def norm_oneweek():
    data['mean'] = data.groupby(pd.cut(data['temp'], range(data.loc[0, "Time"], data.loc[0, "Time"] + constants.ONEWEEK)))['temp'].transform('mean')
    return("one week")


