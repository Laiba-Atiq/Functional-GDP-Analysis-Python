import pandas as pd

class TransformationEngine:
    def __init__(self):
        ...

    def dataCleaner(self, rawData):
            newData=pd.DataFrame(rawData)

            return newData

    def execute(self, rawData: list[dict]):
        #clean the raw data
        cleanedData = self.dataCleaner(rawData)
        print(cleanedData)

        # Step 2: Filter the data if needed
        #filtered_data = data_filter(cleaned_data)

        # Step 3: Compute statistics
        #stats = data_statistics(filtered_data)

        # Step 4: Send the processed results to the Output module
        #self.sink.write(stats)
