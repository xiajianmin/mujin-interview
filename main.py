from flask import Flask
from flask_restful import Api
from config import Config

from routes import *

app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)

initalizeRoutes(api)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)