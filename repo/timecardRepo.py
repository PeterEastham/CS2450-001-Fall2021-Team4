"""
Handles the Timecard "Repository", which is really a CSV
"""
from model import Timecard

#TODO: Parse File
class TimeCardRepo():

    def __init__(self, resourcesString=".//resources//timecards.csv"):
        self.timecards = []
        pass


    def get_one_by_id(self, id):
        for timecard in self.timecards:
            if timecard.id == id:
                return timecard

        return None

    def get_all(self):
        return self.timecards

    def delete_one_by_id(self, id):
        for timecard in self.timecards:
            if timecard.id == id:
                self.timecards.remove(timecard)


    def update_timecard(self, timecard):
        self.delete_one_by_id(timecard.id)
        self.timecards.append(timecard)
