# Andrew Shen, 08/24/2022

class Transaction:
    """
    Class for "Transaction" object definition, each row in expense report is one transaction
    """
    amount = 0
    ref_num = 0
    transact_date = ""
    post_date = ""
    info = ""

    def __init__(self, amount, ref_num, transact_date, post_date, info):
        self.amount = amount
        self.ref_num = ref_num
        self.transact_date = transact_date
        self.post_date = post_date
        self.info = info
