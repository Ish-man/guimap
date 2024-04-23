# import osmnx as ox
# import contextily as ctx
# import matplotlib.pyplot as plt

# location_point = (31.28315, 75.64664)

# G = ox.graph_from_point(location_point, dist=1000, dist_type="bbox", network_type="drive")

# nodes, edges = ox.graph_to_gdfs(G)

# fig, ax = plt.subplots(figsize=(10, 10))
# edges.plot(ax=ax, linewidth=1, edgecolor='blue')

# ctx.add_basemap(ax, crs=edges.crs, source=ctx.providers.CartoDB.Voyager)


# # Show the plot
# plt.show()
import osmnx as ox
import contextily as ctx
import matplotlib.pyplot as plt

# Define a point in Jalandhar, Punjab, India
location_point = (31.2838319, 75.5918736)

# Create a network from point, within a bounding box of 1km from the point
G = ox.graph_from_point(location_point, dist=1000, dist_type="bbox", network_type="drive")

# Convert graph to GeoDataFrames
nodes, edges = ox.graph_to_gdfs(G)

# Plot the edges GeoDataFrame
fig, ax = plt.subplots(figsize=(10, 10))
edges.plot(ax=ax, linewidth=0.01, edgecolor='blue')

# Add a satellite basemap using contextily
ctx.add_basemap(ax, crs=edges.crs, source=ctx.providers.CartoDB.Voyager)

# Show the plot
plt.show()