
import os
import json
import hashlib
import webbrowser
from threading import Timer

from flask import Flask, render_template, request

app = Flask(__name__)

USERS_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "users.json"
)

sessions = {}


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        200000
    )

    return salt.hex() + ":" + hashed.hex()


def check_password(password, stored):
    salt_hex, expected = stored.split(":")
    actual = hash_password(
        password,
        bytes.fromhex(salt_hex)
    )

    return actual == stored


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)


def get_users():
    users = load_users()

    if "Gear" not in users:
        users["Gear"] = hash_password("14526788")
        save_users(users)

    return users


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")

            if not username or not password:
                return render_template(
                    "index.html",
                    error="Заполните все поля!"
                )

            users = get_users()

            if username in users and check_password(
                password, users[username]
            ):
                token = os.urandom(32).hex()
                sessions[token] = username

                response = app.make_response(
                    render_template(
                        "login.html",
                        username=username
                    )
                )

                response.set_cookie(
                    "auth_token",
                    token,
                    httponly=True,
                    samesite="Lax"
                )

                return response

            return render_template(
                "index.html",
                error="Неверное имя пользователя или пароль!"
            )

        except Exception:
            return render_template(
                "index.html",
                error="Ошибка авторизации!"
            )

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            confirm = request.form.get("confirm", "")

            if not username or not password or not confirm:
                return render_template(
                    "register.html",
                    error="Заполните все поля!"
                )

            if password != confirm:
                return render_template(
                    "register.html",
                    error="Пароли не совпадают!"
                )

            if len(password) < 8:
                return render_template(
                    "register.html",
                    error="Пароль должен содержать минимум 8 символов!"
                )

            users = get_users()

            if username in users:
                return render_template(
                    "register.html",
                    error="Пользователь уже существует!"
                )

            users[username] = hash_password(password)
            save_users(users)

            return render_template(
                "index.html",
                success="Регистрация успешна! Теперь войдите."
            )

        except Exception:
            return render_template(
                "register.html",
                error="Ошибка регистрации!"
            )

    return render_template("register.html")


@app.route("/login_page")
def login_page():
    token = request.cookies.get("auth_token")
    username = sessions.get(token)

    if username:
        return render_template(
            "login.html",
            username=username
        )

    return render_template("index.html")


@app.route("/logout")
def logout():
    token = request.cookies.get("auth_token")
    sessions.pop(token, None)

    response = app.make_response(
        render_template("index.html")
    )

    response.delete_cookie("auth_token")

    return response


def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")


if __name__ == "__main__":
    get_users()
    Timer(1.5, open_browser).start()
    app.run(host="127.0.0.1", port=5000, debug=False)
