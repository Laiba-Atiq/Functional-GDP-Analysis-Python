import pandas as pd

def loadGDPfile(dataFilePath):
    try:
        data = pd.read_csv(dataFilePath)
        return data

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{dataFilePath}' not found.")
        
    except Exception as exp
        raise Exception(f"Error : {e} in loading the {dataFilePath} file")
        