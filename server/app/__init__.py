from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)
CORS(app)

# Update the import statement for the config module

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hari123'
app.config['MYSQL_DB'] = 'project1'

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

# Importing route files
from . import donor_routes, hospital_routes, hospital_login_routes, group_selection