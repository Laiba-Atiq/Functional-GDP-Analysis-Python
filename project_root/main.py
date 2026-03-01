import streamlit as st
import time
from config_reader import readConfigFile
from config_validator import validateConfigFile

filePath="gdp_with_continent_filled.csv"

#setting up dashboard
st.set_page_config(page_title="GDP Analysis",page_icon=":bar_chart:",layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "init"

if st.session_state.page == "init":
    with st.status("Initializing dashboard...", expanded=True) as status:
        try:
            with st.spinner("Reading configuration file..."): 
                time.sleep(0.5) 
                configDictionary = readConfigFile()
            st.write("✅ Configuration file read successfully!")
            
            with st.spinner("Validating configuration file..."): 
                time.sleep(0.5) 
                configDictionary = validateConfigFile(configDictionary) 
            st.write("✅ Configuration file validated successfully!")

            status.update(label="Initialization complete", state="complete")

        except Exception as exp:
            status.update(label="Initialization failed", state="error")
            st.exception(exp)
            st.stop()
