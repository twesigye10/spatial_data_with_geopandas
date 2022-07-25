import geopandas as gdp

df_data_host_community = gdp.read_file(filename="outputs/ref_host_reprojected.gpkg")
print("Finished reading file: ref_host_reprojected")

df_data_177 = gdp.read_file(filename="outputs/177_buildings.gpkg", mask=df_data_host_community)
print("Finished reading file: 177_buildings")
df_data_177.to_file("outputs/177_buildings_ref_host.gpkg", layer='177_buildings_ref_host', driver="GPKG")
print("***       Finished processing 177_buildings         ***")


