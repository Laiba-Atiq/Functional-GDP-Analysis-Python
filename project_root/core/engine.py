import pandas as pd

class TransformationEngine:
    def __init__(self):
        ...

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

        print(f"Removed number of rows {before-after}")

        return df

    def execute(self, rawData: list[dict]):
        #clean the raw data
        cleanedData = self.dataCleaner(rawData)
       
        # Step 2: Filter the data if needed
        #filtered_data = data_filter(cleaned_data)

        # Step 3: Compute statistics
        #stats = data_statistics(filtered_data)

        # Step 4: Send the processed results to the Output module
        #self.sink.writereturn newDat(stats)
