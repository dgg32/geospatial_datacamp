result = rasterstats.zonal_stats(country.geometry, "DEM_gworld.tif", stats=['mean'])

countries['mean_elevation'] = pd.DataFrame(result)

countries.sort_values('mean_elevation', ascending=False).head(10)