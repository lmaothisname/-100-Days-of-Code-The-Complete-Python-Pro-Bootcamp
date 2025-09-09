with open(r"D:\Python\Day 26\file1.txt") as var:
    var_data = var.readlines()
with open(r"D:\Python\Day 26\file2.txt") as file:
    file_data = file.readlines()
result = [int(num) for num in var_data if num in file_data]
print(result)