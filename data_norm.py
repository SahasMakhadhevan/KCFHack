import constants
import DataLoading
import pandas as pd

path = r"E:\Hackathon\KCFHack\Data_set\HackPSU\Fan 1\Temperature.csv"

data = DataLoading.load_temp(path)

def norm_oneweek():
    data.Time = pd.to_datetime(data.Time)
    result = data.resample('W', on="Time").Temp.mean()
    print(result)

def norm_oneday():
    data['mean'] = data.groupby(pd.cut(data['Temp'], range(data.loc[0, "Time"], data.loc[0, "Time"] + constants.ONEDAY)))['Temp'].transform('mean')
    return(data)

def norm_oneweek():
    data['mean'] = data.groupby(pd.cut(data['temp'], range(data.loc[0, "Time"], data.loc[0, "Time"] + constants.ONEWEEK)))['temp'].transform('mean')
    return("one week")


