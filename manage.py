import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    """Render index page."""
    return render_template("index.html")

@app.route('/about')
def about():
    """Render about page."""
    return render_template("about.html")

@app.route('/technologies')
def technologies():
    """Render skills/tools page."""
    return render_template("technologies.html")

@app.route('/projects')
def projects():
    """Render projects page."""
    return render_template("projects.html")

# @app.route('/resume')
# def resume():
#     """Render resume page."""
#     return render_template("resume.html")

@app.route('/contact')
def contact():
    """Render contact page."""
    return render_template("contact.html")



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
