def filterByCountry(configDict, df):
    if not configDict["country"]:  # empty list
        return df
    return df.loc[df["Country Name"].map(lambda c: c in configDict["country"])]


def filterByRegion(configDict, df):
    regionFilter = df.loc[df["Continent"].map(lambda r: r in configDict["region"])]

    #filtering by yaer if list is not empty
    if not configDict["year"]:
        return regionFilter

    yearColumns = list(map(str, configDict["year"])) 

    return regionFilter.loc[:, regionFilter.columns.isin(
        ["Country Name", "Country Code",
        "Indicator Name", "Indicator Code", "Continent"] + yearColumns
        )
    ]