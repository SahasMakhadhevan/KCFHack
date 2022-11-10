import constants
import DataLoading
import streamlit as st
import pandas as pd


def norm_oneweek(data):
    data.Time = pd.to_datetime(data.Time)
    result = data.resample('W-FRI', on="Time").Value.mean().to_frame().reset_index()
    return result


def norm_oneday(data):
    data.Time = pd.to_datetime(data.Time)
    result = data.resample('D', on="Time").Value.mean().to_frame().reset_index()
    return result


def norm_onehour(data):
    data.Time = pd.to_datetime(data.Time)
    result = data.resample('H', on="Time").Value.mean().to_frame().reset_index()
    return result
