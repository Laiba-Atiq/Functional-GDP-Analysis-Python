import streamlit as st
import matplotlib.pyplot as plt
import time
from data_loader import loadGDPfile
from config_reader import readConfigFile
from data_cleaner import dataCleaner
from config_validator import validateConfig

filePath="gdp_with_continent_filled.csv"

#setting up dashboard
st.set_page_config(page_title="GDP Analysis",page_icon=":bar_chart:",layout="wide")

with st.status("Initializing dashboard...", expanded=True) as status:
    try:
        loadedData = loadGDPfile(filePath)
        st.write("✅ GDP data loaded")

        cleanedData=dataCleaner(loadedData)
        st.write("✅ GDP data cleaned")

        configDictionary = readConfigFile()
        st.write("✅ Configuration file loaded")

        configDictionary = validateConfig(configDictionary,cleanedData)
        st.write("✅ Configuration file validated")

        status.update(label="Initialization complete", state="complete")

    except Exception as exp:
        status.update(label="Initialization failed", state="error")
        st.exception(exp)
        st.stop()
