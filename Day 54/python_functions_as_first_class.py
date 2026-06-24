def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

#First-class objects, can be passed around as arguments e.g. int/string/float/etc.
def calculate(calc_function,n1,n2):
  return calc_function(n1,n2)

print(calculate(add,3,4))

# Nested Functions

def outer_function():
  print("I'm outer")
  
  def nested_function():
    print("I'm inner")
    
# Functions can be returned from other functions 
def outer_function():
  print("I'm outer")\
  
  def nested_function():
    print("I', inner")
    
  return nested_function


