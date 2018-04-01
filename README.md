# Capstone Book Keeping
a personal documentation repo for the 311 capstone project

## Project Description
This project aims to build a data extraction and data processing tool for the NYC 311 data. Making it easier for researches from all disciplines to query and explore 311 data in personalized format

### Resources Links:
+ [311 api documentation](https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv)
  + [SoQL query functions documentation](https://dev.socrata.com/docs/functions/#2.1,)

+ jupyter notebook related
  + [bqplot](https://hub.mybinder.org/user/bloomberg-bqplot-npypnn3c/notebooks/examples/Index.ipynb)
  + [interactive_widgets](https://github.com/jupyter-widgets/ipywidgets/blob/master/docs/source/examples/Index.ipynb)
    + [ipywidgets_documentation](https://ipywidgets.readthedocs.io/en/latest/)
  + [code publishing](https://mybinder.org/)
+ Data base related
  + [PostgresQL-python](http://www.postgresqltutorial.com/postgresql-python/)
+ web development
  + [jekyll](https://jekyllrb.com/)

#### <span style="color:orange">To do list 2018/03/25</span>
+ figure out how to query with long multipolygon strings (which would otherwise result in a HTTP 414 error)
  + __potentially resolved, since the 311 dataset already contains higher level geospatial units such as borough, community district and neighborhoods. so as long as the geospatial units are small enough, we do not need to do split polygons (2018/03/29)__
+ figure out how to build a query with user interactive widget input
+ figure out memory saving ways to save then manipulate data (how to do everything without pd.DataFrame)
+ figure out how to make multiple same queries and return non-overlapping values
  + __potentially resolved as well, since we do not need to split large polygons anymore (2018/03/29)__

#### <span style="color:orange">To do list 2018/04/01</span>
+ Pull all static 311 data, and add geospatial columns such as census tract
  + how to categorize by census tract?
  + what is the ideal data format? --> HDFS
+ move data to data base
