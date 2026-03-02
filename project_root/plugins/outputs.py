import streamlit as st
import matplotlib.pyplot as plt

class ConsoleWriter:
    def __init__(self, configDictionary: dict):
        self.configDict=configDictionary

    def write(self, output1: list[dict]):
        print(f"Top 10 Countries by GDP for the {self.configDict["continent"]} & {self.configDict["endYear"]}")
        print(output1)

class GraphicsChartWriter:
    def __init__(self, configDictionary: dict):
        self.configDict=configDictionary

    def setupOutputPage(self):
        st.title(":chart_with_upwards_trend: GDP STATISTICS")
        
        #sidebar
        st.sidebar.title(":wrench:CONFIGURATION:")
        
        with st.sidebar.expander("Continent"):
            st.write(self.configDict["continent"])
            
        with st.sidebar.expander("Years"):
            st.write(str(self.configDict["startYear"]) + "-" + str(self.configDict["endYear"]))

        with st.sidebar.expander("Input"):
            st.write(self.configDict["input"])

        with st.sidebar.expander("Output"):
            st.write(self.configDict["output"])
    
    def barchart(self,pos,output: list[dict], statement):
        with pos:
            fig, ax = plt.subplots()
            ax.bar(output["Country Code"], output[str(self.configDict["endYear"])])
            ax.set_xlabel("Countries")
            ax.set_ylabel("GDP")
            ax.set_title(f"GDP of {statement} {self.configDict["continent"] + "n"} Countries")
            plt.xticks(rotation=30)
            st.pyplot(fig)

    def write(self, output1: list[dict]):
       
       self.setupOutputPage()
       
       row1_col1,row1_col2=st.columns(2)

       #the intial outputs
       self.barchart(row1_col1,output1,"Top")
       self.barchart(row1_col2,output1,"Bottom")
     






outputDrivers={"console":ConsoleWriter,"file":GraphicsChartWriter}