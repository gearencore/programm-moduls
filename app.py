
import os
import webbrowser
from threading import Timer

from flask import Flask, render_template, request



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR
)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if email and password:
            message = "Форма входа отправлена!"
        else:
            message = "Заполните все поля!"

    return render_template(
        "login.html",
        message=message
    )



@app.route("/register", methods=["GET", "POST"])
def register():

    message = ""

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not email or not password or not confirm_password:
            message = "Заполните все поля!"

        elif password != confirm_password:
            message = "Пароли не совпадают!"

        else:
            message = "Форма регистрации отправлена!"

    return render_template(
        "register.html",
        message=message
    )



if __name__ == "__main__":

    print("Папка проекта:", BASE_DIR)
    print("Папка HTML:", TEMPLATE_DIR)
    print("Папка HTML существует:", os.path.exists(TEMPLATE_DIR))

    Timer(
        1,
        lambda: webbrowser.open("http://127.0.0.1:5000/")
    ).start()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )

