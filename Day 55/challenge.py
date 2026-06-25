# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
      args_as_string = ', '.join(str(arg) for arg in args)
      print(f"You called {function.__name__}({args_as_string})")
      result = function(*args)
      print(f"It returned: {result}")
      return result
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)