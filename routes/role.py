from flask import Blueprint, request, jsonify
from models import db, Role

role_bp = Blueprint('role', __name__)

@role_bp.route('/add_role', methods=['POST'])
def add_role():
    data = request.json
    role_name = data.get('name')
    permissions = ','.join(data.get('permissions', []))

    if Role.query.filter_by(name=role_name).first():
        return jsonify({'message': 'Role already exists'}), 400

    role = Role(name=role_name, permissions=permissions)
    db.session.add(role)
    db.session.commit()

    return jsonify({'message': 'Role created successfully'}), 201
