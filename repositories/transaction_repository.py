from db.run_sql import run_sql

from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository


def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag_id, amount) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.tag.id, transaction.amount]
    results = run_sql(sql, values)
    id = results[0]["id"]
    transaction.id = id
    return transaction


def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        tag = tag_repository.select(row["tag_id"])
        merchant = merchant_repository.select(row["merchant_id"])
        transaction = Transaction(row["amount"], merchant, tag, row["id"])
        transactions.append(transaction)
    return transactions


def select(id):

    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = merchant_repository.select(result["merchant_id"])
    tag = tag_repository.select(result["tag_id"])
    transaction = Transaction(merchant, tag, result["amount"], result["id"])
    return transaction


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(transaction):
    sql = "UPDATE transactions SET (amount, merchant_id, tag_id) = (%s, %s, %s) WHERE id = %s"
    values = [
        transaction.amount,
        transaction.merchant.id,
        transaction.tag.id,
        transaction.id,
    ]
    run_sql(sql, values)


def total_amount():
    total = []

    sql = "SELECT amount FROM transactions"
    results = run_sql(sql)
    for row in results:
        amount = row["amount"]
        total.append(amount)
    return sum(total)
