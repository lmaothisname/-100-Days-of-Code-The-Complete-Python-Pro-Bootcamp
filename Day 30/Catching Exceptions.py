try:
    file = open(r"D:\Python\Day 30\a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["rauma"])
except FileNotFoundError:
    file = open(r"D:\Python\Day 30\a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key{error_message} does not exists.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("Your program close")