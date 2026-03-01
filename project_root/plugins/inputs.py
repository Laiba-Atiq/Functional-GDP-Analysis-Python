import csv as csv
import json as json
from core.contracts import PipelineService

class CsvReader:
    def __init__(self,pipeline:PipelineService, csvFilePath: str):
        self.pipeline = pipeline
        self.csvFilePath = csvFilePath
        self.read()

    def read(self):
        try:
            with open(self.csvFilePath, "r") as file:
                raw_data = csv.DictReader(file)
                data = list(raw_data)
                self.pipeline.execute(data)

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.csvFilePath}' not found.")
        
        except Exception as exp:
            raise Exception(f"Error : {exp} in loading the {self.csvFilePath} file")
        
class JsonReader:
    def __init__(self,pipeline:PipelineService, jsonFilePath:str):
        self.pipeline = pipeline
        self.jsonFilePath = jsonFilePath
        self.read()
        
    def read(self):
        try:
            with open(self.jsonFilePath, "r") as file:
                data = json.load(file)
                self.pipeline.execute(data)  

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.jsonFilePath}' not found.")
        
        except Exception as exp:
            raise Exception(f"Error : {exp} in loading the {self.jsonFilePath} file")
        
inputDrivers = {"json": JsonReader, "csv": CsvReader}
        