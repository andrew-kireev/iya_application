from flask import Blueprint
from flask import request
from .models.user import User
import json

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    user = User()
    json_req = request.json

    user.login = json_req['login']
    user.password = json_req['password']
    print(json.dumps(user.__dict__))
    return json.dumps(user.__dict__)


