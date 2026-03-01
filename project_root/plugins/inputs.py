import csv as csv
import json as json
from core.contracts import PipelineService

class CsvReader:
    def __init__(self, csvFilePath: str, pipeline:PipelineService):
        self.pipeline = pipeline
        self.csvFilePath = csvFilePath

    def read(self):
        try:
            with open(self.csvFilePath, "r") as file:
                rawData = csv.DictReader(file)
                data = list(rawData)
                self.pipeline.execute(data)

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.csvFilePath}' not found.")
        
        except Exception as exp:
            raise Exception(f"Error : {exp} in loading the {self.csvFilePath} file")
        
class JsonReader:
    def __init__(self, jsonFilePath:str, pipeline:PipelineService):
        self.pipeline = pipeline
        self.jsonFilePath = jsonFilePath
        
    def read(self):
        try:
            with open(self.jsonFilePath, "r") as file:
                data = json.load(file)
                self.pipeline.execute(data)  

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.jsonFilePath}' not found.")
        
        except Exception as exp:
            raise Exception(f"Error : {exp} in loading the {self.jsonFilePath} file")
        
inputDrivers={"csv":CsvReader,"json":JsonReader}
        