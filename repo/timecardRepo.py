"""
Handles the Timecard "Repository", which is really a CSV
"""
from model.timecard import Timecard
#Might be able to merge with receipt?
class TimeCardRepo():

    def __init__(self, resourcesString=".//resources//timecards.csv"):
        self.repoPath = resourcesString
        self.timecards = []
        self.__load_repo()
        #self.type = Enum.Payment_Type(TimeCard/Receipt)

    def __load_repo(self):
        with open(self.repoPath, 'r') as repo:
            for line in repo:
                broken = line.split(",")
                emp_id = broken[0]
                broken.pop(0)
                self.__add_one(emp_id, broken)

    #See notes for receipt, but the list should be handled by the TimeCard object.
    def __add_one(self, id, hours_as_list):
        constr = Timecard(id)
        for hours in hours_as_list:
            constr.add_hours(hours)
        self.timecards.append(constr)


    def get_one_by_id(self, id):
        for timecard in self.timecards:
            if timecard.id == id:
                return timecard
        return None #Raise Exception?

    #Debatable function
    def get_all(self):
        return self.timecards

    #Delete might get swapped by archive?
    def delete_one_by_id(self, id):
        for timecard in self.timecards:
            if timecard.id == id:
                self.timecards.remove(timecard)

    #Assume no ID collision, should only be called from the EmployeeController
    def update_timecard(self, timecard):
        self.delete_one_by_id(timecard.id)
        self.timecards.append(timecard)
