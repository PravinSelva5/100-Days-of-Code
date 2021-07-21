import pandas

'''
data = pandas.read_csv("weather_data.csv")
print(data)

print("---------------------------\n")
print(data["temp"].max())
print(data["temp"].mean())
print("---------------------------\n")
# Get Data in columns
print(data["condition"])
print("\n")
print(data.condition)

print("---------------------------\n")
print(data[data.temp == data.temp.max()])



# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_2 =pandas.DataFrame(data_dict)
data_2.to_csv("new_data_2")
'''

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data.dict)
df.to_csv("squirrel_count.csv")