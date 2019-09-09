from flask import Flask, render_template

app = Flask(__name__, template_folder="./templates")


@app.route("/")
def hello():
    return "Hello World"


@app.route("/hallo")

def hallo():
    return render_template("hallo.html", teststring="this will  be put in the template")


if __name__ == "__main__":
    app.run()
