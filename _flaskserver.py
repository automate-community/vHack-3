from json import dumps

from flask import Flask, request,render_template

from _login import login
from _register import register, checkRegisterByName
from _users import getUsersForAttack

SERVER = Flask(__name__)


@SERVER.route("/")
def serverHome():
    return render_template("home.html")


@SERVER.route("/register", methods=["POST"])
def serverRegister():
    if request.method == "POST":
        return dumps(register(request.form["username"], request.form["password"]))


@SERVER.route("/register/check", methods=["POST"])
def serverCheckRegister():
    if request.method == "POST":
        return dumps(checkRegisterByName(request.form["username"]))


@SERVER.route("/login", methods=["POST"])
def serverLogin():
    if request.method == "POST":
        return dumps(login(request.form["token"], request.form["password"]))


@SERVER.route("/attack", methods=["POST", "GET"])
def serverAttack():
    if request.method == "POST":
        from _attack import attack

        return dumps(attack(request.form["userTK"], request.form["objectiveID"]))

    return getUsersForAttack()[1]
