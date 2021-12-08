# Inspect the first rows of the districts dataset
print(districts.head())

# Inspect the area of the districts
print(districts.area)

# Add a population density column
districts['population_density'] = districts['population'] / districts.area * 10**6

# Make a plot of the districts colored by the population density
districts.plot(column='population_density', legend=True)
plt.show()