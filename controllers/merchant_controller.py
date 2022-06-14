from flask import Flask, render_template, request, redirect
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from flask import Blueprint

merchant_blueprint = Blueprint("merchants", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/merchants'
@merchant_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants=merchants)


# NEW
# GET '/merchants/new'
@merchant_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html")


# CREATE
# POST '/merchants'
@merchant_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form["name"]
    merchants = Merchant(name)
    merchant_repository.save(merchants)
    return redirect("/merchants")


# SHOW
# GET '/merchants/<id>'
@merchant_blueprint.route("/merchants/<id>")
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/show.html", merchant=merchant)


# EDIT
# GET '/merchants/<id>/edit'
@merchant_blueprint.route("/merchants/<id>/edit", methods=["GET"])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant=merchant)


# UPDATE
# PUT '/merchants/<id>'
@merchant_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    merchant = Merchant(name, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")


# DELETE
# DELETE '/merchants/<id>'
@merchant_blueprint.route("/merchants/<id>/delete", methods=["POST"])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")
