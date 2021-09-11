"""
Handles the Receipt "Repository", which is really a CSV
"""
from model.receipt import Receipt

#TODO: Parse File
class ReceiptRepo():

    def __init__(self, resourceString=".//resources//receipts.csv"):
        self.receipts = []
        self.repoPath = resourceString
        self.__load_repo()


    def __load_repo(self):
        with open(self.repoPath, 'r') as repo:
            for line in repo:
                broken = line.split(",")
                emp_id = broken[0]
                broken.pop(0)
                self.__add_one(emp_id, broken)

    def __add_one(self, id, costs_as_list):
        constr = Receipt(id)
        for cost in costs_as_list:
            constr.add_costs(cost)
        self.receipts.append(constr)

    def get_one_by_id(self, id):
        for receipt in self.receipts:
            if receipt.id == id:
                return receipt
        print(f"Failed to find: {id}")
        return None

    def get_all(self):
        return self.receipts

    def delete_one_by_id(self, id):
        for receipt in self.receipts:
            if receipt.id == id:
                self.receipts.remove(receipt)

    def update_receipt(self, receipt):
        self.delete_one_by_id(receipt.id)
        self.receipts.append(receipt)

    def save_repo(self):
        pass
