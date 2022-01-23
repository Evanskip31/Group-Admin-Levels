# import json
# data = json.loads('H:/WORK/Upwork/Project 7 - Python School Data Analysis/Countries Admin Levels/GADM-Countries/Extracted/Admin Data GeoJSON/Andorra/gadm36_AND_0.geojson')
# data['features'][0]['geometry'] 
# import geopandas as gpd
# import pandas as pd
# earthquake = pd.read_json('H:/WORK/Upwork/Project 7 - Python School Data Analysis/Countries Admin Levels/GADM-Countries/Extracted/Admin Data GeoJSON/Andorra/gadm36_AND_0.geojson')
# print(earthquake.head())

import json
with open('H:/WORK/Upwork/Project 7 - Python School Data Analysis/Countries Admin Levels/GADM-Countries/Extracted/Admin Data GeoJSON/Australia/gadm36_AUS_2.geojson') as f:
    data = json.load(f)
for feature in data['features']:
    print(feature['properties'])