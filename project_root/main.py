from config_reader import readConfigFile
from config_validator import validateConfigFile
from plugins.inputs import inputDrivers
from core.engine import TransformationEngine

filePaths={"csv":"data\\gdp_with_continent_filled.csv","json":"data\\gdp_with_continent_filled.json"}

configDictionary = readConfigFile()
print("DONE 1")

configDictionary = validateConfigFile(configDictionary)
print("DONE 2")

engine=TransformationEngine()
reader=inputDrivers[configDictionary["input"]](filePaths[configDictionary["input"]], pipeline=engine)
reader.read()



