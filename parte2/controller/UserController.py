from flask import Blueprint, jsonify
from repository import UserRepository

userController = Blueprint("user", __name__)

userRepository = UserRepository()

@userController.route("/add")
def add_usuario(): 
    return userRepository.add_usuario("Igor", "igor@igor.com")

@userController.route("/ver")
def ver():
    return jsonify(userRepository.buscar_todos_usuarios_json()) 