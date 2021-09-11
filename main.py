from controller import *

Econ = EC.start_controller()
Pcon = PC.start_controller()
employees = Econ._EmpRepo.get_all_employees()

for emp in employees:
    print(Pcon.get_pay_str(emp.id))
