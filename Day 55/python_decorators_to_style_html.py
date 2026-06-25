from flask import Flask

app = Flask(__name__)  
def make_bold(function):
  def bold_function():
    return f'<h1 style="font-weight: bold;">{function()}</h1>'
  return bold_function

def make_emphasis(function):
  def emphasis_function():
    return f'<em>{function()}</em>'
  return emphasis_function

def make_underlined(function):
  def underlined_function():
    return f'<h1 style="text-decoration: underline;"">{function()}</h1>'
  return underlined_function

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
      '<p>This is a paragraph</p>'\
      '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjQyeG4xYnpqZjJsaGVnOTB2ZThiNHZ2NjRwbDliNmc2cTNwcmJ4NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/relnvfSEa2Qa125uPA/giphy.gif" width=200>'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
  return "Bye!"


if __name__ == "__main__":
  app.run(debug=True)