"""
Handles the Receipt "Repository", which is really a CSV
Data format is really similar to Timecards, potential abstraction?
"""
from model.receipt import Receipt

#If we archive receipts, maybe save like time:id:value,value? Then if we try to
#Read it like it's unpaid, we'll get an error.
class ReceiptRepo():

    #Since we might look into archiving the paid Receipts, we'll pass
    #in the repository path.
    def __init__(self, resourceString=".//resources//receipts.csv"):
        self.receipts = []
        self.repoPath = resourceString
        self.__load_repo()

    #Missing bad data handling.
    def __load_repo(self):
        with open(self.repoPath, 'r') as repo:
            for line in repo:
                broken = line.split(",")
                emp_id = broken[0]
                broken.pop(0)
                self.__add_one(emp_id, broken)

    #TODO put list handling to the receipt model.
    def __add_one(self, id, costs_as_list):
        constr = Receipt(id)
        for cost in costs_as_list:
            constr.add_costs(cost)
        self.receipts.append(constr)

    #Archive Repo will need a "get_all_by_id",
    # "get_all_in_range" which return sub lists.
    def get_one_by_id(self, id):
        for receipt in self.receipts:
            if receipt.id == id:
                return receipt
        return None #Raise Execption?

    #def get_count(self)?

    #Debating on allowing this function to exist.
    #When should we get all the receipts? Why do we need them all?
    def get_all(self):
        return self.receipts

    def delete_one_by_id(self, receipt_id):
        for receipt in self.receipts:
            if receipt.id == receipt_id:
                self.receipts.remove(receipt)

    #We assume no id collisions since these are tied to employees.
    def update_receipt(self, receipt):
        self.delete_one_by_id(receipt.id)
        self.receipts.append(receipt)

    def save_repo(self):
        pass
