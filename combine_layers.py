import geopandas as gdp
import pandas as pd

df_data_177 = gdp.read_file(filename="outputs/177_buildings_ref_districts_kampala.gpkg")
print("Finished reading file: 177_buildings")

df_data_19d = gdp.read_file(filename="outputs/19d_buildings_ref_districts_kampala.gpkg")
print("Finished reading file: 19d_buildings")

combined_layers = pd.concat([df_data_177, df_data_19d])
print("Finished combining files")

combined_layers.to_file("outputs/UGA_google_buildings_ref_host_kampala.gpkg", layer='uga_google_buildings_ref_host_kampala', driver="GPKG")

print("Exported combined files")
