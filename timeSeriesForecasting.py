import DataLoading
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
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


#
# stepwise_fit = auto_arima(Data['avgTemp'], trace=True, suppress_warnings=True)
# stepwise_fit.summary()
# ad_test(Data)

# Create Training and Test
train = Data.Temp[:85]
test = Data.Temp[85:]

# Build Model
# model = ARIMA(train, order=(3,2,1))
model = ARIMA(train, order=(1, 1, 1))
fitted = model.fit(disp=-1)

# Forecast
fc, se, conf = fitted.forecast(15, alpha=0.05)  # 95% conf

# Make as pandas series
fc_series = pd.Series(fc, index=test.index)
lower_series = pd.Series(conf[:, 0], index=test.index)
upper_series = pd.Series(conf[:, 1], index=test.index)
