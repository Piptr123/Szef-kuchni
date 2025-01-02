# -*- coding: utf-8 -*-
# filepath: /c:/Users/tomek/source/repos/Szef-kuchni/app.py

from flask import Flask, request, jsonify, Response, render_template
from config import app, db
from models import Recipe
import json

# @app.route('/get_recipes', methods=['GET']) #decorator    
# def get_recipes():
#     recipes = Recipe.query.all()
#     json_recipies = list(map(lambda x: x.to_json(), recipes)) #new list with json objects
#     return jsonify({'recipies': json_recipies})

# -*- coding: utf-8 -*-




@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    json_recipes = list(map(lambda x: x.to_json(), recipes))
    response = app.response_class(
        response=json.dumps({'recipes': json_recipes}, ensure_ascii=False),
        mimetype='application/json; charset=utf-8'
    )
    return response


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)