# # Plik główny

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Konfiguracja połączenia z bazą danych SQL
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/chef_database'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Endpoint testowy
# @app.route('/')
# def home():
#     return "Chef app is running!"

# if __name__ == '__main__':
#     app.run(debug=True)

## localhost:5000/get_recipes
from flask import Flask, request, jsonify
from config import app, db
from models import Recipe


@app.route('/get_recipes', methods=['GET']) #decorator
def get_recipes():
    recipes = Recipe.query.all()
    json_recipies= list(map(lambda recipe: recipe.to_json(), recipes))#new list with json objects
    return jsonify({'recipies': json_recipies})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)