# python decorators is a function that wraps another function to add or modify functionality
# running code before,after, or around the original, without editing it.
import time

def delay_decorator(function):
  def wrapper_function():
    time.sleep(2)
    function()
  return wrapper_function

@delay_decorator
def say_hello():
  print("Hello")
  
@delay_decorator
def say_bye():
  print("Bye")

def say_greeting():
  print("How are you?")
  
decorated_function = delay_decorator(say_greeting)
decorated_function()