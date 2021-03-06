# Extract the single Point
eiffel_tower = s_eiffel_tower_projected[0]

#print (eiffel_tower)
# Ensure the restaurants use the same CRS
restaurants = restaurants.to_crs({'init': 'epsg:2154', 'no_defs': True})

# The distance from each restaurant to the Eiffel Tower
dist_eiffel = restaurants.distance(eiffel_tower)

# The distance to the closest restaurant
print(dist_eiffel.min())