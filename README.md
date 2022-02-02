# Group-Admin-Levels
This code consumes geojson country files to generate the total number of units within a specific admin level, while also getting the names of those admin levels as well as finding the least admin level possible.
The major task in this project was `web scraping`, `automation` and `classifying countries` and `finding total number of units in a certain admin level`.
`Web scraping` is a task that involves extracting and obtaining data from the web, usually from a data resource, i.e a website that has the required data. With the use of `Python`,
it becomes very easy and automated.
Our data resource is [GADM website](https://gadm.org/download_country.html), that contains all the countries' GIS files.

For this project, the required libraries include: `requests`, `json`, `beautifulsoup`, `defaultdict` etc. To install them, use `pip install`:
```
pip install beatifulsoup4
pip install requests
```

These libraries are then imported to our project.
``` 
from bs4 import BeautifulSoup
import requests
import os 
import json
from collections import defaultdict
```
