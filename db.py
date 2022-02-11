#db.py

#!/usr/bin/python

import os
import pymysql.cursors
import mysql.connector
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

mydb = mysql.connector.connect(
  host="34.88.135.61",
  port="3306",
  user="joel",
  password="rAg7vimdiS"
)