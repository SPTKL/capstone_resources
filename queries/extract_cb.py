import pandas as pd
from sodapy import Socrata
import json
import geopandas as gpd
import fiona
import shapely
import numpy as np
from shapely.geometry import asShape
import urllib.request, json
from tqdm import tqdm_notebook

client = Socrata("data.cityofnewyork.us", 'VQtPna4DyINdAHU8AgxFGwiEr')
def polygon_query_points_id(client, MTPLG):
    results = client.get("fhrw-4uyv",
                         select = 'unique_key',
                         limit = 5000000000000,
                         where = "within_polygon(location, '{0}')".format(MTPLG))
    return results

cb_raw = client.get("twhy-dzjp", limit = 5000000000000)
cb = gpd.GeoDataFrame.from_records(cb_raw)
cb['geometry'] = list(map(lambda x: asShape(x), cb.the_geom))

def create_dict(i):
    results = polygon_query_points(client, cb['geometry'][i])
    results = [dict(item, bctcb2010 = cb['bctcb2010'][i]) for item in results]
    return results

L = []
exceptions = []
for i in tqdm_notebook(range(0,38795-1000, 1000)):
    for j in tqdm_notebook(range(i, i + 1000)):
        try:
            L = L + create_dict(j)
        except Exception:
            exceptions.append(j)
 for j in tqdm_notebook(range(38000, 38794)):
        try:
            L = L + create_dict(j)
        except Exception:
            exceptions.append(j)

pd.DataFrame(L).to_csv('cb_2010_311_partial.csv', index = False)
