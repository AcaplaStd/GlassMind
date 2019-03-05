from flask import Flask
from flask import render_temlate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("html.html")

if __name__ == "__main__":
    app.run()
