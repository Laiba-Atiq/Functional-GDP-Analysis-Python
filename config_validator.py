def validateConfigSchema(configDict):

    keyList = ["region", "year", "country", "operation" , "output"]

    #checking if all teh required keys exist
    if not all(map(lambda k : k in configDict, keyList)):
        missing = list(filter(lambda k: k not in config, keyList))
        raise ValueError(f"Missing keys {missing} in config.json")

    #validating data types
    if not isinstance(configDict["region"], str):
        raise TypeError("Error: region in config.json must be a string")

    if not isinstance(configDict["year"], int):
        raise TypeError("Error: year in config.json must be an integer")

    if not isinstance(configDict["country"], str):
        raise TypeError("Error: country in config.json must be a string")

    if not isinstance(configDict["operation"], str):
        raise TypeError("Error: operation in config.json must be a string")
    
    if not isinstance(configDict["output"], str):
        raise TypeError("Error: output in config.json must be a string")
    
    #checking valid values
    validOperations ={ "sum", "average"}
    if configDict["operation"] not in valid_operations:
        raise ValueError(f"Invalid operation: {configDict["operation"]} not allowed")

    validOutputs = {"dashboard"}
    if configDict["output"] not in validOutputs:
        raise ValueError(f"Invalid output: {configDict["output"]} not allowed")

    return configDict

def validateConfigState(configDict, df):

    #creating sets of regions, year and countries
    regions = set(df["Continent"])
    years = set(df["Year"])
    countries = set(df["Country Name"])

    #checking valid values of region, year and country:
    if config["region"] not in regions:
        raise ValueError(f"Invalid region: {configDict["region"]} is not present in the dataset")

    if config["year"] not in years:
        raise ValueError(f"Invalid year: {configDict["year"]} is not present in the dataset")  

    if config["country"] not in countries:
        raise ValueError(f"Invalid country: {configDict["country"]} is not present in the dataset")

    #validaing if the country belogs to the given region:
    if configDict["Country"] != "" and configDict["region"] != "":
        countryRegions = df[df["Country Name"] == configDict["country"]]["Continent"].unique()

        if len(countryRegions == 0) or config["region"] not on countryRegions:
            raise ValueError(f"Error: {configDict["country"]} does not belong to the region {config["region"]}")

    return True        

def validateConfig(configDict, df):
    configDict = validateConfigSchema(config)
    validateConfigState(configDict, df)
    return configDict
    



    





