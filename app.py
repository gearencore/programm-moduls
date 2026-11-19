
import os
import webbrowser
from threading import Timer

from flask import Flask, render_template, request

app = Flask(__name__)

USERNAME = "Gear"
PASSWORD = "14526788"

sessions = set()


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

            if username == USERNAME and password == PASSWORD:
                token = os.urandom(32).hex()
                sessions.add(token)

                response = app.make_response(
                    render_template("login.html", username=username)
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
                error="Произошла ошибка при авторизации!"
            )

    token = request.cookies.get("auth_token")

    if token in sessions:
        return render_template("login.html", username=USERNAME)

    return render_template("index.html")


@app.route("/login_page")
def login_page():
    token = request.cookies.get("auth_token")

    if token in sessions:
        return render_template("login.html", username=USERNAME)

    return render_template("index.html")


@app.route("/logout")
def logout():
    token = request.cookies.get("auth_token")
    sessions.discard(token)

    response = app.make_response(render_template("index.html"))
    response.delete_cookie("auth_token")

    return response


def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")


if __name__ == "__main__":
    Timer(1.5, open_browser).start()
    app.run(host="127.0.0.1", port=5000, debug=False)
