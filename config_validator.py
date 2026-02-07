def validateConfigSchema(configDict):

    keyList = ["region", "year", "country", "operation" , "output"]

    #checking if all teh required keys exist
    if not all(map(lamda k : k in configDict, keyList)):
        missing = list(filter(lamda k: k not in config, keyList))
        raise ValueError(f"Missing keys {missing} in config.json")

    #validating data types
    if not isinstance(configDict["region"], str):
        raise TypeError("Error: region in config.json must be a string")

    if not isinstance(configDict["year"], int):
        raise TypeError("Error: year in config.json must be an integer")

    if not isinstance(configDict["country"], str):
        raise TypeError("Error: country in config.json must be an integer")

    if not isinstance(configDict["operation"], str):
        raise TypeError("Error: operation in config.json must be an integer")
    
    if not isinstance(configDict["output"], str):
        raise TypeError("Error: output in config.json must be an integer")
    
    #checking valid values
    validOperations ={ "sum", "average"}
    if configDict["operation"] not in valid_operations:
        raise ValueError(f"Invalid operation: {configDict["operation"]} not allowed")

    validOutputs = {"dashboard"}
    if configDict["output"] not in valid_operations:
        raise ValueError(f"Invalid output: {configDict["output"]} not allowed")


    





