from flask import Blueprint, request, jsonify
from models import db, User, Role
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role_name = data.get('role')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    role = Role.query.filter_by(name=role_name).first()
    if not role:
        return jsonify({'message': 'Role does not exist'}), 400

    user = User(username=username, role_id=role.id)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={'id': user.id, 'role': user.role_id})
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401
