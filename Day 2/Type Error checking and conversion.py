# TypeError
# These errors occur when you are using the wrong data type. e.g. len(12345)
# Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

# Ex:len(123)
# No TypeErrorx
len("Hello")
# Type Checking
# you can check the data type of any value or variable in python using the type() function
# print(type("abc")) #will give you <class 'str'>
print(type("Thanh Hoa"))
print(type(36))
print(type(3.6))
print(type(True))
# Type Conversion
# you can convert data into different data types using special functions
str()
int()
float()
bool()
name_of_the_user = input("What's your name?")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))