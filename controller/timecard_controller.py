"""
Handles Time Card Operations.

Very similar to Receipt Controller
Potential to combine with Receipt Controller
"""
from repo.timecardRepo import TimeCardRepo
from service.file_helper import FileHelper

class TimeCardController():
    _TimeCardRepo = None
    _TimeCardInstance = None
    _FileHelper = None

    @staticmethod
    def start_controller():
        if TimeCardController._TimeCardInstance == None:
            TimeCardController()
        return TimeCardController._TimeCardInstance

    @staticmethod
    def get_controller():
        if TimeCardController._TimeCardInstance != None:
            return TimeCardController._TimeCardInstance
        else:
            raise Exception("Start the Controller first")

    @staticmethod
    def stop_controller():
        if TimeCardController._TimeCardInstance != None:
            object = TimeCardController._TimeCardInstance
            object._TimeCardRepo.save_repo()
            object._TimeCardRepo = None
            TimeCardController._TimeCardInstance = None


    def __init__(self):
        if TimeCardController._TimeCardInstance != None:
            raise Exception("This class is a singleton")
        else:
            TimeCardController._TimeCardInstance = self
            self._FileHelper = FileHelper.get_helper()

    def get_timecard(self, emp_id):
        return self._TimeCardRepo.get_one_by_id(emp_id)

    def get_total_hours(self, emp_id):
        return self._TimeCardRepo.get_one_by_id(emp_id).get_total_hours()

    def update_timecard(self, changed_timecard):
        self._TimeCardRepo.update_object(changed_timecard)

    def add_timecard(self, new_timecard):
        self._TimeCardrepo.update_object(new_timecard)

    def clear_one_timecard(self, timecard_id):
        self._TimeCardRepo.delete_one_by_id(timecard_id)

    def open_repo(self, relativePath):
        if self._TimeCardRepo != None:
            raise Exception("Only one Receipt Database may be open!")
        else:
            repoPath = self._FileHelper.get_adjusted_path("./resources/timecards.csv")
            self._TimeCardRepo = TimeCardRepo(repoPath)

    def close_repo(self):
        if self._TimeCardRepo == None:
            self.__no_timecard_repo()
        else:
            self._TimeCardRepo.save_repo()
            self._TimeCardRepo = None

    def __no_timecard_repo(self):
        raise Exception("You must open the Repository first!")
