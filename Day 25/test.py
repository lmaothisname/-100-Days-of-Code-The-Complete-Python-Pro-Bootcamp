# with open(r"D:\python\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         temperatures.append(row[1])
#     print(temperatures)
import pandas

data = pandas.read_csv(r"D:\Python\Day 25\weather_data.csv")
temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "students" : ["Amy","James","Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv(r"D:\python\Day 25\new_data.csv")

# data = pandas.read_csv(r"D:\python\Day 25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrel_count = len(data[data["Primary Fur Color"] == "Grey"])
# red_squirre_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirre_count = len(data[data["Primary Fur Color"] == "Black"])
# data_dict = {
#     "Fur Color" : ["Gray", "Cinammon","Black"],
#     "Count" : [grey_squirrel_count,red_squirre_count,black_squirre_count]
# }
# data_csv = pandas.DataFrame(data_dict)
# data_csv.to_csv(r"D:\python\Day 25\squirrel_count.csv")