# capstone_resources
a personal documentation repo for the 311 capstone project

## project description
This project aims to build a data extraction and data processing tool for the NYC 311 data. Making it easier for researches from all disciplines to query and explore 311 data in personalized format

### resources links:
+ [311 api documentation](https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv)
  + [SoQL query functions documentation](https://dev.socrata.com/docs/functions/#2.1,)

+ jupyter notebook related
  + [bqplot](https://hub.mybinder.org/user/bloomberg-bqplot-npypnn3c/notebooks/examples/Index.ipynb)
  + [interactive_widgets](https://github.com/jupyter-widgets/ipywidgets/blob/master/docs/source/examples/Index.ipynb)
    + [ipywidgets_documentation](https://ipywidgets.readthedocs.io/en/latest/)
  + [code publishing](https://mybinder.org/)

# To do list
+ figure out how to query with long multipolygon strings (which would otherwise result in a HTTP 414 error)
+ figure out how to build a query with user interactive widget input
+ figure out memory saving ways to save then manipulate data (how to do everything without pd.DataFrame)
+ figure out how to make multiple same queries and return non-overlapping values
