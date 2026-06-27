from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests
app = Flask(__name__)

@app.route("/")
def home():
  ranndom_number = randint(0,100)
  year = datetime.now().year
  return render_template("index.html",num=ranndom_number,year=year)

@app.route("/guess/<name>")
def guess_name(name):
  parameters = {
    "name" : name
  }
  response1 = requests.get(url="https://api.genderize.io",params=parameters)
  response2 = requests.get(url="https://api.agify.io",params=parameters )
  data1 = response1.json()
  data2 = response2.json()
  return render_template("guess.html",name=name,gender=data1["gender"],age=data2["age"])

blog_url="https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(blog_url).json()
@app.route("/blog/<num>")
def blog(num):
  return render_template("blog.html",posts=all_posts)
if __name__ == "__main__":
  app.run(debug=True)