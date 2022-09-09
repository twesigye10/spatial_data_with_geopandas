import geopandas as gdp

df_data_host_community_reproj = gdp.read_file(filename="outputs/ref_host_districts.gpkg")
print("Finished reading data")
df_data_osm = gdp.read_file(filename="inputs/uganda_osm_09_2022/gis_osm_buildings_a_free_1.shp", mask=df_data_host_community_reproj)
print("Finished reading file: gis_osm_buildings")
df_data_osm.to_file("outputs/osm_buildings_host_districts_kampala.gpkg", layer='osm_buildings_ref_host', driver="GPKG")
print("***       Finished processing osm_buildings         ***")