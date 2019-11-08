from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("mainpage.html")

@app.route("/index")
def index():
	return "Hello, world!"

@app.route("/<string:name>")
def hello(name):
	return f"Hello, {name}!"

# @app.route("/graph")
# def graph():

# @app.route("/title_show", methods=["GET","POST"])
# def title_show():

if __name__ == '__main__':
	app.run(debug=True)