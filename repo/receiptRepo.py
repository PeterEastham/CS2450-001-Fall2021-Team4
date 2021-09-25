"""
Handles the Receipt "Repository", which is really a CSV
Data format is really similar to Timecards, potential abstraction?
"""
from model.receipt import Receipt
from repo.baseRepo import BaseCSVRepo

class ReceiptRepo(BaseCSVRepo):

    #We're going to override the original method to avoid the hassle
    #of CSV reading
    def _load_repo(self):
        with open(self.repoPath, 'r') as repo:
            for line in repo:
                broken = line.split(",")
                self.objects.append(self.make_object(broken[0], broken[1:]))

    #TODO put list handling to the receipt model.
    def make_object(self, id, costs_as_list):
        constr = Receipt(id)
        for cost in costs_as_list:
            constr.add_costs(cost)
        return constr

    def save_objects_list(self):
        save_format = []
        sorted_receipt = sorted(self.objects, key=lambda Receipt : Receipt.id)
        for receipt in sorted_receipt:
            save_format.append(str(receipt) + "\n")
        return save_format
