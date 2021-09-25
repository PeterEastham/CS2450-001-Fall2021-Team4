"""
Handles the Timecard "Repository", which is really a CSV
"""
from model.timecard import Timecard
from repo.baseRepo import BaseCSVRepo
#Might be able to merge with receipt?
class TimeCardRepo(BaseCSVRepo):

    def _load_repo(self):
        with open(self.repoPath, 'r') as repo:
            for line in repo:
                broken = line.split(",")
                self.objects.append(self.make_object(broken[0], broken[1:]))

    def make_object(self, id, hours_as_list):
        constr = Timecard(id)
        for hours in hours_as_list:
            constr.add_hours(hours)
        return constr

    def save_objects_list(self):
        save_format = []
        sorted_timecard = sorted(self.objects, key=lambda TimeCard : TimeCard.id)
        for timecard in sorted_timecard:
            save_format.append(str(timecard) + "\n")
        return save_format
