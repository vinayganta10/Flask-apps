from flask import Flask,g
from sqlProject import pages
from flask_mysqldb import MySQL

def create_app():
    app = Flask(__name__)

    app.secret_key='vinay'

    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='1234'
    app.config['MYSQL_DB']='customers'
    
    mysql = MySQL(app)

    app.register_blueprint(pages.bp)

    @app.before_request
    def before_request():
        g.mysql=mysql 
           
    return app