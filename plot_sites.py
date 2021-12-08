# Plot of the parks and mining sites
ax = national_parks.plot(color='green')
mining_sites.plot(ax=ax, markersize=5, column = "mineral", legend=True)
ax.set_axis_off()
plt.show()