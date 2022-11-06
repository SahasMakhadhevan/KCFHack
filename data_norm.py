import constants
import DataLoading
import pandas as pd


def norm_oneweek(data):
    data.Time = pd.to_datetime(data.Time)
    data.Temp = pd.to_numeric(data.Temp)
    result = data.resample('W-FRI', on="Time").Temp.describe()
    return result


def norm_oneday(data):
    data.Time = pd.to_datetime(data.Time)
    data.Temp = pd.to_numeric(data.Temp)
    result = data.resample('D', on="Time").Temp.mean()
    return result


def norm_onehour(data):
    data.Time = pd.to_datetime(data.Time)
    data.Temp = pd.to_numeric(data.Temp)
    result = data.resample('60T', on="Time").Temp.mean()
    return result
