import pandas as pd

def dataCleaner(df):
    #checks if country is valid; df=df[mask]
    df["Country Name"]=df["Country Name"].str.strip()
    df = df[ (df["Country"]!= "") & df["Country"].notna() & df["Country"].apply(lambda x: isinstance(x, str)) ]

    #checks if region is valid; df=df[mask]
    df["Continent"]=df["Continent"].str.strip()
    validContinents = {"Africa","Asia","Europe","North America","South America","Oceania","Antarctica", "Global"}
    df = df[df["Continent"].notna() & df["Continent"].isin(validContinents)]

    #column names in csv files are string 
    yearCols = list(map(str,range(1960,2025)))

    #the gdp values are convereted to int/float and the string or inavlid inputs to NaN
    #updates the yearcols with numeric data
    df[yearCols] = df[yearCols].apply(pd.to_numeric, errors='coerce')

    #selects only the year cols and check if an entire row is NaN then removes it
    df = df.dropna(subset=yearCols, how='all')

    #df.to_csv("cleaned_gdp_data.csv", index=False); to check the data exported 

    return df