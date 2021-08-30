import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pyproj import CRS
import matplotlib.pyplot as plt

#read_file ref_province.shp
g1 = gpd.read_file (r'D:\T\เขตปกครอง\ref_province.shp')

#read_file data_point.csv
df = pd.read_csv (r'D:\T\data_point.csv')

#drop lon lat
df1 = df.dropna(subset=['lon','lat'])

#Convert the DataFrame's content (e.g. Lat and Lon columns) 
#into appropriate Shapely geometries first and then use them together 
#with the original DataFrame to create a GeoDataFrame.
geometry = [Point(xy) for xy in zip (df1['lon'], df1['lat'])]
gdf1 = gpd.GeoDataFrame(df1, crs = CRS.from_string("epsg:4326"), geometry=geometry)
g1 = g1.to_crs("EPSG:32647")
gdf1 = gdf1.to_crs("EPSG:32647")

#With how='intersection', it returns only those geometries that are contained 
#by both GeoDataFrames
country_cores = gpd.overlay( gdf1, g1 , how='intersection')
country_cores.plot(color = 'red',markersize = 4)

country_cores.to_csv(r'test.csv')