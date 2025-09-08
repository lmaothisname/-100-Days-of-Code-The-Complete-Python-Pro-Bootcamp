# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
with open("C:\Users\tranc\OneDrive\Máy tính") as file:
    contents = file.read()
    print(contents)
    #this no need to remember close after open
with open("new_file.txt",mode="w") as file:
    file.write("Ur mum Fat")