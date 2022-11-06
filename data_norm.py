import constants
import DataLoading
import pandas as pd

data = DataLoading.load_temps()
endtime = data.tail()
print(endtime)
def norm_oneweek():
    temp = data.filter(like='2022 Oct ')

def norm_oneday():
    data['mean'] = data.groupby(pd.cut(data['Temp'], range(data.loc[0, "Time"], data.loc[0, "Time"] + constants.ONEDAY)))['Temp'].transform('mean')
    return(data)

def norm_oneweek():
    data['mean'] = data.groupby(pd.cut(data['temp'], range(data.loc[0, "Time"], data.loc[0, "Time"] + constants.ONEWEEK)))['temp'].transform('mean')
    return("one week")


