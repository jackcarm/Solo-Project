from flask import Flask, render_template, request, redirect
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from flask import Blueprint

merchant_blueprint = Blueprint("merchant", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/merchants'
@merchant_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", all_merchants=merchants)


# NEW
# GET '/merchants/new'
@merchant_blueprint.route("/merchant/new")
def new_merchant():
    return render_template("merchants/new.html")


# CREATE
# POST '/merchants'
@merchant_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form["name"]
    merchant = merchant(name)
    merchant_repository.save(merchant)
    return redirect("/merchants")


# SHOW
# GET '/merchants/<id>'
@merchant_blueprint.route("/merchant/<id>")
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/show.html", merchant=merchant)


# EDIT
# GET '/merchants/<id>/edit'
@merchant_blueprint.route("/merchant/<id>/edit", methods=["GET"])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant=merchant)


# UPDATE
# PUT '/transactions/<id>'
@merchant_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    merchant = merchant_repository.select_all(name)
    merchant = merchant(name)
    merchant_repository.update(merchant)
    return redirect("/merchants")


# DELETE
# DELETE '/transactions/<id>'
@merchant_blueprint.route("/merchants/<id>/delete", methods=["POST"])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")
