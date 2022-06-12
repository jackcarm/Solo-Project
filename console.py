import pdb
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag


import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

merchant1 = Merchant("Tesco")
merchant_repository.save(merchant1)
merchant2 = Merchant("Apple Store")
merchant_repository.save(merchant2)
merchant3 = Merchant("Starbucks")
merchant_repository.save(merchant3)

tag1 = Tag("Steak", merchant1)
tag_repository.save(tag1)
tag2 = Tag("iPhone", merchant2)
tag_repository.save(tag2)
tag3 = Tag("Coffee", merchant3)
tag_repository.save(tag3)

transaction1 = Transaction(7.00, merchant1, tag1)
transaction_repository.save(transaction1)
transaction2 = Transaction(800.00, merchant2, tag2)
transaction_repository.save(transaction2)
transaction3 = Transaction(2.50, merchant3, tag3)
transaction_repository.save(transaction3)

transaction_repository.select_all


pdb.set_trace()
