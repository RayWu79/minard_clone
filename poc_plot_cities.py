import pandas as pd
import sqlite3
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

connection = sqlite3.connect("data/minard.db")
cities_df = pd.read_sql("""SELECT * FROM cities;""", con=connection)
connection.close
# print(cities_df)

lons = cities_df['lonc']
lats = cities_df['latc']
cities = cities_df['city']

fig, ax = plt.subplots()

m = Basemap(projection='lcc' ,resolution='i', width=1000000, height=400000, lon_0=31, lat_0=55, ax=ax)
m.drawrivers()
m.drawcountries()
m.drawparallels(range(54, 57), labels=[1, 0, 0, 0])
m.drawmeridians(range(23, 54, 2), labels=[0, 0, 0, 1])
x, y, = m(lons, lats)
for xi, yi, city in zip(x, y, cities):
    ax.annotate(text=city, xy=(xi, yi), fontsize=6)

plt.show()