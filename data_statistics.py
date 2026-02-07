def sumGdp(dfc, dfr):
  
  ########For country########
  #the dfc.columns iterates over column names and the for each string isdigit is checked and filtered
  #the str.isdigit only returns bool is not typecasting anything)
  yearColumns = list(filter(str.isdigit, dfc.columns))

  #assign adds the sum in data frame where as drop then removes all year columns
  resultCountry = dfc.assign(Sum_of_GDP=dfc[yearColumns].sum(axis=1))
  resultCountry.drop(columns=yearColumns, inplace=True)

  return resultCountry
  