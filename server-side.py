from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Steeler43@localhost/teletalk_user'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = users_db.Column(users_db.TIMESTAMP, default=users_db.func.now())

    def __repr__(self):
        return f'<User {self.username}>'

class TVShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Numeric(3, 2), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<TVShow {self.name}>'

def connect_to_database():
    conn = psycopg2.connect(
        host="localhost",
        database="teletalk_user",
        user="postgres",
        password="Steeler43"
    )
    return conn

def get_all_users():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_user(username, password, email):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
    conn.commit()
    cur.close()
    conn.close()

def get_all_tv_shows():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tv_shows")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_tv_show(name, genre, rating, description):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("INSERT INTO tv_shows (name, genre, rating, description) VALUES (%s, %s, %s, %s)", (name, genre, rating, description))
    conn.commit()
    cur.close()
    conn.close()
