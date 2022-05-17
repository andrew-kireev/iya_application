from flask import Blueprint
from flask import request
from .models.user import User
import json
from db.db import db

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/register', methods=['POST'])
def register():
    user = User()
    json_req = request.json

    user.username = json_req['login']
    user.email = json_req['email']
    user.password = json_req['password']


    print(user)
    db.register_user(user)


    print(json.dumps(user.__dict__))
    return json.dumps(user.__dict__)


