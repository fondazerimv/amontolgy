from IPython.display import display
from geopy.geocoders import Nominatim
import pandas as pd
import re

#rawData = pd.read_csv("antiquari/0109infoviz/antiquari.csv")
rawData = pd.read_excel("antiquari/0109infoviz/antiquari.xlsx")

# Refine type 
for idx, row in rawData.iterrows():
    if "A" in str(row["Type"]):
        rawData.loc[idx, "Antiquario"] = 1
    elif "C" in str(row["Type"]):
        rawData.loc[idx, "Collezionista"] = 1
    elif "G" in str(row["Type"]):
        rawData.loc[idx, "Galleria"] = 1
    elif "CdA" in str(row["Type"]) or "CA" in str(row["Type"]):
        rawData.loc[idx, "Asta"] = 1
    rawData.drop(['Type'], axis=1)

# Refine location. Caveat: it considers only the first location, improves dataset
for idx, row in rawData.iterrows():
    location = str(row["Luogo"])
    re.sub("[\(].*?[\)]", "", location)
    sep = {",","/",";"}
    for el in sep:
        if el in location:
            placelist = location.split(el)
            rawData.loc[idx, "Luogo"] = placelist[0]

latList = []
lonList = []
for idx, row in rawData.iterrows():
    place = str(row["Luogo"])
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(place)
       
    try:
        latList.append(getLoc.latitude)
        lonList.append(getLoc.longitude)
    except AttributeError or ValueError:
        continue
    """
    print("================")
    print("Place:   ", place, type(getLoc))
    """
     
    
rawData["lat"] = latList
rawData["lon"] = lonList

rawData.to_csv("antiquari/0109infoviz/antiquari.csv", index=False)
