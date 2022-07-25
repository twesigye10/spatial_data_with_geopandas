import geopandas as gdp

df_data_host_community = gdp.read_file(filename="inputs/UGA_Host_subcounty.gpkg")

df_data_host_community_reproject = df_data_host_community.to_crs("EPSG:4326")

df_data_host_community_reproject.to_file("outputs/ref_host_reprojected.gpkg", layer='ref_host_reprojected', driver="GPKG")
