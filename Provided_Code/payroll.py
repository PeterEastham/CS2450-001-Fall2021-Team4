"""
UVU CS Dept.
CS1410 Project 5Part2 - Employee
Summer1 - 2020



I declare that the following source code was modified solely by me.
I understand that copying any source code verbatim, in whole, constitues cheating
and copying in part requires that I acknowledge the author of the original content.
In this case these presentations are in general authored by Dana Doggett and
Chuck Allison as part of the UVU CS department for instructional purposes.


"""
#todo:

#completed:
# 1. Implement Employee
# 2. Implement Classification and Classification Types
# 3. Implement PaymentMethod and Method Types
# 4. Implement load_employees
# 5. Implement find_employee_by_id
# 6. Implement process_timecards
# 7. Implement process_receipts
# 8. run_payroll
# 9. run main


from abc import ABC, abstractmethod
class Classification(ABC):
    '''from ABS for an abstract class determine how the employee wants to be paid'''

    @abstractmethod
    def get_Pay(self):
        pass

class Hourly(Classification):
    '''employee type'''
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecards = []

    def get_Pay(self):
        '''calculate pay for hourly employee'''
        amount = 0.0
        for timecard in self.timecards:
            amount += timecard * self.hourly_rate
        self.timecards.clear()
        return amount

    def add_Timecard(self, hours):
        '''add some hours to the timecards list'''
        self.timecards.append(hours)


class Salaried(Classification):
    '''employee type'''
    def __init__(self, salary):
        self.salary=salary
    def get_Pay(self):
        '''return pay calculation for Salary employee'''
        return self.salary/24



class Commissioned(Salaried):
    '''employee type'''
    def ___init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def add_Sale(self, receipt):
        '''put receipts in a list'''
        self.receipts.append(receipt)

    def get_Pay(self):
        '''custom pay method'''
        amount = super().get_Pay()
        for receipt in self.receipts:
            amount += receipt * self.commission_rate/ 100
            self.receipts.clear()
            return amount

class Payment_Method(ABC):
    '''abstract PaymentMethod class'''
    def __init__(self, employee):
        self.employee = employee

    @abstractmethod
    def pay(self, amount):
        pass

class Direct(Payment_Method):
    '''employee wants a directdeposit'''
    def __init__(self, employee, route, account):
        super().__init__(employee)
        self.route = route
        self.account=account
    def pay(self, amount):
        with open(pay_log_file, 'a') as plog:#add file to print to.
            print("Transferring", f"{amount:.02f}", "for", self.employee.name, "to", self.account, ": ", self.route, file=plog)

class Mailed(Payment_Method):
    '''employee wants a mailed check'''
    def __init__(self, employee):
        super().__init__(employee)

    def pay(self, amount):
        with open(pay_log_file, 'a') as plog:
            print("Mailing", f"{amount:.02f}", "to", self.employee.name, "at" ,self.employee.address, self.employee.city. self.employee.state, self.employee.zipcode, file=plog)


employees = []
def load_employees():
    '''populate employees list'''
    with open("employees.csv") as femp:
        femp.readline()
        for line in femp:
            data = line.strip().split(",")
            emp = Employee(data[0], data[1], data[2], data[3], data[4], data[5])
            if int(data[6] == 1):
                emp.make_hourly(float(data[9]))
            elif int(data[6] == 2):
                emp.make_salaried(float(data[8]))
            else:
                emp.make_commissioned(float(data[8]), int(data[10]))
        if int(data[7]) == 1:
            emp.direct(data[11], data[12])
        else:
            emp.mailed()
        employees.append(emp)

def find_employee_by_id(emp_id):
    for emp in employees:
        if emp.emp_id == emp_id:
            return emp

def process_timecards():
    with open("timecards.txt") as tfile:
        for line in tfile:
            data = line.strip().split(",")
            emp = find_employee_by_id(data[0])
            if emp != None:
                data.pop(0)
                for timecard in data:
                    emp.classification.add_timecard(float(timecard))
def process_receipts():
    with open("receipts.txt") as rfile:
        for line in rfile:
            data = line.strip().split(",")
            emp = find_employee_by_id(data[0])
            if emp != None:
                data.pop(0)
                for receipt in data:
                    emp.classification.add_Sale(float(receipt))
import os, shutil
pay_log_file = 'paylog.txt'
def run_payroll():
    if os.path.exists(pay_log_file):
        os.remove(pay_log_file)
    for emp in employees:
        emp.pay()


'''
    p5.py: Illustrates the payroll module.
'''

#from payroll import *

def main():
    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()

    # Save copy of payroll file; delete old file
    shutil.copyfile('paylog.txt', 'paylog_old.txt')
    if os.path.exists(pay_log_file):
        os.remove(pay_log_file)

    # Change Karina Gay to Salaried and MailMethod by changing her Employee object:
    emp = find_employee_by_id('688997')
    emp.make_salaried(45884.99)
    emp.mail_method()
    emp.issue_Pay()

    # Change TaShya Snow to Commissioned and DirectMethod; add some receipts
    emp = find_employee_by_id('522759')
    emp.make_commissioned(50005.50, 25)
    emp.direct_method('30417353-K', '465794-3611')
    clas = emp.classification
    clas.add_receipt(1109.73)
    clas.add_receipt(746.10)
    emp.issue_Pay()

    # Change Rooney Alvarado to Hourly; add some hour entries
    emp = find_employee_by_id('165966')
    emp.make_hourly(21.53)
    clas = emp.classification
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    emp.issue_Pay()

if __name__ == '__main__':
    main()
