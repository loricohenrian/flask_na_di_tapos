from flask import Flask
import mysql.connector

app = Flask(__name__)

app.config['SECRET_KEY'] = '30a9c161f25a46f1d97998c10bd0b1f8'
app.config['WTF_CSRF_ENABLED'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = False 
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  
        database='flask_db'
    )

from finalproject import routes