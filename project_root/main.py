from config_reader import readConfigFile
from config_validator import validateConfigFile
from plugins.inputs import inputDrivers
from plugins.outputs import outputDrivers
from core.engine import TransformationEngine

filePaths={"csv":"data\\gdp_with_continent_filled.csv","json":"data\\gdp_with_continent_filled.json"}

configDictionary = readConfigFile()

configDictionary = validateConfigFile(configDictionary)

sink=outputDrivers[configDictionary["output"]](configDictionary)
engine=TransformationEngine(configDictionary, sink=sink)
reader=inputDrivers[configDictionary["input"]](filePaths[configDictionary["input"]], pipeline=engine)
reader.read()



