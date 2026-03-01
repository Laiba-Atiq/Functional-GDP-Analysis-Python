
def validateConfigFile(configDict):

    keyList = ["input", "output", "continent", "startYear", "endYear"]
    inputTypes=["csv","json"]
    outputTypes=["file","console"]

    #checking if all the required keys exist
    if not all(map(lambda k : k in configDict, keyList)):
        missing = list(filter(lambda k: k not in configDict, keyList))
        raise ValueError(f"Missing keys {missing} in config.json")
    
    #input type checks 
    if not isinstance(configDict["input"], str):
        raise TypeError("Error: input in config.json must be a string")
    
    if configDict["input"] not in inputTypes:
        raise TypeError("Error: invalid input type")
    
    if not isinstance(configDict["output"], str):
        raise TypeError("Error: output in config.json must be a string")
    
    if configDict["output"] not in outputTypes:
        raise TypeError("Error: invalid output type")
    
    if not isinstance(configDict["continent"], str):
        raise TypeError("Error: continent in config.json must be a string")
    
    if not configDict["continent"]:
        raise TypeError("Error: continent in config.json can't be empty")
    
    if not isinstance(configDict["startYear"], int):
        raise TypeError("Error: start year in config.json must be a integer")
    
    if not isinstance(configDict["endYear"], int):
        raise TypeError("Error: end year in config.json must be a integer")
    
    if not (configDict["startYear"]<configDict["endYear"]):
        raise TypeError("Error: the given year range is not valid")
    
    return configDict