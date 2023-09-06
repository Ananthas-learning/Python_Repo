import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == 'Gray'])
red_squirrel_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrel_count = len(data[data["Primary Fur Color"] == 'Black'])

squirrel_count = {"color": ["Gray", "Cinnamon", "Black"], "count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]}

df = pandas.DataFrame(squirrel_count)
df.to_csv("Squirrel_Count.csv")
# grouped_set = data.groupby("Primary Fur Color")
# count = grouped_set.count()
# print(grouped_set["Primary Fur Color"], count)


