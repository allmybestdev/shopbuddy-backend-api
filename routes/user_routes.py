from flask import Blueprint, request, jsonify
from models import db, Users, users_schema, users_schema

users = Blueprint('users', __name__)

@users.route('/api/users', methods=['GET'])
def get_users():
    all_users = Users.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@users.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    user = Users.query.get(id)
    if user:
        return users_schema.jsonify(user)
    return jsonify({"message": "사용자를 찾을 수 없습니다"}), 404

@users.route('/api/users', methods=['POST'])
def add_user():
    user_nm = request.json['user_nm']
    chrome_extention_uuid_id = request.json.get('chrome_extention_uuid_id')  # optional
    
    new_user = Users(
        user_nm=user_nm,
        chrome_extention_uuid_id=chrome_extention_uuid_id
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return users_schema.jsonify(new_user) 