# Load the restaurants data
restaurants = geopandas.read_file("paris_restaurants.geosjon")

#print (restaurants.head())
# Calculate the number of restaurants of each type
type_counts = restaurants.groupby('type').size()

# Print the result
print(type_counts)