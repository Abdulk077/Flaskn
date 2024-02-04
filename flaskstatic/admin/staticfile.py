# custom css images and java script
from flask import Flask, render_template, redirect, url_for
from admin.second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")

@app.route("/")
def test():
    return "<h1>  t </h1> "

if __name__ == "__main__":

    app.run(debug=True)

