from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection="lcc", resolution="i", width=1000000, height=400000, lat_0=55, lon_0=31)

lons = [24.0, 37.6] # 24.0 55.0 Kowno
lats = [55.0, 55.8] # 37.6 55.8 Moscou
m.drawcounties()
m.drawrivers()
m.drawparallels(range(54, 57), labels=[1, 0, 0, 0])
m.drawmeridians(range(23, 54, 2), labels=[0, 0, 0, 1])
xi, yi = m(lons, lats)
m.scatter(xi, yi)
plt.show()