from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.register_blueprint()

if __name__ == '__main__':
    app.run(debug=True)