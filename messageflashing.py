from flask import Flask, redirect, render_template, url_for, redirect, request, session, flash
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
        flash("login sussesfully")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in")
            user = session["user"]
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("you are not logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("you have been logged out")
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
