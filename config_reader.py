import json as j

def readConfigFile(dataFilePath = "config.json"):
    try:
        with open (dataFilePath, "r") as file:
            configDict = j.load(file)

        return configDict  

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: config file {dataFilePath} not found")

    except j.JSONDecodeError:
        raise ValueError("Error: config.json is not a valid json file")

    except Exception as exp:
        raise Exception(f"Error: {exp} in loading the {dataFilePath} file")    


