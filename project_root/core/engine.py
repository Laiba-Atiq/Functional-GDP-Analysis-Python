from core.contracts import DataSink
import pandas as pd

class TransformationEngine:
    def __init__(self, configDictionary: dict, sink: DataSink):
        self.configDict = configDictionary
        self.sink = sink

    def execute(self, raw_data: list[dict]):
        # Step 1: Clean the raw data
        cleaned_data = self.data_cleaner(raw_data)

        # Step 2: Filter the data if needed
        filtered_data1 = self.data_filter(cleaned_data)
        filtered_data2 = self.data_filter(cleaned_data)

        # Step 3: Compute statistics
        stats = self.data_statistics(filtered_data1, filtered_data2)

        # Step 4: Send the processed results to the Output module
        #self.sink.write(stats)

    

    def data_statistics(self, filtered_data1, filtered_data2):

        continent = self.configDict["continent"]
        continent_df = filtered_data1.sort_values(by = "2024", ascending = False)

        #Top 10 Countries by GDP for the given continent & year
        top10 = continent_df.head(10)

        #Bottom 10 Countries by GDP for the given continent & year
        bottom10 = continent_df.tail(10)

        #GDP Growth Rate of Each Country in the given continent for the given data range
        startYear = str(self.configDict["startYear"])
        endYear = str(self.configDict["endYear"])

        filtered_data3 = filtered_data2[filtered_data2["Continent"] == continent]
        growthRateSeries = ((filtered_data3[endYear] - filtered_data3[startYear]) / filtered_data3[startYear]) * 100

        growthRate = pd.DataFrame({
            "Country" : filtered_data3["Country Name"],
            "GDP Growth Rate" : growthRateSeries
        })

        #Average GDP by Continent for given date range
        yearCols = list(map(lambda y: str(y), range (int(startYear), int(endYear)+1, +1)))
        filtered_data2["Sum of GDP"] = filtered_data2[yearCols].sum(axis = 1)

        grpByContinent = filtered_data2.groupby("Continent")
        averageGDPSeries = grpByContinent["Sum of GDP"].mean()                

                                                                        #averageGDPSeries is a pandas Series that came from the groupby().mean() operation.Its index is the continent names.Its values are the average GDPs.
        AverageGDP = averageGDPSeries.reset_index()
        AverageGDP.rename(columns={"Sum of GDP": "Average GDP"}, inplace=True)
        
        