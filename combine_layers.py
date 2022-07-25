import geopandas as gdp

df_data_177 = gdp.read_file(filename="outputs/177_buildings_ref_host.gpkg")
print("Finished reading file: 177_buildings")

df_data_19d = gdp.read_file(filename="outputs/19d_buildings_ref_host.gpkg")
print("Finished reading file: 19d_buildings")

combined_layers = df_data_177.append(df_data_19d)
print("Finished combining files")

combined_layers.to_file("outputs/UGA_buildings_ref_host.gpkg", layer='UGA_buildings_ref_host', driver="GPKG")

print("Exported combined files")
