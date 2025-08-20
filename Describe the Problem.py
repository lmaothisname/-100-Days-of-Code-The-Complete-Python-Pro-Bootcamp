def my_function():
    for i in range(1,20):
        if i == 20:
            print("You got it")

my_function()
# What is the for loop doing? -> the loop is iterative value i from 1 to 19
# When is the function meant to print "You got it"?  -> when i loop step 20 and i = 20 it will print "You got it"
# What are your assumptions about the value of i? -> the i will loop to 19 it will not print "You got it"

# solution
def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")
my_function()