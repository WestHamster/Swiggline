import time

# {
#     "status_code": 200/400/500,
#     "status_message": "successful",
#     "message": "Transaction successful"
# }

successfulTxn = {
    "status_code": 200,
    "status_message": "successful",
    "message": "Transaction successful"
}
failedTxn = {
    "status_code": 400,
    "status_message": "failed",
    "message": "Transaction failed"
}


class TransactionStat:
    balAccount = 1000
    transactions = {}

    def __init__(self):
        pass

    def checkTransaction(txnVal):
        """
        :description: checks whether debit or credit
        :return: successful / failed txn
        """
        is_fail = True
        if txnVal != None:
            transaction = txnVal['transaction']
            transactionStatus = False
            if transaction == 'debit':
                transactionStatus = TransactionStat.debitTransaction(txnVal)
            elif transaction == 'credit':
                transactionStatus = TransactionStat.creditTransaction(txnVal)

            if transactionStatus:
                return successfulTxn

        if is_fail:
            return failedTxn

    @staticmethod
    def checkBalance():
        """
        :description: displays the balance amount
        :return:
        """
        print("\n\n\t\tBalance:", TransactionStat.balAccount)

    def debitTransaction(txnVal):
        """
        :param txnVal: contains transaction information
        :return:
        """
        print("\n\n\t\tStarting transaction")
        time.sleep(2)
        TransactionStat.balAccount -= int(txnVal['amount'])
        if TransactionStat.balAccount < 0:
            print("\n\n\t\tCannot process amount as balance is lower than amount")
            return False
        print("\n\n\t\tDebited amount:", txnVal['amount'])
        TransactionStat.transactions.update(txnVal)

        return True

    def creditTransaction(txnVal):
        """
        :param txnVal: contains transaction information
        :return:
        """
        print("\n\n\t\tStarting transaction")
        time.sleep(2)
        if TransactionStat.balAccount + int(txnVal['amount']) > 10000:
            print("\n\n\t\tCannot process amount as balance limit has exceeded!!")
            return False
        TransactionStat.balAccount += int(txnVal['amount'])
        print("\n\n\t\tCredited amount:", txnVal['amount'])
        print("\n\n\t\tNew Balance:", TransactionStat.balAccount)

        return True
