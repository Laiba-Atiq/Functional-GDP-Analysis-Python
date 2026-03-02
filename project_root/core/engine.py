from core.contracts import DataSink
import pandas as pd

class TransformationEngine:
    def __init__(self, configDictionary: dict, sink: DataSink):
        self.configDict = configDictionary
        self.sink = sink

    def execute(self, rawData: list[dict]):
        # Step 1: Clean the raw data
        cleanedData = self.dataCleaner(rawData)

        # Step 2: Filter the data if needed
        filtered_data1, filtered_data2 = self.dataFilter(cleanedData)

        # Step 3: Compute statistics
        stats = self.data_statistics(filtered_data1, filtered_data2)

        # Step 4: Send the processed results to the Output module
        #self.sink.write(stats)

    

    def dataStatistics(self, filtered_data1, filtered_data2):
        startYear = str(self.configDict["startYear"])
        endYear = str(self.configDict["endYear"])

        continent = self.configDict["continent"]
        continentDf = filtered_data1.sort_values(by = endYear, ascending = False)

        #1. Top 10 Countries by GDP for the given continent & year
        top10 = continentDf.head(10)

        #2. Bottom 10 Countries by GDP for the given continent & year
        bottom10 = continentDf.tail(10)

        #3. GDP Growth Rate of Each Country in the given continent for the given data range
        filtered_data3 = filtered_data2[filtered_data2["Continent"] == continent]
        growthRateSeries = ((filtered_data3[endYear] - filtered_data3[startYear]) / filtered_data3[startYear]) * 100

        growthRate = pd.DataFrame({
            "Country" : filtered_data3["Country Name"],
            "Code":filtered_data3["Country Code"],
            "GDP Growth Rate" : growthRateSeries
        })

        #4. Average GDP by Continent for given date range
        yearCols = list(map(lambda y: str(y), range (int(startYear), int(endYear)+1, +1)))
        filtered_data2["Sum of GDP"] = filtered_data2[yearCols].sum(axis = 1)

        averageGDPSeries = filtered_data2.groupby("Continent")["Sum of GDP"].mean()                
                                                                        #averageGDPSeries is a pandas Series that came from the groupby().mean() operation.Its index is the continent names.Its values are the average GDPs.
        AverageGDP = averageGDPSeries.reset_index()
        AverageGDP.rename(columns={"Sum of GDP": "Average GDP"}, inplace=True)
        
        #5. Total Global GDP Trend for given date range
        globalGDPTrend = filtered_data2[yearCols].sum()
        globalGDPTrendDF = globalGDPTrend.reset_index()   #converts back to dataframe
        globalGDPTrendDF.columns = ["Year", "Global GDP"]

        #6. Fastest Growing Continent for the given date range 
        growthRateOfContinents = filtered_data2.groupby("Continent")[[startYear, endYear]].sum()
        growthRateOfContinents["GDP Growth Rate(Continent Wise)"] = (growthRateOfContinents[endYear] - growthRateOfContinents[startYear])/ growthRateOfContinents[startYear] * 100

        GDPgrowthRateOfContinents = growthRateOfContinents[["GDP Growth Rate(Continent Wise)"]].reset_index()    
        FastestGrowing = GDPgrowthRateOfContinents.loc[       #use .loc to select a row by index:
            GDPgrowthRateOfContinents["GDP Growth Rate(Continent Wise)"].idxmax()
        ]    

        temp = filtered_data2.groupby("Continent")[yearCols].sum()
        temp = temp.reset_index()
        temp = (temp[temp["Continent"] == FastestGrowing["Continent"]])
        temp["GDP Growth Rate"] = FastestGrowing["GDP Growth Rate(Continent Wise)"]

        #7. Countries with Consistent GDP Decline in Last x Years 
        diffYears = filtered_data2[yearCols].diff(axis = 1)
        maskYears = diffYears.iloc[:, 1:].lt(0).all(axis=1)   #lt(0)->less than 0
        decline = filtered_data2[maskYears]
        decliningCountries = decline[["Country Name"] + yearCols]   #make line/scatter plot

        #8. Contribution of Each Continent to Global GDP for given data range
        globalGDPPerContinent = filtered_data2.groupby("Continent")["Sum of GDP"].sum()
        globalGDPPerContinent = globalGDPPerContinent.reset_index()
        globalGDPPerContinent.rename(columns={"Sum of GDP": "Contribution to Global GDP"}, inplace=True)

        return top10, bottom10, growthRate, AverageGDP, globalGDPTrendDF, temp, decliningCountries, globalGDPPerContinent