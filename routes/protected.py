from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, Role

protected = Blueprint('protected', __name__)

@protected.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])
    role = Role.query.get(user.role_id)

    if 'view_protected' not in role.permissions.split(','):
        return jsonify({'message': 'Permission denied'}), 403

    return jsonify({'message': 'Welcome to the protected route'}), 200
