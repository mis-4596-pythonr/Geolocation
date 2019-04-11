#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import googlemaps


# In[2]:


murders = pd.read_csv("C:/Users/Kyle Haberman/Documents/pamurders.csv")


# In[3]:


cities = murders["City"]
cities = pd.DataFrame(cities)


# In[4]:


gmaps_key = googlemaps.Client(key = "") #api key


# In[5]:


cities["LAT"] = None
cities["LON"] = None


# In[6]:


for i in range(0, len(cities), 1):
    geocode_result = gmaps_key.geocode(cities.iat[i,0])
    try: 
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
        cities.iat[i, cities.columns.get_loc("LAT")] = lat
        cities.iat[i, cities.columns.get_loc("LON")] = lon
    except:
        lat = None
        lon = None
        
cities


# In[7]:


cities['Murders'] = murders['Murders']
cities['Murders/100K'] = murders['Murders/100K']
cities


# In[8]:


locations = cities[['LAT', 'LON']]
locationlist = locations.values.tolist()
len(locationlist)
locationlist[7]


# In[9]:


import folium

m = folium.Map(location=[41, -77.5], tiles='cartodbpositron',
                   zoom_start=7, control_scale=True)
for point in range(0, len(locationlist)):
    folium.CircleMarker(locationlist[point], popup=cities['City'][point], radius=int(cities.iloc[point]['Murders'])/11,
                       color="red", fill=True).add_to(m)
m

