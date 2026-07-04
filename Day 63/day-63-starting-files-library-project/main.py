from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import sqlite3
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form.get("name")
        author = request.form.get("author")
        rating = request.form.get("rating")
        new_book = Book(title=book_name, author=author, rating=float(rating))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html")

@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book, book_id)
    if request.method == "POST":
        book.rating  = float(request.form.get("rating"))
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)

