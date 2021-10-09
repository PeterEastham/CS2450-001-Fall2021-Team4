"""
Controller for Receipts
See - timecard_controller for potential ideas
"""

from model.receipt import Receipt
from repo.receiptRepo import ReceiptRepo
from service.file_helper import FileHelper

class ReceiptController():
    _ReceiptRepo = None
    _ReceiptInstance = None
    _FileHelper = None

    @staticmethod
    def start_controller():
        if ReceiptController._ReceiptInstance == None:
            ReceiptController()
        return ReceiptController._ReceiptInstance

    @staticmethod
    def get_controller():
        if ReceiptController._ReceiptInstance != None:
            return ReceiptController._ReceiptInstance
        else:
            raise Exception("Start the Controller first")

    @staticmethod
    def stop_controller():
        if ReceiptController._ReceiptInstance != None:
            object = ReceiptController._ReceiptInstance
            object._ReceiptRepo.save_repo()
            object._ReceiptRepo = None
            ReceiptController._ReceiptInstance = None

    def __init__(self):
        if ReceiptController._ReceiptInstance != None:
            raise Exception("This class is a singleton")
        else:
            ReceiptController._ReceiptInstance = self
            self._FileHelper = FileHelper.get_helper()

    def open_repo(self, relativePath):
        if self._ReceiptRepo != None:
            raise Exception("Only one Receipt Database may be open!")
        else:
            repoPath = self._FileHelper.get_adjusted_path("./resources/receipts.csv")
            self._ReceiptRepo = ReceiptRepo(repoPath)

    def close_repo(self):
        if self._ReceiptRepo == None:
            self.__no_receipt_repo()
        else:
            self._ReceiptRepo.save_repo()
            self._ReceiptRepo = None

    def get_receipt(self, emp_id):
        return self._ReceiptRepo.get_one_by_id(emp_id)

    def update_receipt(self, changed_receipt):
        self._ReceiptRepo.update_object(changed_receipt)

    def add_receipt(self, new_receipt):
        self._ReceiptRepo.update_object(new_receipt)

    def get_receipt_total(self, emp_id):
        if self._ReceiptRepo == None:
            self.__no_receipt_repo()

        receipt = self._ReceiptRepo.get_one_by_id(emp_id)
        if receipt == None:
            return 0

        return receipt.get_total_costs()

    def clear_one_receipt(self, emp_id):
        self._ReceiptRepo.delete_one_by_id(emp_id)

    #Need to inject this into each function. Can we make a header do that for us?
    def __no_receipt_repo(self):
        raise Exception("You need to open a Repository before using this!")
