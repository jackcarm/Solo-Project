from db.run_sql import run_sql

from models.merchant import Merchant
from models.transaction import Transaction


def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING *"
    values = [merchant.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    merchant.id = id
    return merchant


def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row["name"], row["id"])
        merchants.append(merchant)
    return merchants


def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result["name"], result["id"])
    return merchant


def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(merchant):
    sql = "UPDATE merchants SET name = %s WHERE id = %s"
    values = [merchant.name, merchant.id]
    run_sql(sql, values)


def transaction(merchant):
    transactions = []

    sql = "SELECT * FROM transactions WHERE merchant_id = %s"
    values = [merchant.id]
    results = run_sql(sql, values)

    for row in results:
        transaction = Transaction(
            row["amount"], row["merchant_id"], row["tag_id"], row["id"]
        )
        transaction.append(transaction)
    return transactions
