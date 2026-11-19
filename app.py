import os
from flask import Flask, render_template, request, redirect, url_for, make_response

try:
    import pymysql
    from pymysql.cursors import DictCursor
except ImportError:
    raise ImportError("Установите pymysql: pip install pymysql")

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "admin",
    "database": "flask_auth",
    "charset": "utf8mb4",
    "cursorclass": DictCursor,
    "autocommit": True,
}

class Database:

    def __init__(self, config=None):
        self.config = config or DB_CONFIG
        self.connection = None
        self.cursor = None
        self.last_error = None

    def connect(self):
        if self.connection is None or not self.connection.open:
            self.connection = pymysql.connect(**self.config)
            self.cursor = self.connection.cursor()
        return self

    def close(self):
        if self.cursor:
            try:
                self.cursor.close()
            except Exception:
                pass
            self.cursor = None
        if self.connection:
            try:
                self.connection.close()
            except Exception:
                pass
            self.connection = None

    def get_user(self, username):
        self.last_error = None
        try:
            self.connect()
            self.cursor.execute(
                "SELECT id, user_name, user_password FROM users WHERE user_name = %s",
                (username,),
            )
            user = self.cursor.fetchone()
            return user  # dict или None
        except Exception as e:
            self.last_error = str(e)
            print(f"[Database] Ошибка get_user: {e}")
            return None
        finally:
            self.close()

    def create_user(self, username, password):
        self.last_error = None
        try:
            self.connect()
            self.cursor.execute(
                "INSERT INTO users (user_name, user_password) VALUES (%s, %s)",
                (username, password),
            )
            return True
        except pymysql.err.IntegrityError as e:
            self.last_error = "Пользователь уже существует"
            print(f"[Database] IntegrityError: {e}")
            return False
        except Exception as e:
            self.last_error = str(e)
            print(f"[Database] Ошибка create_user: {e}")
            return False
        finally:
            self.close()


app = Flask(__name__)
app.secret_key = os.urandom(24)
sessions = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Если уже авторизован — показываем страницу с именем
    token = request.cookies.get("auth_token")
    if token and token in sessions:
        return render_template("login.html", username=sessions[token])

    if request.method == "POST":
        try:
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")

            if not username or not password:
                return render_template(
                    "login.html",
                    message="Заполните все поля!",
                )

            db = Database()
            user = db.get_user(username)

            if db.last_error:
                return render_template(
                    "login.html",
                    message=f"Ошибка БД: {db.last_error}",
                )

            if user is None:
                return render_template(
                    "login.html",
                    message="Неверное имя пользователя или пароль!",
                )

            if user["user_password"] != password:
                return render_template(
                    "login.html",
                    message="Неверное имя пользователя или пароль!",
                )

            token = os.urandom(32).hex()
            sessions[token] = user["user_name"]

            response = make_response(redirect(url_for("login")))
            response.set_cookie(
                "auth_token",
                token,
                httponly=True,
                samesite="Lax",
                max_age=3600 * 24,  # 1 день
            )
            return response

        except Exception as e:
            print(f"[login] Ошибка: {e}")
            return render_template(
                "login.html",
                message=f"Ошибка при авторизации: {e}",
            )

    # GET
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")

        if not username or not password:
            return render_template(
                "register.html",
                message="Заполните все поля!",
                error=True,
            )
        if password != confirm:
            return render_template(
                "register.html",
                message="Пароли не совпадают!",
                error=True,
            )

        db = Database()
        ok = db.create_user(username, password)

        if ok:
            return render_template(
                "register.html",
                message="Регистрация успешна! Теперь можно войти.",
            )
        else:
            msg = db.last_error or "Пользователь уже существует или ошибка БД."
            return render_template(
                "register.html",
                message=msg,
                error=True,
            )

    return render_template("register.html")


@app.route("/logout")
def logout():
    token = request.cookies.get("auth_token")
    if token and token in sessions:
        del sessions[token]

    response = make_response(redirect(url_for("index")))
    response.delete_cookie("auth_token")
    return response


@app.route("/test_db")
def test_db():
    db = Database()
    try:
        db.connect()
        db.cursor.execute("SELECT DATABASE()")
        current_db = db.cursor.fetchone()
        db.cursor.execute("SHOW TABLES")
        tables = db.cursor.fetchall()
        db.cursor.execute("SELECT COUNT(*) as cnt FROM users")
        count = db.cursor.fetchone()
        db.close()

        return f"""
        <h2> Подключение к MySQL успешно!</h2>
        <p><b>Текущая БД:</b> {current_db}</p>
        <p><b>Таблицы:</b> {tables}</p>
        <p><b>Пользователей в users:</b> {count}</p>
        <p><a href="/">На главную</a></p>
        """
    except Exception as e:
        return f"""
        <h2> Ошибка подключения к MySQL</h2>
        <pre style="color:red; background:#fee; padding:15px;">{e}</pre>
        <h3>Что проверить:</h3>
        <ol>
            <li>Запущен ли MySQL? (в XAMPP/WAMP — кнопка Start)</li>
            <li>Правильный ли пароль в <code>DB_CONFIG</code> в app.py?</li>
            <li>Создана ли база <code>flask_auth</code>? Выполни schema.sql</li>
        </ol>
        <p><a href="/">На главную</a></p>
        """

"""

CREATE DATABASE IF NOT EXISTS flask_auth;
USE flask_auth;

CREATE TABLE IF NOT EXISTS users (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    user_name     VARCHAR(64)  NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL
);

INSERT INTO users (user_name, user_password)
VALUES ('Vladimir Putin', '123456789');
"""


if __name__ == "__main__":
    print("=" * 50)
    print("Flask + MySQL auth")
    print("Проверка БД: http://127.0.0.1:5000/test_db")
    print("=" * 50)
    app.run(host="127.0.0.1", port=5000, debug=True)
