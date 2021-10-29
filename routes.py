from flask import Flask

app = Flask(__name__)


@app.get("/")
@app.get("/home")
@app.get("/index")
def home():
    return "Login/Register Template"


@app.post("/register")
def register():
    return "Register Guest/Host"


@app.post("/login")
def login():
    return "Login User"


@app.get("/guests")
def list_guest():
    """
    Guide only `Hosts` to this Route
    """
    return "All Guests are here!"


@app.get("/hosts")
def list_hosts():
    """
    Guide only `Guests` to this Route
    """
    return "All Hosts are here!"


@app.post("/hosts/<host_id>/review")
def post_review_about_host(host_id):
    return "Post Review About Hosts!"


@app.post("/guests/<guest_id>/review")
def post_review_about_guest(guest_id):
    return "Post Review About Guest!"
