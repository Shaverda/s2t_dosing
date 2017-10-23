from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)

#mysql configs cuz I don't really care about commiting these :)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'lolol'
app.config['MYSQL_DATABASE_DB'] = 'medications'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

