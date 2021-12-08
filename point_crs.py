# Construct a Point object for the Eiffel Tower
from shapely.geometry import Point
eiffel_tower = Point(2.2945, 48.8584)

# Put the point in a GeoSeries with the correct CRS
s_eiffel_tower = geopandas.GeoSeries([eiffel_tower], crs={'init': 'EPSG:4326'})

# Convert to other CRS
s_eiffel_tower_projected = s_eiffel_tower.to_crs({'init': 'epsg:2154'})

# Print the projected point
print(s_eiffel_tower_projected)