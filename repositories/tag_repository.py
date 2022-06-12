from db.run_sql import run_sql

from models.tag import Tag
from models.transaction import Transaction


def save(tag):
    sql = "INSERT INTO tags (item) VALUES (%s) RETURNING *"
    values = [tag.item]
    results = run_sql(sql, values)
    id = results[0]["id"]
    tag.id = id
    return tag


def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row["item"], row["id"])
        tags.append(tag)
    return tags


def select(id):
    user = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result["item"], result["id"])
    return tag


def delete_all():
    sql = "DELETE  FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(tag):
    sql = "UPDATE tags SET (item) = (%s) WHERE id = %s"
    values = [tag.item, tag.id]
    run_sql(sql, values)


def transaction(tag):
    transactions = []

    sql = "SELECT * FROM transactions WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)

    for row in results:
        transaction = Transaction(
            row["amount"], row["merchant_id"], row["tag_id"], row["id"]
        )
        transaction.append(transaction)
    return transactions
