def validateConfigSchema(configDict):

    keyList = ["region", "year", "country", "operation" , "output"]

    #checking if all teh required keys exist
    if not all(map(lambda k : k in configDict, keyList)):
        missing = list(filter(lambda k: k not in configDict, keyList))
        raise ValueError(f"Missing keys {missing} in config.json")

    #validating input format as list:
    if not isinstance(configDict["region"], list):
        raise TypeError("Error: region in config.json must be a list")
 
    if not isinstance(configDict["year"], list):
        raise TypeError("Error: year in config.json must be a list")

    if not isinstance(configDict["country"], list):
        raise TypeError("Error: country in config.json must be a list")

    if not configDict["region"]:
        raise ValueError("Region is not specified")

    #validating data types
    if not all(map(lambda x: isinstance(x, str), configDict["region"])):
        raise TypeError("Error: region in config.json must be a string")

    if not all(map(lambda x: isinstance(x, int), configDict["year"])):
        raise TypeError("Error: year in config.json must be an integer")

    if not all(map(lambda x: isinstance(x, str), configDict["country"])):
        raise TypeError("Error: country in config.json must be a string")

    if not isinstance(configDict["operation"], str):
        raise TypeError("Error: operation in config.json must be a string")
    
    if not isinstance(configDict["output"], str):
        raise TypeError("Error: output in config.json must be a string")
    
    #checking valid values
    validOperations ={ "sum", "average"}
    if configDict["operation"] not in validOperations:
        raise ValueError(f"Invalid operation: {configDict['operation']} not allowed")

    validOutputs = {"dashboard"}
    if configDict["output"] not in validOutputs:
        raise ValueError(f"Invalid output: {configDict['output']} not allowed")

    return configDict

def validateConfigState(configDict, df):

    #creating sets of regions, year and countries
    regions = set(df["Continent"])
    countries = set(df["Country Name"])
    years = set(
        map(int,
            filter(lambda col: col.isdigit(), df.columns)
        )
    )


    #checking valid values of region, year and country:
    if not all(map(lambda r: r in regions, configDict["region"])):
        invalidRegions = list(filter(lambda r: r not in regions, configDict["region"]))
        raise ValueError(f"Invalid region: {invalidRegions} not present in dataset")

    if not all(map(lambda y: y in years, configDict["year"])):
        invalidYears = list(filter(lambda y: y not in years, configDict["year"]))  
        raise ValueError(f"Invalid year: {invalidYears} not present in the dataset")  

    if not all(map(lambda c: c in countries, configDict["country"])):
        invalidCountries = list(filter(lambda c: c not in countries, configDict["country"]))
        raise ValueError(f"Invalid country: {invalidCountries} not present in dataset")

    return True        

def validateConfig(configDict, df):
    configDict = validateConfigSchema(configDict)
    validateConfigState(configDict, df)
    return configDict
    



    





