from flask import Flask

app = Flask(__name__)  

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
      '<p>This is a paragraph</p>'\
      '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjQyeG4xYnpqZjJsaGVnOTB2ZThiNHZ2NjRwbDliNmc2cTNwcmJ4NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/relnvfSEa2Qa125uPA/giphy.gif" width=200>'

@app.route("/bye")
def bye():
  return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
  return f"Hello there {name}, you are {number}!"

if __name__ == "__main__":
  app.run(debug=True)