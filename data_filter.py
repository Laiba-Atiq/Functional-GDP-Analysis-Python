def filterByCountry(configDict, df):
    if not configDict["country"]:  # empty list
        return df
    return df.loc[df["Country Name"].map(lambda c: c in configDict["country"])]
