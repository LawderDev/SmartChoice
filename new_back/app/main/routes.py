from flask import Blueprint, jsonify, request
from . import main
from app.controllers import user_controller

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_controller.get_user_by_id(user_id)
    if user:
        return jsonify(user.json())
    return jsonify({'error': 'User not found'}), 404

@main.route('/hello', methods=['GET'])
def hello():
    return "Hello World"