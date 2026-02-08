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

if "page" not in st.session_state:
    st.session_state.page = "init"

if st.session_state.page == "init":
    with st.status("Initializing dashboard...", expanded=True) as status:
        try:
            with st.spinner("Loading GDP data..."): 
                time.sleep(0.5) 
                loadedData = loadGDPfile(filePath) 
            st.write(":white_check_mark: GDP data loaded")

            with st.spinner("Cleaning GDP data..."):
                time.sleep(0.5)
                cleanedData=dataCleaner(loadedData) 
            st.write(":white_check_mark: GDP data cleaned") 
            
            with st.spinner("Reading configuration file..."): 
                time.sleep(0.5) 
                configDictionary = readConfigFile()
            st.write(":white_check_mark: Configuration file read")
            
            with st.spinner("Validating configuration file..."): 
                time.sleep(0.5) 
                configDictionary = validateConfig(configDictionary,cleanedData) 
            st.write(":white_check_mark: Configuration file validated")

            status.update(label="Initialization complete", state="complete")

            #saving data for next page
            st.session_state.cleanedData = cleanedData
            st.session_state.config = configDictionary
            time.sleep(1)
            #switch to statistics page
            st.session_state.page = "stats"
            st.rerun()

        except Exception as exp:
            status.update(label="Initialization failed", state="error")
            st.exception(exp)
            st.stop()

if st.session_state.page == "stats":

    st.title(":bar_chart: GDP Statistics")
