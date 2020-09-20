from json import dumps

from flask import Flask, request, render_template

from _login import login
from _register import register, checkRegisterByName
from _settings import SETTINGS
from _attack import getAttackList

SERVER = Flask(__name__)


@SERVER.route("/")
def serverHome():
    return render_template("home.html")


@SERVER.route("/register", methods=["POST"])
def serverRegister():
    if request.method == "POST":
        return dumps(register(request.form["userNM"], request.form["userPS"], request.form["userML"]))


@SERVER.route("/register/check", methods=["POST"])
def serverCheckRegister():
    if request.method == "POST":
        return dumps(checkRegisterByName(request.form["userNM"]))


@SERVER.route("/login", methods=["POST"])
def serverLogin():
    if request.method == "POST":
        return dumps(login(request.form["userTK"], request.form["userPS"]))


@SERVER.route("/attack", methods=["POST", "GET"])
def serverAttack():
    if request.method == "POST":
        from _attack import attack

        return dumps(attack(request.form["userTK"], request.form["objectiveID"]))

    return getAttackList()[1]


@SERVER.route("/shop", methods=["POST"])
def serverShop():
    if request.method == "POST":
        from _shop import buy

        return dumps(buy(request.form["userTK"], request.form["abilityNM"]))


@SERVER.route("/menu.<menu>")
def serverMenus(menu: str):
    return dumps(SETTINGS["MENU.{0}".format(menu.upper())] if "MENU.{0}".format(menu.upper()) in SETTINGS else ["Error"])
