import os
import sys
import inspect
from flask import request, jsonify
from app import app

curr_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(curr_dir)
# Setting src module on the system path
sys.path.insert(0, parent_dir)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "OK"}), 200



