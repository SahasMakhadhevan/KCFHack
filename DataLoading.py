import pandas as pd

def load_temps(path):
    data = pd.read_csv(path, header=None)
    data.columns = ["Time", "Temp"]
    return data