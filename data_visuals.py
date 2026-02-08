import matplotlib.pyplot as plt
import streamlit as st

def plotRegionGdp(regionDf, titleSuffix=""):
    
    #makes series of entire columns
    regions = regionDf.iloc[:, 0]  
    gdp = regionDf.iloc[:, 1]       

    #bar graph
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(regions, gdp)
    ax_bar.set_xlabel("Region")
    ax_bar.set_ylabel("GDP")
    ax_bar.set_title(f"GDP by Region {titleSuffix}")
    #so that regions name dont overlap
    plt.xticks(rotation=45)

    st.pyplot(fig_bar)

    #pie chart
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(gdp, labels=regions, autopct="%1.1f%%")
    ax_pie.set_title(f"GDP Distribution by Region {titleSuffix}")

    st.pyplot(fig_pie)