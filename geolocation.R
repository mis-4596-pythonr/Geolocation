library(tidyverse)
library(ggmap)
library(dplyr)
library(sf)
library(mapview)
library(ggrepel)

#set up connection with API
api <- "" #api key
register_google(key = api)
getOption("ggmap")

#retrieve the CSV file, put city column into data frame 
murders <- read.csv("pamurders.csv",stringsAsFactors = FALSE)
cities <- distinct(murders, City)
cities_df <- as.data.frame(cities)

#retreive geocodes, append attributes columns to geocodes, convert data frame to tibble
locations_df <- mutate_geocode(cities_df, City)
locations_df$Murders <- murders$Murders
locations_df$MurdersPer100k <- murders$Murders.100K
locations <- as_tibble(locations_df)

#plot cities with geocodes
locations_sf <- st_as_sf(locations, coords = c("lon", "lat"), crs = 4326)
mapviewOptions(
               raster.palette = grey.colors,
               vector.palette = colorRampPalette(c("pink", "red","red4")),
               na.color = "magenta",
               layers.control.pos = "topright")
mapview(locations_sf, zcol = "MurdersPer100k", cex="Murders")


