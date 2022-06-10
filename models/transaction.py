class Transaction:
    def __init__(self, amount, merchant, tag, user, id=None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.user = user
        self.id = id
