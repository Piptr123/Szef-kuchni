# Plik główny

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfiguracja połączenia z bazą danych SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/chef_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Endpoint testowy
@app.route('/')
def home():
    return "Chef app is running!"

if __name__ == '__main__':
    app.run(debug=True)
