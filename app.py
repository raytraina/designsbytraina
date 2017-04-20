from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/technologies')
def technologies():
    return render_template("technologies.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")



if __name__ == '__main__':

    app.run(port=5000, debug=False)
    # app.run(host="0.0.0.0", port=5000, debug=False)
    # app.run(debug=True, host='0.0.0.0', port=5000)