import DataLoading
#import statsmodels.api as smapi
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf
import pandas as pd
from pmdarima import auto_arima
import warnings

warnings.filterwarnings("ignore")


def load_temps():
    data = pd.read_csv(r"/Users/sarthakgiri/Documents/GitHub/KCFHack/Data_set/HackPSU/Fan 1/Temperature.csv",
                       header=None)
    data.columns = ["Time", "Temp"]
    return data


Data = load_temps()


def ad_test(data):
    result = adfuller(data['Temp'], autolag='AIC')
    print("1. ADF : ", result[0])
    print("2. P-Value : ", result[1])
    print("3. Num Of Lags : ", result[2])
    print("4. Nm Of Observations Used For ADF Regression and Critical Values Calculation:", result[3])
    print("5. Critical Values :")
    for key, val in result[4].items():
        print("\t", key, ": ", val)


ad_test(Data)

