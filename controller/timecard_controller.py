"""
Handles Time Card Operations.

Very similar to Receipt Controller
"""
from repo.timecardRepo import TimeCardRepo

class TimeCardController():
    _TimeCardRepo = None
    _TimeCardInstance = None

    @staticmethod
    def start_controller():
        if TimeCardController._TimeCardInstance == None:
            TimeCardController()
        return TimeCardController._TimeCardInstance

    def __init__(self):
        if TimeCardController._TimeCardInstance != None:
            raise Exception("This class is a singleton")
        else:
            TimeCardController._TimeCardInstance = self

    def get_timecard(self, emp_id):
        return self._TimeCardRepo.get_one_by_id(emp_id)

    def get_total_hours(self, emp_id):
        return self._TimeCardRepo.get_one_by_id(emp_id).get_total_hours()

    def update_timecard(self, changed_timecard):
        self._TimeCardRepo.update_timecard(changed_timecard)

    def add_timecard(self, new_timecard):
        self._TimeCardrepo.update_timecard(new_timecard)

    def clear_one_timecard(self, timecard_id):
        self._TimeCardRepo.delete_one_by_id(timecard_id)

    def open_repo(self, repoPath):
        if self._TimeCardRepo != None:
            raise Exception("Only one Receipt Database may be open!")
        else:
            self._TimeCardRepo = TimeCardRepo(repoPath)

    def close_repo(self):
        if self._TimeCardRepo == None:
            self.__no_timecard_repo()
        else:
            self._TimeCardRepo.save_repo()
            self._TimeCardRepo = None
