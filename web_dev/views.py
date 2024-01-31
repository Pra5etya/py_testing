from flask import render_template
from web_dev import app

@app.route('/')
def index():
    return render_template('index.html', title = 'Home', content = 'Hello, World!')