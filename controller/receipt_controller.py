"""
Controller for Receipts
"""

from model.receipt import Receipt
from repo.receiptRepo import ReceiptRepo


def get_receipt(emp_id):
    return ReceiptRepo.get_one_by_id(emp_id)

def change_receipt(emp_id, newShift):
    pass

def get_receipt_total(emp_id):
    return ReceiptRepo.get_one_by_id(emp_id).get_total_costs()
