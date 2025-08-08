bmi = 84 / 1.65 ** 2
# Original float with decimal places
print(bmi)
# Flooring a Number
# you can floor a number or remove all decimal places using the int() function which converts a floating point number(with decimal places) into an integer(whole number).
print(int(bmi))
# Rounding a Number
# However,if you want to round a decimal number to nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds 
# down.Then you can use the python round() function.

# Rounding the number into whole number
print(round(bmi))

# Rounding only to 2 decimal places
print(round(bmi,2))
# Accumulate
score = 0

# Assignment Operators
# Assignment Operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
# +=
# -=
# *=
# /=

# User scores a point
score += 1
print(score)

#Also
score -= 1
score *= 1
score /= 1

score = 0
height = 1.8
is_winning = True
# f-String
# In python, we can use f-strings to insert a variable or an expression into a string.
print(f"Your score is = {score}, your height is {height}. You are winning is{is_winning}")