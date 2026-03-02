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

    def write(self, output1: list[dict]):
      
       st.title("Data Statistics")
       
       row1_col1,row1_col2=st.columns(2)

       #the first output
       with row1_col1:
          fig, ax = plt.subplots()
          ax.bar(output1["Country Code"], output1[str(self.configDict["endYear"])])
          ax.set_xlabel("Countries")
          ax.set_ylabel("GDP")
          ax.set_title(f"GDP of Top {self.configDict["continent"]} Countries")
          plt.xticks(rotation=30)
          st.pyplot(fig)






outputDrivers={"console":ConsoleWriter,"file":GraphicsChartWriter}