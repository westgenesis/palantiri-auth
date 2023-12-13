from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.setting import STORAGE_DSN
from flask_jwt_extended import JWTManager


app = Flask("palantiri-auth")
app.config["JSON_AS_ASCII"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = STORAGE_DSN
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
jwt = JWTManager(app)
