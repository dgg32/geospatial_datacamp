# Generate the choropleth and store the axis
n_trees_per_area = districts_trees.plot(column='n_trees_per_area', scheme='quantiles', k=7, cmap='YlGn', legend=True)

# Remove frames, ticks and tick labels from the axis
n_trees_per_area.set_axis_off()
plt.show()