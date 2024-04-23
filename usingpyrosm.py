from pyrosm import OSM, get_data
import os

# Specify the path to your OSM file
osm_file_path = "map.osm"

# Create an OSM object
osm = OSM(osm_file_path)

# Read nodes, ways, and relations from the OSM file
nodes, ways, relations = osm.get_data_by_custom_criteria(
    custom_filter={"area": False},
    filter_type="keep",
    keep_unfiltered=False
)

# Print the data
print("Nodes:")
print(nodes.head())

print("Ways:")
print(ways.head())

print("Relations:")
print(relations.head())
