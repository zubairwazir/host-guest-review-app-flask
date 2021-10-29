from flask import Flask, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "1c0acd1d7fef474eafc15dee4c6687de"


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Login/Register Template"


@app.route("/register", methods=["POST"])
def register():
    return "Register Guest/Host"


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json(force=True)
        session["user_type"] = data.get("user_type")
        return data


@app.route("/users")
def list_users():
    user_type = session.get("user_type")
    return user_type or ""


@app.route("/hosts/<host_id>/review", methods=["POST"])
def post_review_about_host(host_id):
    return "Post Review About Hosts!"


@app.route("/guests/<guest_id>/review", methods=["POST"])
def post_review_about_guest(guest_id):
    return "Post Review About Guest!"
