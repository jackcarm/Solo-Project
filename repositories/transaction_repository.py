from db.run_sql import run_sql

from models.merchant import Merchant
from models.tag import Tag
from models.user import User
from models.transaction import Transaction
import repositories.user_repository as user_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository


def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id, user_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [
        transaction.amount,
        transaction.merchant.id,
        transaction.tag.id,
        transaction.user.id,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    transaction.id = id
    return transaction


def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row["user_id"])
        tag = tag_repository.select(row["tag_id"])
        merchant = merchant_repository.select(row["merchant_id"])
        transaction = Transaction(row["amount"], merchant, tag, user, row["id"])
        transactions.append(transaction)
    return transactions


def select(id):
    transaction = None
    sql = "SELECT * FROM tranactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result["user_id"])
        tag = tag_repository.select(result["tag_id"])
        merchant = merchant_repository.select(result["merchant_id"])
        transaction = Transaction(result["amount"], merchant, tag, user, result["id"])
    return transaction


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(transaction):
    sql = "UPDATE transactions SET (amount, merchant_id, tag_id, user_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [
        transaction.amount,
        transaction.merchant.id,
        transaction.tag.id,
        transaction.user.id,
        transaction.id,
    ]
    run_sql(sql, values)
