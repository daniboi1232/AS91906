import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a new figure
plt.figure(figsize=(5, 10))

# Create a Basemap instance with the desired map projection and region
map = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=90,
              llcrnrlon=-180, urcrnrlon=180, resolution='l')

# Draw coastlines, countries, and states (if available)
map.drawcoastlines()
map.drawcountries()
map.drawstates()

# Draw parallels and meridians
map.drawparallels(range(-90, 91, 30), labels=[1,0,0,0])
map.drawmeridians(range(-180, 181, 60), labels=[0,0,0,1])

# Add a title
plt.title('World Map with Basemap')

# Show the map
plt.show()
