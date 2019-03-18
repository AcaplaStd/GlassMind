from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('some_page.html', is_whitemode=False)


@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)
