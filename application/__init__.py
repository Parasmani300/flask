from flask import Flask
app=Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from flask import request
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/book'
db=SQLAlchemy(app)

from application import routes
