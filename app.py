import uuid

from flask import Flask, session, render_template, request, redirect, flash

from database.guests import guests
from database.hosts import hosts

app = Flask(__name__)
app.config["SECRET_KEY"] = "1c0acd1d7fef474eafc15dee4c6687de"


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    if session.get("user_id"):
        user_type = session.get("user_type")
        if user_type == "guest":
            return render_template("host.html", hosts=hosts)
        elif user_type == "host":
            return render_template("guest.html", guests=guests)
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html", message="must provide username")

        if not request.form.get("name"):
            return render_template("error.html", message="must provide name")

        if not request.form.get("location"):
            return render_template("error.html", message="must provide location")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("error.html", message="must provide password")

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return render_template("error.html", message="must confirm password")

        # Check passwords are equal
        elif not request.form.get("password") == request.form.get("confirmation"):
            return render_template("error.html", message="passwords didn't match")

        new_user = {
            "id": uuid.uuid4().hex,
            "username": request.form.get("username"),
            "name": request.form.get("name"),
            "password": request.form.get("password"),
            "location": request.form.get("location"),
            "rating": [],
            "overall_ratings": None
        }

        user_type = request.form.get("user_type")

        if user_type == "guest":
            guests.append(new_user)
        elif user_type == "host":
            new_user["services"] = request.form.get("services")
            hosts.append(new_user)

        flash('Account created', 'info')

        # Redirect user to login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("error.html", message="must provide username")

        elif not request.form.get("password"):
            return render_template("error.html", message="must provide password")

        username = request.form.get("username")
        password = request.form.get("password")
        user_type = request.form.get("user_type")

        if user_type == "host":
            user = [usr for usr in hosts if usr["password"] == password and usr["username"] == username]
        else:
            user = [usr for usr in guests if usr["password"] == password and usr["username"] == username]

        if not user:
            return render_template("error.html", message="username or password is incorrect. Try again!")

        user = user[0]
        session["user_id"] = user["id"]
        session["username"] = user["username"]
        session["user_type"] = user_type

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # Forget any user ID
    session.clear()

    # Redirect user to login form
    return redirect("/login")


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
