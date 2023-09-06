
# with open("./weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
mean = data["temp"].mean()
max = data["temp"].max()
print(max)


