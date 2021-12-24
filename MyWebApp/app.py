import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database='service_db', user='postgres', password='postgres', host='localhost', port='5432')
cursor = conn.cursor()


def require_form(fields):
    required = 0
    for field in fields:
        if len(field) != 0:
            required = 1

    return required


# def require_form(field_username, field_password):
#     if len(field_username) != 0 and len(field_password) != 0:
#         return 1
#     else:
#         return 0


def check_nickname(data):
    if not data:
        return 0
    else:
        return 1


@app.route('/')
def home():
    return redirect("/login/")


@app.route('/login/', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')

            if require_form([username, password]) == 1:
                cursor.execute('SELECT * FROM service.users WHERE login=%s AND password=%s',
                               (str(username), str(password)))
                records = list(cursor.fetchall())

                if check_nickname(records) == 1:
                    return render_template('account.html',
                                           full_name=records[0][1], username=records[0][2], password=records[0][3])
                else:
                    return '<p>Вас нет в базе данных</p>' + '<p><a href="/login/">Вернуться назад</a></p>'
            else:
                return '<p>Введите логин или пароль<p>' + '<p><a href="/login/">Заново ввести логин и пароль</a></p>'
        elif request.form.get("registration"):
            return redirect("/registration/")


@app.route('/registration/',  methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')

    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('login')
        password = request.form.get('password')

        if require_form([name, username, password]) == 1:
            cursor.execute('SELECT * FROM service.users WHERE login=%s AND password=%s',
                           (str(username), str(password)))
            db_username = list(cursor.fetchall())[0][2]
            print (db_username)
            if db_username != username:
                cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                               (str(name), str(username), str(password)))
                conn.commit()

                return redirect('/login/')
            else:
                return '<p>Такой пользователь уже существует<p>' + '<p><a href="/login/">Заново ввести имя, логин и пароль</a></p>'
        else:
            return '<p>Введите имя, логин или пароль<p>' + '<p><a href="/login/">Заново ввести имя, логин и пароль</a></p>'