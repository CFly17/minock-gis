import geopandas as gpd
import pandas as pd

# Load the updated CSV file
csv_file = 'path/to/resident_taxpayer_information.csv'
df_csv = pd.read_csv(csv_file)

# Load the geospatial data files
gpkg_file = 'path/to/data.gpkg'
geojson_file = 'path/to/data.geojson'
geodb_file = 'path/to/data.gdb'

# Read geopackage
gdf_gpkg = gpd.read_file(gpkg_file)

# Assume 'parcel_id' is the common identifier
gdf_gpkg = gdf_gpkg.merge(df_csv, left_on='parcel_id', right_on='parcel_id')

# Save the updated geopackage
gdf_gpkg.to_file(gpkg_file, layer='parcels', driver='GPKG')

# The process would be similar for .geojson and geodatabase files
# ...

# Note: You need to ensure that the geodatabase can be accessed by geopandas, which might require additional libraries or drivers
