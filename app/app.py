from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)

# Konfigurace SQLite databáze
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import modelů
from models import User

# Vytvoření databázových tabulek
@app.before_first_request
def create_tables():
    db.create_all()

# Hlavní stránka
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
