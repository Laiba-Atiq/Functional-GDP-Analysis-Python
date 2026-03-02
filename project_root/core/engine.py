from core.contracts import DataSink
import pandas as pd

class TransformationEngine:
    def __init__(self, configDictionary: dict, sink: DataSink):
        self.configDict = configDictionary
        self.sink = sink

    def dataCleaner(self, rawData):
        #converting the data into a data frame
        df = pd.DataFrame(rawData)
    
        before=len(df)

        yearCols=list(filter(str.isdigit,df.columns))
        otherCols=list(filter(lambda col: col not in yearCols, df.columns))
        
        df[yearCols] = df[yearCols].apply(pd.to_numeric, errors='coerce').astype(float)
        df = df.dropna(subset=yearCols, how='all')

        df[otherCols]=df[otherCols].apply(lambda col: col.str.strip())

        mask = ((df[otherCols].notna()) & (df[otherCols] != ""))
        
        #only return rows with all true rows
        df=df[mask.all(axis=1)]

        after=len(df)

        #print(f"Removed number of rows {before-after}")

        return df
    
    def dataFilter(self, df):
        yearCols=list(filter(str.isdigit,df.columns))
        
        rangeYears=list(map(str,range(self.configDict["startYear"],(self.configDict["endYear"]+1))))
        if not all (map(lambda r: r in yearCols, rangeYears)):
            raise ValueError("The years specified in configuration file are not in data")
        
        #checks all columns
        dfFirst = df[["Country Name"] + rangeYears + ["Continent"] + ["Country Code"]]

        #boolean series checks rows
        df = df[df["Continent"] == (self.configDict["continent"])]
        if df.empty:
            raise ValueError("The continent in configuration file is not in data")
        
        dfSec = df[["Country Name",str(self.configDict["endYear"]),"Continent","Country Code"]]
        
        return dfSec,dfFirst