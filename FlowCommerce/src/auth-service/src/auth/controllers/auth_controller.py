from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token
#from auth.services.auth_service import create_user, authenticate_user
from ..services.auth_service import create_user, authenticate_user
from auth.schemas import UserSchema

auth_bp = Blueprint('auth', __name__)
user_schema = UserSchema()


@auth_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        user_schema.load(data)  # Validação dos dados de entrada
        username = data.get('username')
        password = data.get('password')

        if create_user(username, password):
            return jsonify({"message": "User created successfully"}), 201
        else:
            return jsonify({"message": "User already exists"}), 400
    except ValidationError as err:
        return jsonify(err.messages), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user_schema.load(data)  # Validação dos dados de entrada
        username = data.get('username')
        password = data.get('password')

        if authenticate_user(username, password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    except ValidationError as err:
        return jsonify(err.messages), 400