from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form.get("search")
        result = f"You searched for: {user_input}"

    return render_template("index.html", result=result)