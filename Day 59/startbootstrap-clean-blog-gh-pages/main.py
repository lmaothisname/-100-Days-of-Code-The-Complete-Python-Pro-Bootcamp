from flask import Flask, render_template
import requests
app = Flask(__name__)
blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
@app.route("/")
def main():
  all_posts = requests.get(blog_url).json()
  return render_template("index.html", all_posts=all_posts)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/home")
def home():
  all_posts = requests.get(blog_url).json()
  return render_template("index.html", all_posts=all_posts)

@app.route("/post/<int:post_id>")
def get_post(post_id):
  all_posts = requests.get(blog_url).json()
  post = next((p for p in all_posts if p["id"] == post_id), None)
  return render_template("post.html", post=post)
if __name__ == "__main__":
  app.run(debug=True)
  