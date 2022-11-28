import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="1726354",
                        host="localhost",
                        port="5432")

cursor=conn.cursor()

@app.route('/', methods=['GET'])
def index():
    return redirect("/login/")

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            if (not username) or (not password): # if empty
                return render_template('empty_error.html')
            try: # try if user does not exist in db
                cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
                records = list(cursor.fetchall())
                return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
            except:
                return render_template('not_exist_error.html')
        elif request.form.get("signup"): # choose to sign up
            return redirect("/sign-up/")
    return render_template('login.html')

@app.route('/sign-up/', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        if (not name.replace(" ", "")) or (not login.replace(" ", "")) or (not password.replace(" ", "")): # empty name/login/password
            return render_template('signup_name_error.html')
        elif not name.replace(" ", "").isalpha(): # numbers in name
            return render_template('signup_numbers_error.html')
        if login:
            cursor.execute('SELECT * FROM service.users')
            rows = cursor.fetchall()
            for row in rows:
                if login == row[2]:
                    return render_template('signup_name_error.html')
        cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
        conn.commit()
        return redirect("/login/")
    return render_template('signup.html')

