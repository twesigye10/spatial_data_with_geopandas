from pandas import read_csv
from geopandas import GeoDataFrame
from shapely import wkt

# testing
df_test = read_csv("inputs/19d_buildings_test.csv")
df_test_one_column = df_test[["geometry"]]
print("number of features: {0}".format(len(df_test_one_column)))
print("Columns: {0}".format(df_test_one_column.columns))
gdf_test = GeoDataFrame(df_test_one_column, crs="EPSG:4326", geometry=df_test_one_column['geometry'].apply(wkt.loads))
gdf_test.to_file("outputs/19d_buildings_test.gpkg", layer='test_data', driver="GPKG")

# data 19d_buildings
df_19d = read_csv("inputs/19d_buildings.csv")
df_19d_one_column = df_19d[["geometry"]]
gdf_19d = GeoDataFrame(df_19d_one_column, crs="EPSG:4326", geometry=df_19d_one_column['geometry'].apply(wkt.loads))
gdf_19d.to_file("outputs/19d_buildings.gpkg", layer='19d_buildings', driver="GPKG")

# data 177_buildings
df_177 = read_csv("inputs/177_buildings.csv")
df_177_one_column = df_177[["geometry"]]
gdf_177 = GeoDataFrame(df_177_one_column, crs="EPSG:4326", geometry=df_177_one_column['geometry'].apply(wkt.loads))
gdf_177.to_file("outputs/177_buildings.gpkg", layer='177_buildings', driver="GPKG")

print("Finished geo data processing")
