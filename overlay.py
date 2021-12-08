# Print the first five rows of both datasets
print(land_use.head())
print(districts.head())

# Overlay both datasets based on the intersection
combined = geopandas.overlay(land_use, districts, how='intersection')

# Print the first five rows of the result
print(combined.head())