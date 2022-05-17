from cgitb import text
from flask import Flask
from app.login import users_blueprint
from app.text import text_blueprint
from app.register import register_blueprint

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.register_blueprint(users_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(text_blueprint)

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0')