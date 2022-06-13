from flask import Flask, render_template, request, redirect
from repositories import transaction_repository, tag_repository, merchant_repository
from models.transaction import Transaction

from flask import Blueprint

tasks_blueprint = Blueprint("tasks", __name__)


# INDEX
# GET '/transactions'
@tasks_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("tasks/index.html", all_tasks=transactions)
