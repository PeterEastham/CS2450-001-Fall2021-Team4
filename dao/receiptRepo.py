
from model import Receipt

class ReceiptRepo():

    def __init__(self, resourceString=".//resources//receipts.csv"):
        self.receipts = []
        pass

    def get_one_by_id(self, id):
        for receipt in receipts:
            if receipt.id == id:
                return receipt
        return None

    def get_all(self):
        return self.receipts

    def delete_one_by_id(self, id):
        for receipt in receipts:
            if receipt.id == id:
                self.receipts.remove(receipt)

    def update_receipt(self, receipt):
        self.delete_one_by_id(receipt.id)
        self.receipts.append(receipt)
