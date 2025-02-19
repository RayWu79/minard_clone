import pandas as pd
import sqlite3
class CreateMinardDB():
    def __init__(self):
        with open("data/minard.txt") as f:
            lines = f.readlines()

        column_names = lines[2].split()
        patterns_replace = {"(", "$", ")", ","}
        adjusted_column_names = []
        for column_name in column_names:
            for pattern in patterns_replace:
                if pattern in column_name:
                    column_name = column_name.replace(pattern, "")
            adjusted_column_names.append(column_name)
        self.lines = lines
        self.column_name_city = adjusted_column_names[:3]
        self.column_name_temp = adjusted_column_names[3:7]
        self.column_name_troop = adjusted_column_names[7:]

# print(column_name_city)
# print(column_name_temp)
# print(column_name_troop)
    def create_cities_df(self):
        i=6
        longitudes, latitudes, cities = [], [], []
        while i <= 25:
            long, latc, city = self.lines[i].split()[:3]
            longitudes.append(float(long))
            latitudes.append(float(latc))
            cities.append(city)
            i+=1
        # print(longitudes)
        # print(latitudes)
        # print(cities)
        city_data = (longitudes, latitudes, cities)
        city_df = pd.DataFrame()
        for city_name, data in zip(self.column_name_city, city_data):
            city_df[city_name] = data
        return city_df
        # print(city_df)
    def create_temperatures_df(self):
        i = 6
        longitudes, temperatures, days, dates = [], [], [], []
        while i <= 14:
            line_split = self.lines[i].split()
            longitudes.append(float(line_split[3]))
            temperatures.append(int(line_split[4]))
            days.append(int(line_split[5]))
            if i == 10:
                dates.append("Nov 24")
            else:
                date_str = line_split[6] + " " + line_split[7]
                dates.append(date_str)
            i+=1
        temperature_date = (longitudes, temperatures, days, dates)

        temperature_df = pd.DataFrame()
        for column_name, data in zip(self.column_name_temp, temperature_date):
            temperature_df[column_name] = data
        return temperature_df

#  print(temperature_df)
    def create_troops_df(self):
        longitudes, latitudes, survives, directions, divisions = [], [], [], [], []
        i = 6
        while i <= 53:
            line_split = self.lines[i].split()
            divisions.append(int(line_split[-1]))
            directions.append(line_split[-2])
            survives.append(int(line_split[-3]))
            latitudes.append(float(line_split[-4]))
            longitudes.append(float(line_split[-5]))
            i+=1

        troop_data = (longitudes, latitudes, survives, directions, divisions)

        troop_df = pd.DataFrame()
        for column, data in zip(self.column_name_troop, troop_data):
            troop_df[column] = data
        return troop_df
        # print(troop_df)


    def create_sqlite_db(self):
        connection = sqlite3.connect('data/minard.db')
        city_df = self.create_cities_df()
        temperature_df = self.create_temperatures_df()
        troop_df = self.create_troops_df()
        df_dict = {
            "cities": city_df,
            "temperatures": temperature_df,
            "troops": troop_df
        }

        for key, value in df_dict.items():
            value.to_sql(name=key, con=connection, index=False, if_exists="replace")
        connection.close()

create_minard_db = CreateMinardDB()
create_minard_db.create_sqlite_db()


