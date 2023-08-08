# Spatial data with Geopandas

This project contains scripts for processing spatial data especially if you have trouble with large spatial datasets.
We used it to process Open buildings from google and shelters from OSM.

## Processing Open buildings from Google 

Run the following  scripts to extract buildings of interest.
In this scenario, we were extracting buildings for refugee hosting districts that we then combine with osm and use for sampling.

> 1. convert_csv_to_geopackage_with_geopandas.py. This will convert csv files downloaded into geopackage format
> 2. selection_mask.py. This will help for the layers we have converted to geopackage to now select buildings of interest defined by the boundary of the mask.
> 3. combine_layers.py. This will help to combine the buildings selected from the previous step into a single file.

## Processing osm buildings from OpenStreetMap 

For this, we just need to

> selection_mask_hosting_districts.py This helps to extract only buildings within the refugee hosting districts
> 
 
