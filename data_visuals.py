import matplotlib.pyplot as plt
import streamlit as st

import pandas as pd

def barChart(regionDf, titleSuffix=""):
    #makes series of entire columns
    regions = regionDf.iloc[:, 0]  
    gdp = regionDf.iloc[:, 1]       

    #bar graph
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(regions, gdp)
    ax_bar.set_xlabel("Region", color="darkgreen")
    ax_bar.set_ylabel("GDP", color="darkgreen")
    ax_bar.set_title(f"Region-Wise GDP {titleSuffix}", color="#8B0000")
    #so that regions name dont overlap
    plt.xticks(rotation=45)

    st.pyplot(fig_bar)

    
def pieChart(regionDf, titleSuffix=""):
    
    #makes series of entire columns
    regions = regionDf.iloc[:, 0]  
    gdp = regionDf.iloc[:, 1]       

    #pie chart
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(gdp, labels=regions, autopct="%1.1f%%")
    ax_pie.set_title(f"Region-Wise GDP {titleSuffix}", color="#8B0000")

    st.pyplot(fig_pie)


def prepareCountryData(df):
    yearColumns = list(filter(str.isdigit, df.columns))
    longDf = df.melt(
        id_vars=["Country Name"],
        value_vars=yearColumns,
        var_name="Year",
        value_name="GDP"
    )
    longDf["Year"] = longDf["Year"].astype(int)
    resDf = df[[df.columns[0], df.columns[-1]]].copy()
    return longDf, resDf

def lineChart(wideDf, titleSuffix="", column=None):
    longDf, _ = prepareCountryData(wideDf)
    countries = longDf["Country Name"].unique()

    fig, ax = plt.subplots(figsize=(10, 6))

    list(map(
        lambda country: ax.plot(
            longDf[longDf["Country Name"] == country]["Year"],
            longDf[longDf["Country Name"] == country]["GDP"],
            linestyle="-",
            label=country
        ),
        countries
    ))

    ax.set_xlabel("Year", color="darkgreen")
    ax.set_ylabel("GDP", color="darkgreen")
    ax.set_title(f"Year-Wise GDP {titleSuffix}", color="#8B0000")
    ax.legend()
    ax.grid(True)

    if column:
        column.pyplot(fig)
    else:
        st.pyplot(fig)

def scatterChart(wideDf, titleSuffix="", column=None):
    longDf, _ = prepareCountryData(wideDf)
    countries = longDf["Country Name"].unique()

    fig, ax = plt.subplots(figsize=(10, 6))

    list(map(
        lambda country: ax.scatter(
            longDf[longDf["Country Name"] == country]["Year"],
            longDf[longDf["Country Name"] == country]["GDP"],
            label=country
        ),
        countries
    ))

    ax.set_xlabel("Year", color="darkgreen")
    ax.set_ylabel("GDP", color="darkgreen")
    ax.set_title(f"Year-Wise GDP {titleSuffix}", color="#8B0000")
    ax.legend()
    ax.grid(True)

    if column:
        column.pyplot(fig)
    else:
        st.pyplot(fig)
