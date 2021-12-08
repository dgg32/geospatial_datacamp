# Read the mining site data
mining_sites = geopandas.read_file("ipis_cod_mines.geojson")
national_parks = geopandas.read_file("cod_conservation.shp")

# Convert both datasets to UTM projection
mining_sites_utm = mining_sites.to_crs(epsg=32735)
national_parks_utm = national_parks.to_crs(epsg=32735)

# Write converted data to a file
mining_sites_utm.to_file("ipis_cod_mines_utm.gpkg", driver="GPKG")
national_parks_utm.to_file("cod_conservation_utm.shp", driver="ESRI Shapefile")