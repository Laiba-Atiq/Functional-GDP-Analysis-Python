import streamlit as st
import matplotlib.pyplot as plt
import time
from data_loader import loadGDPfile

filePath="gdp_with_continent_filled.csv"

#setting up dashboard
st.set_page_config(page_title="GDP Analysis",page_icon=":bar_chart:",layout="wide")

#loading gdp data in data frame
try:
    with st.spinner("Loading data..."):
        time.sleep(1)
        loadedData=loadGDPfile(filePath)
        st.success("Data loaded successfully")
except Exception as exp:
    st.error("Data loading failed")
    st.exception(exp)
    st.stop()