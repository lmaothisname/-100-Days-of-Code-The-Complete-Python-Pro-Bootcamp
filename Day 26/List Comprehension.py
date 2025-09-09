numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)
name = "Thanh Hoa"
new_list = [letter for letter in name]
print(new_list)
new_l = [n * 2 for n in range(1,5)]
print(new_l)
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)