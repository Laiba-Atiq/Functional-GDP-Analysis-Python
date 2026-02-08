import matplotlib.pyplot as plt
import streamlit as st

import pandas as pd

def prepareCountryData(df):
    yearColumns = list(filter(str.isdigit, df.columns))

    longDf = df.melt(id_vars=["Country Name"],value_vars=yearColumns,var_name="Year",value_name="GDP")

    longDf["Year"] = longDf["Year"].astype(int)

    resDf = df[[df.columns[0], df.columns[-1]]].copy()

    return longDf,resDf


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

def plotCountryGdp(wideDf, operation=""):

    #line graph
    fig_line, ax_line = plt.subplots()

    #scattergram
    fig_gram,ax_gram=plt.subplots()

    #easier to plot
    longDf,results = prepareCountryData(wideDf)
    countries = longDf["Country Name"].unique()

    for country in countries:
        countryDf = longDf[longDf["Country Name"] == country]
        ax_line.plot(
            countryDf["Year"],
            countryDf["GDP"],
            linestyle="-",
            label=country)
        
        #scatter plot
        ax_gram.scatter(
            countryDf["Year"],
            countryDf["GDP"],
            label=country
        )

    ax_line.set_xlabel("Year")
    ax_line.set_ylabel("GDP")
    ax_line.set_title("GDP Trend Over Time")
    ax_line.legend()
    ax_line.grid(True)

    st.pyplot(fig_line)

    ax_gram.set_xlabel("Year")
    ax_gram.set_ylabel("GDP")
    ax_gram.set_title("GDP Values Over Time")
    ax_gram.legend()
    ax_gram.grid(True)

    st.pyplot(fig_gram)
