from flask import Flask,redirect, render_template, url_for, redirect, request, session
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "Hello"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanentc = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user", usr=user))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    if "user" in session:
        user = session["user"]
        return f"<h1> Hello   {usr}</h1>"
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
