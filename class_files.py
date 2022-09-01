# Andrew Shen, 08/24/2022

class Transaction:
    """
    Class for "Transaction" object definition, each row in expense report is one transaction
    """
    transact_date = ""
    post_date = ""
    info = ""
    ref_num = 0
    amount = 0

    def __init__(self, transact_date, post_date, info, ref_num, amount):
        self.transact_date = transact_date
        self.post_date = post_date
        self.info = info
        self.ref_num = ref_num
        self.amount = amount

    def print_transaction(self):
        """
        Prints transaction info in block format (5 lines)
        """
        print("Transaction Date: %s\n"
              "Post Date: %s\n"
              "Transaction Info: %s\n"
              "Reference Number: %s\n"
              "Amount: %s" % (self.transact_date, self.post_date, self.info, self.ref_num, self.amount))

    def print_transaction_short(self):
        """
        Prints transaction info in condensed format (1 line)
        """
        print("%s\t%s\t%s\t%s\t%s" % (self.transact_date, self.post_date, self.info, self.ref_num, self.amount))
