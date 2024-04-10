from flask import Flask, render_template, request

app = Flask(__name__)

# Функция для чтения пользователей из файла log
def read_users():
    users = {}
    with open('log', 'r') as file:
        for line in file:
            username, password = line.strip().split(':')
            users[username] = password
    return users

# Получаем список пользователей из файла
users = read_users()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return "Logged in successfully!"
    else:
        return "Login failed. Please check your username and password."

if __name__ == '__main__':
    app.run(debug=True)


