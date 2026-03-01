from core.contracts import DataSink

class TransformationEngine:
    def __init__(self, configDictionary: dict, sink: DataSink):
        self.configDict = configDictionary
        self.sink = sink

    def execute(self, raw_data: list[dict]):
        # Step 1: Clean the raw data
        cleaned_data = self.data_cleaner(raw_data)

        # Step 2: Filter the data if needed
        filtered_data1 = self.data_filter(cleaned_data)

        # Step 3: Compute statistics
        stats = self.data_statistics(filtered_data1)

        # Step 4: Send the processed results to the Output module
        #self.sink.write(stats)

    

    def data_statistics(self, filtered_data1):

        #Top 10 Countries by GDP for the given continent & year
        continent = self.configDict["continent"]
        continent_df = filtered_data1[ filtered_data1["continent"] == continent]
        top10 = continent_df.head(10)

        #Bottom 10 Countries by GDP for the given continent & year
        bottom10 = continent_df.tail(10)

        #

        
        