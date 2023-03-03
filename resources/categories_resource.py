from flask import request, jsonify
from app import app
from model.categories_model import ExpenseCategoriesModel
from schemas.categories_schema import ExpenseCategoriesSchema

ecs = ExpenseCategoriesSchema(many=True)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "OK"}), 200


@app.route('/categories', methods=['GET'])
def get_all_categories():
    all_categories = ExpenseCategoriesModel.fetch_all()
    if all_categories and all_categories['Items']:
        return ecs.dump(all_categories['Items']), 200
    return jsonify({"message": f"No Expense categories found"}), 404



