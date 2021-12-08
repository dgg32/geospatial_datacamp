# Convert to the Web Mercator projection
restaurants_webmercator = restaurants.to_crs({'init': 'epsg:3857'})

# Plot the restaurants with a background map
ax = restaurants_webmercator.plot(markersize=1)
contextily.add_basemap(ax)
plt.show()