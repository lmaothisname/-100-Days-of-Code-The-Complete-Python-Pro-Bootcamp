from flask import Flask
from random import randint
app = Flask(__name__)  

@app.route("/")
def higher_lower_game():
    return '<h1>Guess a number between 0 and 9</h1>' \
      '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGttN2ExeWdiNWl2bzlrM3M2b3Jsa3pkb3dnaTd5cjlrdW9nbnU1bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Fwnp19AzPOTnKKbgZl/giphy.gif">'

random_number = randint(0,9)
def check_guessNum_decorator(function):
  def wrapper(number):
    if number == random_number:
      return '<h1 style="color: green;">You found me!</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number > random_number:
      return '<h1 style="color: purple;">Too high, try again!</h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
      return '<h1 style="color: red;">Too low, try again!</h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
  return wrapper

@app.route("/<int:number>")
@check_guessNum_decorator
def result(number):
  return "<h1></h1>"
if __name__ == "__main__":
  app.run(debug=True)