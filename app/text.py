from flask import Blueprint

text_blueprint = Blueprint('text_blueprint', __name__)


@text_blueprint.route('/text', methods=['GET', 'POST'])
def text():

    pass