from flask import request, jsonify
from app import app


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "OK"}), 200


@app.route('/categories', methods=['GET'])
def get_all_categories():
    pass



