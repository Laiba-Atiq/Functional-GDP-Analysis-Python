def validateConfigSchema(configDict):

    keyList = ["region", "year", "country", "operation" , "output"]

    #checking if all teh required keys exist
    if not all(map(lamda k : k in configDict, keyList)):
        missing = list(filter(lamda k: k not in config, keyList))
        raise ValueError(f"Missing keys {missing} in config.json")

    return configDict

    


