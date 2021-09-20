from controller import *
from service.version_handling import class_csv_headers as cch

Econ = EC.start_controller()
Pcon = PC.start_controller()
employees = Econ._EmpRepo.get_all_employees()


with open("payroll.txt", 'w') as payroll:
    pay = []
    for emp in employees:
        pay_str = Pcon.get_pay_str(emp.id)
        print(pay_str, end='')
        pay.append(pay_str)

    payroll.writelines(pay)
