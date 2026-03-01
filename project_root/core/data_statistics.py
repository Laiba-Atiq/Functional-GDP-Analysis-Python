def sumGdp(dfc, dfr):
  
  ########For country########
  #the dfc.columns iterates over column names and the for each string isdigit is checked and filtered
  #the str.isdigit only returns bool is not typecasting anything)
  yearColumns = list(filter(str.isdigit, dfc.columns))
  dropColumns=["Indicator Name", "Indicator Code", "Country Code"]

  #assign adds the sum in data frame where as drop then removes all year columns
  resultCountry = dfc.assign(Sum_of_GDP=dfc[yearColumns].sum(axis=1))
  resultCountry.drop(columns=dropColumns, inplace=True)
  
  ########For regions########
  yearColumnsRegions = list(filter(str.isdigit, dfr.columns))

  #group data on the basis of region, then for all the rows only sum the year columns
  #the group label is then set as a column value along with year columns
  resultRegions = (dfc.groupby("Continent", as_index=False)[yearColumnsRegions].sum())

  return resultCountry,resultRegions

def avgGdp(dfc, dfr):
  
  ########For country########
  yearColumns = list(filter(str.isdigit, dfc.columns))
  dropColumns=["Indicator Name", "Indicator Code", "Country Code"]
  sizeCountry=len(yearColumns)

  resultCountry = dfc.assign(Avg_of_GDP=(dfc[yearColumns].sum(axis=1))/sizeCountry)
  resultCountry.drop(columns=dropColumns, inplace=True)

  ########For regions########
  yearColumnsRegions = list(filter(str.isdigit, dfr.columns))

  #the size region is grouped by regions containing number of rows for each continent
  sizeRegion = dfr.groupby("Continent").size()
  resultRegions = (dfr.groupby("Continent")[yearColumnsRegions].sum()
                   .div(sizeRegion,axis=0)
                   .reset_index())
  
  return resultCountry,resultRegions
  