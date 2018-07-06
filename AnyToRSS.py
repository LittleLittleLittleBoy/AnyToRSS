from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager=Manager(app)

from model import model as model
app.register_blueprint(model)

if __name__ == '__main__':
    app.run(debug=True)