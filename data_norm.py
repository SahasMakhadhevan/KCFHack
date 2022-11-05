import constants
import DataLoading
import pandas as pd

data = DataLoading.load_temps()

def norm_oneday():
    data['mean'] = data.groupby(pd.cut(data['Temp'], range(data.loc[0, "Time"], data.loc[0, "Time"] + constants.ONEDAY)))['Temp'].transform('mean')
    print(data)



def norm_oneweek():
    data['mean'] = data.groupby(pd.cut(data['temp'],
                                       range(data.loc[0, "Time"], data.loc[0, "Time"] + constants.ONEWEEK)))['temp'].transform('mean')

    print("one week")



def norm_onemonth():
    print("one month")

