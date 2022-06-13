from flask import Flask, render_template, request, redirect
from repositories import transaction_repository, tag_repository, merchant_repository
from models.transaction import Transaction

from flask import Blueprint

transaction_blueprint = Blueprint("transaction", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/transactions'
@transaction_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", all_transactions=transactions)


# NEW
# GET '/transactions/new'
@transaction_blueprint.route("/transactions/new")
def new_transaction():
    return render_template("transactions/new.html")


# CREATE
# POST '/transactions'
@transaction_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    amount = request.form["amount"]
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(merchant, tag, amount)
    transaction_repository.save(transaction)
    return redirect("/transactions")


# SHOW
# GET '/transactions/<id>'
@transaction_blueprint.route("/transactions/<id>")
def show_transactions(id):
    transaction = transaction_repository.select(id)
    return render_template("transactions/show.html", transaction=transaction)


# EDIT
# GET '/transactions/<id>/edit'
@transaction_blueprint.route("/transaction/<id>/edit", methods=["GET"])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchant = merchant_repository.select_all()
    tag = tag_repository.select_all()
    return render_template(
        "transactions/edit.html",
        transaction=transaction,
        merchant=merchant,
        tag=tag,
    )


# UPDATE
# PUT '/transactions/<id>'
@transaction_blueprint.route("/transaction/<id>", methods=["POST"])
def update_transaction(id):
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    amount = request.form["amount"]
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select_all(tag_id)
    transaction = Transaction(merchant, tag, amount, id)
    transaction_repository.update(transaction)
    return redirect("/tasks")


# DELETE
# DELETE '/transactions/<id>'
@transaction_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")
