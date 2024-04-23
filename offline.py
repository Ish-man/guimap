import osmnx as ox
import contextily as ctx
import matplotlib.pyplot as plt

# Path to your downloaded OSM file (e.g., 'jalandhar.osm')
osm_file_path = 'map.osm'

# Create a network from the local OSM file
G = ox.graph_from_xml(osm_file_path)

# Convert graph to GeoDataFrames
nodes, edges = ox.graph_to_gdfs(G)

# Plot the edges GeoDataFrame
fig, ax = plt.subplots(figsize=(10, 10))
edges.plot(ax=ax, linewidth=1, edgecolor='blue')

# Add a basemap using contextily (ensure you have the basemap tiles stored offline)
ctx.add_basemap(ax, crs=edges.crs, source='ctx.providers.CartoDB.Voyager')

# Show the plot
plt.show()
