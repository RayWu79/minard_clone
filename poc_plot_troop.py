import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect("data/minard.db")
troop_df = pd.read_sql("""SELECT * FROM troops;""", con=connection)
connection.close()
# print(troop_df)

lons = troop_df['lonp'].values
lats = troop_df['latp'].values
survives = troop_df['surviv'].values
directions = troop_df['direc'].values
divisions = troop_df['division'].values
# print(rows)

fig, ax = plt.subplots()

rows = troop_df.shape[0]
for i in range(rows - 1):
    if directions[i] == 'A':
        line_color = 'tan'
    else:
        line_color = 'black'
    start_stop_lons = (lons[i], lons[i+1])
    start_stop_lats = (lats[i], lats[i+1])
    line_width = survives[i]
    ax.plot(start_stop_lons, start_stop_lats, linewidth=line_width/20000, color=line_color)

plt.show()






