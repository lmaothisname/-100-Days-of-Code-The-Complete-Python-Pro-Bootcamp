from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.get("/contact")
def contact():
    return render_template("contact.html",msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.post("/contact")
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_num = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # encrypts the connection
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="lmaothiscoach@gmail.com",
                msg=f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone_num}\nMessage: {message}"
            )
        return render_template("contact.html",msg_sent=True)
    else:
        return render_template("contact.html",msg_sent=False)
if __name__ == "__main__":
    app.run(debug=True, port=5001)
