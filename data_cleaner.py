import pandas as pd

def dataCleaner(df):

    #column names in csv files are string 
    yearCols = list(map(str,range(1960,2025)))

    #the gdp values are convereted to int/float and the string or inavlid inputs to NaN
    #updates the yearcols with numeric data
    df[yearCols] = df[yearCols].apply(pd.to_numeric, errors='coerce')

    #selects only the year cols and check if an entire row is NaN then removes it
    df = df.dropna(subset=yearCols, how='all')

    #df.to_csv("cleaned_gdp_data.csv", index=False); to check the data exported 

    return df