from controller import *
from service.version_handling import class_csv_headers as cch

Econ = EC.start_controller()
Pcon = PC.start_controller()
employees = Econ._EmpRepo.get_all_employees()


with open("payroll.txt", 'w') as payroll:
    pay = []
    for emp in employees:
        pay.append(Pcon.get_pay_str(emp.id))

    payroll.writelines(pay)
