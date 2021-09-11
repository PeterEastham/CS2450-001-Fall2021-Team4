from controller.employee_controller import EmployeeController as EC
from controller.payment_controller import PaymentController as PC
from controller.receipt_controller import ReceiptController as RC
from controller.timecard_controller import TimeCardController as TC


EC.start_controller().open_repo(".//resources//employees.csv")
TC.start_controller().open_repo(".//resources//timecards.csv")
RC.start_controller().open_repo(".//resources//receipts.csv")
PC.start_controller()

payment_str = []
