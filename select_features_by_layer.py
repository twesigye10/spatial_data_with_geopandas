import geopandas as gdp

# buildings datasets
df_data_19d = gdp.read_file(filename="outputs/19d_buildings.gpkg")

df_data_177 = gdp.read_file(filename="outputs/177_buildings.gpkg")

# host community dataset

df_data_host_community = gdp.read_file(filename="inputs/UGA_Host_subcounty.gpkg")
df_data_host_community_reproject = df_data_host_community.to_crs(df_data_19d.crs)
# select by another layer
df_selection_19d = df_data_19d.overlay(right=df_data_host_community_reproject, how="identity")

df_selection_177 = df_data_177.overlay(right=df_data_host_community_reproject, how="identity")

# write output
df_selection_19d.to_file("outputs/19d_buildings_ref_host.gpkg", layer='19d_buildings_ref_host', driver="GPKG")
df_selection_177.to_file("outputs/177_buildings_ref_host.gpkg", layer='177_buildings_ref_host', driver="GPKG")

