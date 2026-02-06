import pandas as pd

def loadGDPfile(dataFilePath):
    try:
        data = pd.read_csv(dataFilePath)
        return data
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{dataFilePath}' not found.")
        