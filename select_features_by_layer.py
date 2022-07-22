import geopandas as gdp

# buildings datasets
df_data_19d = gdp.read_file(filename="outputs/19d_buildings.gpkg")

df_data_177 = gdp.read_file(filename="outputs/177_buildings.gpkg")

# host community dataset

df_data_host_community = gdp.read_file(filename="inputs/UGA_Host_subcounty.gpkg")

