import datetime
import peewee
from flask import Flask
from flask_json import as_json
from app import app, json, models

''' Create a JSON response '''
@app.route('/', methods=['GET'])
@as_json
def index():
    return dict(status="OK", utc_time=datetime.datetime.utcnow(), time=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

''' Connect to the database before every request '''
@app.before_request
def before_request():
    models.base.database.connect()

''' Close the database connection after every request '''
@app.after_request
def after_request(response):
    models.base.database.close()
    return response

''' In case of 404 error, return JSON with a not found message '''
@app.errorhandler(404)
@as_json
def not_found():
    return dict(code=404, msg="not found"), 404
