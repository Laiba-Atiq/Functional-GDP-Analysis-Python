import pandas as pd
import streamlit as st

def dataCleaner(df):

    #original data 
    before = len(df)

    #checks if country is valid; df=df[mask]
    df["Country Name"]=df["Country Name"].str.strip()
    df = df[ (df["Country Name"]!= "") & df["Country Name"].notna() & df["Country Name"].apply(lambda x: isinstance(x, str)) ]
    
    st.write("Country Name invalid for", before-len(df), "rows")
    before=len(df)

    #checks if region is valid; df=df[mask]
    df["Continent"]=df["Continent"].str.strip()
    validContinents = {"Africa","Asia","Europe","North America","South America","Oceania","Antarctica", "Global"}
    df = df[df["Continent"].notna() & df["Continent"].isin(validContinents)]

    st.write("Continent invalid for", before-len(df), "rows")
    before=len(df)

    #checks
    df = df[ df["Country Code"].apply(lambda x: isinstance(x, str)) & 
            df["Indicator Name"].apply(lambda x: isinstance(x, str)) &
            df["Indicator Code"].apply(lambda x: isinstance(x, str))]
    
    st.write("Country Code/Indicator Name/Indicator Code invalid for", before-len(df), "rows")
    before=len(df)

    #column names in csv files are string 
    yearCols = list(map(str,range(1960,2025)))

    #the gdp values are convereted to int/float and the string or inavlid inputs to NaN
    #updates the yearcols with numeric data
    df[yearCols] = df[yearCols].apply(pd.to_numeric, errors='coerce').astype(float)

    #selects only the year cols and check if an entire row is NaN then removes it
    df = df.dropna(subset=yearCols, how='all')

    st.write("All GDP years empty for", before-len(df), "rows")
    before=len(df)

    #df.to_csv("cleaned_gdp_data.csv", index=False) #; to check the data exported 

    return df