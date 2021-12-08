# Read the restaurants csv file
restaurants = pd.read_csv("paris_restaurants.csv")

# Import contextily
import contextily

# A figure of all restaurants with background
fig, ax = plt.subplots()
ax.plot(restaurants.x, restaurants.y, 'o', markersize=1)
contextily.add_basemap(ax)
plt.show()