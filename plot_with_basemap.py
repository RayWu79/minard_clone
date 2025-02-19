import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Call sql and extract tables
connection = sqlite3.connect("data/minard.db")
cities_df = pd.read_sql("""SELECT * FROM cities;""", con=connection)
temperatures_df = pd.read_sql("""SELECT * FROM temperatures;""", con=connection)
troops_df = pd.read_sql("""SELECT * FROM troops;""", con=connection)
connection.close()

# print(cities_df)
# print(temperatures_df)
# print(troops_df)

# Extract data points
loncs = cities_df['lonc'].values
latcs = cities_df['latc'].values
city_names = cities_df['city'].values
lonts = temperatures_df['lont'].values
temps = temperatures_df['temp'].values
days = temperatures_df['days'].values
dates = temperatures_df['date'].values
rows = troops_df.shape[0]
lonps = troops_df['lonp'].values
latps = troops_df['latp'].values
survives = troops_df['surviv'].values
directions = troops_df['direc'].values
divisions = troops_df['division'].values

fig, ax = plt.subplots(nrows=2, figsize=(25, 12), gridspec_kw={"height_ratios": [4, 1]})

#Basemap setting
m = Basemap(projection="lcc", resolution="i", width=1000000, height=400000, lat_0=55, lon_0=31, ax=ax[0])
m.drawcounties()
m.drawrivers()
m.drawparallels(range(54, 57), labels=[1, 0, 0, 0])
m.drawmeridians(range(23, 54, 2), labels=[0, 0, 0, 1])

# draw cities
x, y, = m(loncs, latcs)
for xi, yi, city_name in zip(x, y, city_names):
    ax[0].annotate(text=city_name, xy=(xi, yi), fontsize=14, zorder=1)

# draw troops
x, y, = m(lonps, latps)
for i in range(rows - 1):
    if directions[i] == 'A':
        line_color = 'tan'
    else:
        line_color = 'black'
    start_stop_lons = (x[i], x[i+1])
    start_stop_lats = (y[i], y[i+1])
    line_width = survives[i]
    ax[0].plot(start_stop_lons, start_stop_lats, linewidth=line_width/20000, color=line_color, zorder=0)

temp_celsius = (temperatures_df["temp"] * 5/4).astype(int)
annotations = temp_celsius.astype(str).str.cat(temperatures_df['date'], sep="°C")
ax[1].plot(lonts, temp_celsius, linestyle="dashed", color="black")
for lont, temp_c, annotaion in zip(lonts, temp_celsius, annotations):
    ax[1].annotate(annotaion, xy=(lont-0.3, temp_c-7), fontsize=16)
ax[1].set_ylim(-50, 10)
ax[1].spines['top'].set_visible(False)
ax[1].spines['bottom'].set_visible(False)
ax[1].spines['left'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].grid(True, which='major', axis='both')
ax[1].set_xticklabels([])
ax[1].set_yticklabels([])
ax[1].set_xlabel("Longitude", fontsize=20)
ax[1].set_ylabel("Temperature (Celsius)", fontsize=20)
ax[0].set_title("Napolean's disastrous Russian campaign of 1800", loc="left", fontsize=30)
plt.tight_layout()
fig.savefig("minard_clone.png")
