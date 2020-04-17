from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.debug = True

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/experience.html")
def experience():
	return render_template("experience.html")

@app.route("/about.html")
def about():
	return render_template("about.html")

@app.route("/contact.html")
def contact():
	return render_template("contact.html")

@app.route("/form.html", methods=["POST"])
def form():
	session["names"] = []
	session["emails"] = []
	session["messages"] = []
	name = request.form.get("name")
	session["names"].append(name)

	email = request.form.get("email")
	session["emails"].append(email)

	message = request.form.get("message")
	session["messages"].append(message)

	return render_template("form.html", names=session["names"], emails=session["emails"], messages=session["messages"])