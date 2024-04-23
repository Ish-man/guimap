# # import osmnx as ox
# # import contextily as ctx
# # import matplotlib.pyplot as plt

# # filepath = "jalndhar.gpkg"

# # G = ox.load_graphml(filepath)
# # nodes, edges = ox.graph_to_gdfs(G)

# # fig, ax = plt.subplots(figsize=(10, 10))
# # edges.plot(ax=ax, linewidth=1, edgecolor='blue')

# # # Add a basemap using contextily (ensure you have the basemap tiles stored offline)
# # # ctx.add_basemap(ax, crs=edges.crs, source='ctx.providers.CartoDB.Voyager')

# # # Show the plot
# # plt.show()

# import geopandas as gpd
# import matplotlib.pyplot as plt

# # Specify the path to your GeoPackage file
# file_path = "jalndhar.gpkg"

# # Read the GeoPackage file using GeoPandas
# gdf = gpd.read_file(file_path)

# # Plot the GeoDataFrame
# gdf.plot()

# # Show the plot
# plt.title("GeoPackage Plot")
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.show()

import sys
import osmnx as ox
import geopandas as gpd
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import contextily as ctx

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the Matplotlib canvas
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        
        # Specify the path to your GeoPackage file
        # file_path = "jalndhar.gpkg"
        
        # Read the GeoPackage file using GeoPandas
        # gdf = gpd.read_file(file_path)
        
        osm_file_path = 'map.osm'

        G = ox.graph_from_xml(osm_file_path)
        nodes, edges = ox.graph_to_gdfs(G)
        
        # Plot the graph edges on the canvas
        edges.plot(ax=sc.axes, linewidth=0.8, edgecolor='blue')
        
        # Optionally, add a basemap using contextily
        ctx.add_basemap(sc.axes, crs=edges.crs, source=ctx.providers.OpenStreetMap.Mapnik)
        
        # Hide axes for better visualization
        sc.axes.set_axis_off()
        
        # Draw the plot
        sc.draw()

        # Create a navigation toolbar and layout
        toolbar = NavigationToolbar(sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold the toolbar and canvas
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle("Map Viewer")

        # Show the main window
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

