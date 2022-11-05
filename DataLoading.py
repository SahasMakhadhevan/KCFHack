import pandas as pd

def load_temps():
    data = pd.read_csv(r"Data_set/HackPSU/Fan 1/Temperature.csv", header=None)
    data.columns = ["Time", "Temp"]
    return data
