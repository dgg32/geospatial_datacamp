# Import the districts dataset
districts = geopandas.read_file("paris_districts.geojson")

# Print the CRS information
print(districts.crs)

# Print the first rows of the GeoDataFrame
print(districts.head())