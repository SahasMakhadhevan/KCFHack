import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
st.title('CapacityMap Report')
st.write("Type of Run: setP, 20220901_0351PM")
@st.cache
def load_data(nrows):
    data = pd.read_csv(r"DNV_Nodes.csv", nrows=nrows)
    return data

@st.cache
def load_delta(nrows):
    data = pd.read_csv(r"DNV_Nodes.csv",usecols=[6], nrows=nrows)
    data.drop(data[data[' DeltaP'] == 999999].index, inplace = True)
    return data

data_load_state = st.text('Loading data...')
delta_data = load_delta(8)
data_load_state.text('Loading data...done!')

number_of_bins = st.slider("How many bins", 1, 30)
#histogram
fig, ax = plt.subplots()
ax.hist(delta_data[' DeltaP'], bins=number_of_bins)
ax.set_ylabel('Counts')
ax.set_xlabel('DeltaP values')
ax.set_title('Cool Histogram')
st.pyplot(fig)

#Model Image
#image = Image.open(r"C:\SampleApps\CapacityMap_Archives\GUICapacityMapv8.1\bin\Release\Results\ModelImage_20220901_0351PM.jpg")
#st.image(image, caption='Model Image from Synergi Gas')

#Show Nodes.CSV Raw Data
st.subheader('Nodes Information')
if st.checkbox('Show Nodes Information data'):
    st.subheader('Nodes Information data')
    st.write(load_data(8))
