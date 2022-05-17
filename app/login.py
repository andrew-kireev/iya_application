from flask import Blueprint
from flask import request
from .models.user import User
import json
from db.db import db
import uuid

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    user = User()
    json_req = request.json

    user.username = json_req['login']
    user.password = json_req['password']

    res = db.login_user(user)
    print(res)

    if res[0] == True:
        session = uuid.uuid4().hex
        db.create_session(user, session)
        

    # print(json.dumps(user.__dict__))
    return json.dumps(user.__dict__)


