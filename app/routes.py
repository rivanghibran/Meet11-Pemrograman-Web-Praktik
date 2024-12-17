from flask import Blueprint, jsonify, request
from . import db
from .models import User

main = Blueprint('main', __name__)

# tampil semua
@main.route('/users', methods=['GET'])
def getall_users():
    users = User.query.all()
    return jsonify(
        [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email
            } for user in users
        ]
    )

# tampil by user id
@main.route('/users/<int:user_id>', methods=['GET'])
def get_users(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    return jsonify({"message": "user not found"},404)

# create user
@main.route('/users/create', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email :
        return jsonify({"message": "name or email are required"})
    
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created", "user" : {"id": new_user.id, "name": new_user.name,"email" : new_user.email }})

@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.query.get (user_id)
    if not user :
        return jsonify({"message": "user not found"},404)

    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    
    
    return jsonify({"message": "User updated", "user" : {"id": user.id, "name": user.name,"email" : user.email }})

@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = request.query.get(user_id)
    if not user :
        return jsonify({"message": "user not found"},404)

    db.session.delete (user)
    db.session.commit ()
    
    
    return jsonify({"message": "User deleted"})