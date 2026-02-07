def sumGdp(dfc, dfr):
  
  ########For country########
  #the dfc.columns iterates over column names and the for each string isdigit is checked and filtered
  #the str.isdigit only returns bool is not typecasting anything)
  yearColumns = list(filter(str.isdigit, dfc.columns))

  #assign adds the sum in data frame where as drop then removes all year columns
  resultCountry = dfc.assign(Sum_of_GDP=dfc[yearColumns].sum(axis=1))
  resultCountry.drop(columns=yearColumns, inplace=True)
  
  ########For regions########
  yearColumnsRegions = list(filter(str.isdigit, dfr.columns))

  #group data on the basis of region, then for all the rows only sum the year columns
  #the group label is then set as a column value along with year columns
  resultRegions = (dfc.groupby("Continent", as_index=False)[yearColumnsRegions].sum())

  return resultCountry,resultRegions
  