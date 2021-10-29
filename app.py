from flask import Flask, request, session, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "1c0acd1d7fef474eafc15dee4c6687de"


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/users")
def list_users():
    user_type = session.get("user_type")
    return user_type or ""

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)