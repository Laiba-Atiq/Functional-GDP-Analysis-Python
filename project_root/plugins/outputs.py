import streamlit as st
import matplotlib.pyplot as plt

class ConsoleWriter:
    def __init__(self, configDictionary: dict):
        self.configDict=configDictionary

    def write(self, output1,output2,output3,output4,output5,output6,output7,output8):
        print(f"Top 10 Countries by GDP for the {self.configDict["continent"]} & {self.configDict["endYear"]}")
        print(output1)

        print(f"Bottom 10 Countries by GDP for the {self.configDict["continent"]} & {self.configDict["endYear"]}")
        print(output2)

        print(f"Growth Rate for Countries in {self.configDict["continent"]}")
        print(output3)

        print("Average GDP for Continents")
        print(output4)

        print("Total Global GDP Trend")
        print(output5)

        print("Fastest Growing Continent")
        print(output6)

        print("Countries with Consistent GDP Decline")
        print(output7)

        print("Contribution of Continents to Global GDP")
        print(output8)


class GraphicsChartWriter:
    def __init__(self, configDictionary: dict):
        self.configDict=configDictionary

    def setupOutputPage(self):
        st.title(":chart_with_upwards_trend: GDP STATISTICS")
        
        #sidebar
        st.sidebar.title("CONFIGURATION:")
        
        with st.sidebar.expander("Continent"):
            st.write(self.configDict["continent"])
            
        with st.sidebar.expander("Years"):
            st.write(str(self.configDict["startYear"]) + "-" + str(self.configDict["endYear"]))

        with st.sidebar.expander("Input"):
            st.write(self.configDict["input"])

        with st.sidebar.expander("Output"):
            st.write(self.configDict["output"])
    
    def horizontalbar(self,pos,output: list[dict], statement):
        with pos:
            fig, ax = plt.subplots()
            ax.barh(output["Country Code"], output[str(self.configDict["endYear"])])
            ax.set_xlabel("GDP")
            ax.invert_yaxis()
            ax.set_ylabel("Countries")
            ax.set_title(f"GDP of {statement} 10 {self.configDict["continent"]+"n"} Countries for the year {str(self.configDict["endYear"])}")
            plt.xticks(rotation=30)
            st.pyplot(fig)
    
    def barchart(self,pos,output: list[dict]):
        with pos:
            fig, ax = plt.subplots()
            ax.bar(output["Continent"], output["Average GDP"])
            ax.set_ylabel("GDP")
            ax.set_xlabel("Continents")
            ax.set_title("Average GDP for all Continents")
            plt.xticks(rotation=30)
            st.pyplot(fig)
    
    def lollipopgraph(self,pos,output):
        with pos:
           fig, ax = plt.subplots(figsize=(18,16))
           ax.vlines(x=output["Code"], ymin=0, ymax=output["GDP Growth Rate"], color='skyblue', linewidth=5)
           ax.scatter(output["Code"], output["GDP Growth Rate"], color='blue', zorder=3)
           ax.axhline(0, color='black', linewidth=0.8)  # zero reference
           ax.set_ylabel("Growth Rate")
           ax.set_xlabel("Country")
           ax.set_title("Growth Rate")
           plt.xticks(rotation=90)
           st.pyplot(fig)

    def donutgraph(self,pos,output):
        with pos:
           fig, ax = plt.subplots()
           wedges, _ = ax.pie(
               output['Contribution to Global GDP'], labels=None, startangle=90,wedgeprops=dict(width=0.3)
            )
           centre_circle = plt.Circle((0,0),0.70,fc='white')
           fig.gca().add_artist(centre_circle)
           ax.set_title("Continent's Contribution to GDP",loc="right")
           ax.legend(wedges, output["Continent"], title="Continents", loc="center left", 
              bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9, title_fontsize=10)
           st.pyplot(fig)

    def linegraph(self,pos,output):
        with pos:
            fig, ax = plt.subplots()
            ax.plot(output['Year'], output['Global GDP'], marker='o', linestyle='-', color='red')
            ax.set_xlabel("Year")
            ax.set_ylabel("Global GDP (USD)")
            ax.set_title("Global GDP Over Years")
            st.pyplot(fig)

    def barandline(self,pos,output):
        val1 = str(self.configDict["startYear"])
        val2 = str(self.configDict["endYear"])
        
        with pos:
            fig, ax1 = plt.subplots()

            continent = output["Continent"].iloc[0]
            gdp_start = output[val1].iloc[0]
            gdp_end = output[val2].iloc[0]
            growth = output['GDP Growth Rate'].iloc[0]
            
            x = [0, 1]
            gdp_values = [gdp_start, gdp_end]
            labels = [val1, val2]
            colors = ['skyblue', 'lightgreen']
            
            ax1.bar(x, gdp_values, color=colors, width=0.8)
            ax1.set_xticks(x)
            ax1.set_xticklabels(labels)
            ax1.set_xlabel(continent)
            ax1.set_ylabel("GDP (USD)")
            ax1.set_title("GDP and Growth Rate")
            
            ax2 = ax1.twinx()
            ax2.plot(x, gdp_values, color='red', marker='o', linestyle='--', label=f'Growth Rate: {growth:.2f}%')
            ax2.set_ylabel("Growth Rate")
            ax2.legend(loc='upper left')
            ax2.grid(axis='y', linestyle='--')
            
            st.pyplot(fig)
            
    def slopegraph(self, pos, output):
        val1 = str(self.configDict["startYear"])
        val2 = str(self.configDict["endYear"])
                
        with pos:
            fig, ax = plt.subplots()
            
            x = [0, 1]
            ax.set_xticks(x)
            ax.set_xticklabels([val1, val2])
            ax.set_xlabel("Year")
            ax.set_ylabel("GDP (USD)")
            ax.set_title(f"GDP Decline from {val1} to {val2}")
            
            y = output[[val1, val2]].T
            ax.plot(x, y, marker='o', linestyle='-')  # plots all columns at once
            ax.legend(output['Country Name'].tolist())
            ax.grid(axis='y', linestyle='--')
            st.pyplot(fig)

    def write(self, output1,output2,output3,output4,output5,output6,output7,output8):
       
       self.setupOutputPage()
       
       row1_col1,row1_col2=st.columns(2)
       row2_col1,row2_col2=st.columns(2)
       row3_col1,row3_col2=st.columns(2)
       row4_col1,row4_col2=st.columns(2)

       #the intial outputs
       self.horizontalbar(row1_col1,output1,"Top")
       self.donutgraph(row1_col2,output8)
       
       self.slopegraph(row2_col1,output7)
       self.barchart(row2_col2,output4)

       self.horizontalbar(row3_col1,output2,"Bottom")
       self.barandline(row3_col2,output6)

       self.linegraph(row4_col1,output5)
       self.lollipopgraph(row4_col2,output3)
       
       
       

      
       
     






outputDrivers={"console":ConsoleWriter,"file":GraphicsChartWriter}