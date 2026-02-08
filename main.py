import streamlit as st
import time
from data_loader import loadGDPfile
from config_reader import readConfigFile
from data_cleaner import dataCleaner
from config_validator import validateConfig
from data_filter import filterByRegion,filterByCountry
from data_statistics import avgGdp,sumGdp
from data_visuals import barChart,pieChart,lineChart,scatterChart 

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
            st.write("✅ GDP data loaded successfully!")

            with st.spinner("Cleaning GDP data..."):
                time.sleep(0.5)
                cleanedData=dataCleaner(loadedData) 
            st.write("✅ GDP data cleaned successfully!") 
            
            with st.spinner("Reading configuration file..."): 
                time.sleep(0.5) 
                configDictionary = readConfigFile()
            st.write("✅ Configuration file read successfully!")
            
            with st.spinner("Validating configuration file..."): 
                time.sleep(0.5) 
                configDictionary = validateConfig(configDictionary,cleanedData) 
            st.write("✅ Configuration file validated successfully!")

            status.update(label="Initialization complete", state="complete")

            #saving data for next page
            st.session_state.cleanedData = cleanedData
            st.session_state.config = configDictionary
            time.sleep(0.5)
            #switch to statistics page
            st.session_state.page = "stats"
            st.rerun()

        except Exception as exp:
            status.update(label="Initialization failed", state="error")
            st.exception(exp)
            st.stop()

if st.session_state.page == "stats":

    config = st.session_state.config
    data = st.session_state.cleanedData

    st.title(":chart_with_upwards_trend: GDP STATISTICS")

    #sidebar
    st.sidebar.title("CONFIGURATION:")

    with st.sidebar.expander("Regions"):
        st.write(", ".join(config["region"]))

    with st.sidebar.expander("Years"):
        st.write(", ".join(map(str, config["year"])))

    with st.sidebar.expander("Countries"):
        st.write(", ".join(config["country"]))

    with st.sidebar.expander("Operation"):
        st.write(config["operation"])



    regionFiltered = filterByRegion(config, data)
    countryFiltered = filterByCountry(config, data)

    if config["operation"] == "average":
        countryComputedData, regionComputedData = avgGdp(countryFiltered, regionFiltered)
        op_label = "(Average)"
    else:
        countryComputedData, regionComputedData = sumGdp(countryFiltered, regionFiltered)
        op_label = "(Sum)"

    # LAYOUT: 2x2 GRID 
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    with row1_col1:
        st.subheader("Bar Chart")
        barChart(regionComputedData, op_label)

    with row1_col2:
        st.subheader("Pie Chart")
        pieChart(regionComputedData, op_label)

    with row2_col1:
        st.subheader("Line Chart")
        lineChart(countryComputedData, op_label)

    with row2_col2:
        st.subheader("Scattergram")
        scatterChart(countryComputedData, op_label)


    st.markdown("---")
    st.subheader("Statistics Summary:")

    st.write("### Region-wise GDP")
    st.dataframe(regionComputedData)  
    
    st.write("### Country-wise GDP")
    st.dataframe(countryComputedData) 

     