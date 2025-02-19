import sqlite3 
import pandas as pd
import matplotlib.pyplot as plt

conncetion = sqlite3.connect("data/minard.db")
temp_df = pd.read_sql("""SELECT * FROM temperatures;""", con=conncetion)
conncetion.close()

# print(temp_df)

temp_celsius = (temp_df["temp"] * 5/4).values
lons = temp_df["lont"].values
fig, ax = plt.subplots()
ax.plot(lons, temp_celsius)
ax.set_xlabel("Longitude")
ax.set_ylabel("Temperature (Celsius)")
plt.show()

