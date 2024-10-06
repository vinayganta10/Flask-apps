from flask import url_for,Blueprint,render_template,g,request,session,redirect
import re
import MySQLdb.cursors

bp = Blueprint("pages",__name__)

@bp.route('/')
def home():
    return render_template('base.html')

@bp.route('/login',methods=['GET','POST'])
def login():
    mysql = g.mysql
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM data where username = % s and password = %s' ,(username, password, ))
        data = cursor.fetchone()
        if data:
            session['loggedin']=True
            session['id']=data['id']
            session['username']=data['username']
            msg = "Logged in successfully"
            return render_template('base.html',msg=msg)
        else:
            msg = 'Incorrect username or password'
    return render_template('login.html',msg=msg)

@bp.route('/register',methods=['GET','POST'])
def register():
    mysql = g.mysql
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('insert into data VALUES (NULL,% s,% s,% s)' ,(username,password,email, ))
        mysql.connection.commit()
        msg = "You have successfully inserted"
    else:
        msg="please fill all the details"
    return render_template('register.html',msg=msg)

@bp.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    return redirect(url_for('pages.login'))