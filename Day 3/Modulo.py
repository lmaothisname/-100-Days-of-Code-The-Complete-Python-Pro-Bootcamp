# The modulo operator gives you the remainder of a division.
# 6 % 2 #will be 0

# 6 % 5 #will be 1

# 6 % 4 #will be 2
# challenge 1:What is 10 % 3?
print(10 % 3)
#challenge 2:Check Odd or Even
number_to_check = int(input("What is the number you want to check?"))
if number_to_check % 2 == 0:
    print("It's even number.")
else:
    print("It's odd number.")