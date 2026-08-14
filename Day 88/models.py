from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column
from sqlalchemy import Integer, String ,Boolean , Float

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///huelocals.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# TABLE 1: Specialty Coffee Places
class CoffeePlace(db.Model):
  __tablename__ = "coffee_places"
  
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
  location: Mapped[str] = mapped_column(String(250), nullable=False)
  img_url: Mapped[str] = mapped_column(String(500), nullable=False)
  map_url: Mapped[str] = mapped_column(String(500), nullable=False)
  type: Mapped[str] = mapped_column(String(10), nullable=False)
  
  # Operating Hours
  open_time: Mapped[str] = mapped_column(String(50), default="07:00")
  close_time: Mapped[str] = mapped_column(String(50), default="22:30")
  
  # Atmosphere / Vibe
  vibe: Mapped[str] = mapped_column(String(100), default="Chill & Chat")
  # Options: "Work & Study", "Chill & Chat", "Versatile / Both"
  
  # Coffee details
  specialty_brew: Mapped[str] = mapped_column(String(100), nullable=False)
  coffee_price: Mapped[str] = mapped_column(String(50), nullable=False)
  coffee_rating: Mapped[float] = mapped_column(Float, default=5.0)
  
  # Amenities
  has_sockets: Mapped[bool] = mapped_column(Boolean, default=True)
  has_wifi: Mapped[bool] = mapped_column(Boolean, default=True)
  open_late: Mapped[bool] = mapped_column(Boolean, default=False)
  description: Mapped[str] = mapped_column(String(500), nullable=True)
  
  def to_dict(self):
    return {col.name : getattr(self, col.name) for col in self.__table__.columns}

# TABLE 2: Food & Delicacy Places
class FoodPlace(db.Model):
  __tablename__ = "food_places"
  
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
  location: Mapped[str] = mapped_column(String(250) , nullable=False)
  img_url: Mapped[str] = mapped_column(String(500), nullable=False)
  map_url: Mapped[str] = mapped_column(String(500), nullable=False)
  type: Mapped[str] = mapped_column(String(10), nullable=False)
  
  # Operating Hours
  open_time: Mapped[str] = mapped_column(String(50), default="07:00")
  close_time: Mapped[str] = mapped_column(String(50), default="21:00")
  menu_by_session: Mapped[str] = mapped_column(String(100), default="morning")
  
  # Delicacy attributes
  signature_dish: Mapped[str] = mapped_column(String(200), nullable=False)
  delicacy_price: Mapped[str] = mapped_column(String(50), nullable=False)
  food_rating: Mapped[float] = mapped_column(Float, default=5.0)
  
  description: Mapped[str] = mapped_column(String(500), nullable=True)
  def to_dict(self):
    return {col.name: getattr(self, col.name) for col in self.__table__.columns}

with app.app_context():
    db.create_all()

with app.app_context():
        db.create_all()
    
        # Tự động nạp mẫu 1 quán Cà phê nếu bảng rỗng
        if not CoffeePlace.query.first():
            cafe1 = CoffeePlace(
                name="Cà Phê Mắt Biếc",
                location="66 Bao Vinh, Hóa Châu, TP. Huế",
                img_url="https://mia.vn/media/uploads/blog-du-lich/Den-tiem-ca-phe-Mat-Biec-de-ngam-nhin-can-nha-cua-Ha-Lan-01-1650991808.jpg",
                map_url="https://maps.app.goo.gl/My4EmWDAziAUrb2q6",
                type="coffee",
                open_time="06:00",
                close_time="19:00",
                vibe="Vintage",
                specialty_brew="Cà phê muối béo ngậy",
                coffee_price="15.000đ - 45.000đ",
                coffee_rating=4.8,
                has_sockets=True,
                has_wifi=True,
                open_late=False,
                description="Quán cà phê bối cảnh phim Mắt Biếc tại phố cổ Bao Vinh."
            )
            db.session.add(cafe1)

        # Tự động nạp mẫu 1 quán Ăn nếu bảng rỗng
        if not FoodPlace.query.first():
            food1 = FoodPlace(
                name="Bún Bò Hẻm Hùng Vương",
                location="Kiệt 29 Hùng Vương, TP. Huế",
                img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3qhwSlder6_JhWLQFyydpGSUVbSFp3skxks86PRCm9A&s",
                map_url="https://maps.app.goo.gl/mVeo2pLNmkC2JTrH7",
                type="food",
                open_time="07:00",
                close_time="09:00",
                menu_by_session="morning",
                signature_dish="Bún bò giò & Chả cua quết tay",
                delicacy_price="40.000đ - 70.000đ",
                food_rating=4.9,
                description="Bún bò thơm lừng đậm đà chuẩn vị Huế."
            )
            db.session.add(food1)

        db.session.commit()
        
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/hue")
def hue():
  category = request.args.get("category", "all")
  coffee = db.session.execute(db.select(CoffeePlace)).scalars().all()
  food = db.session.execute(db.select(FoodPlace)).scalars().all()
  return render_template("hue.html", all_coffee=coffee, all_food=food, current_category=category)

if __name__ == "__main__":
  app.run(debug=True, port=5003)