"""
Getters/Setters for the Timecard Data Object.
This class DOES NOT COMPUTE TOTAL HOURS WORKED!
"""
#TODO: To-CSV for Repository
class Timecard():

    def __init__(self, id, hours):
        self.id = id
        self.hours = hours

    def add_hours(self, shift):
        self.hours.append(shift)

    def remove_hour(self, shift):
        self.hours.remove(shift)

    def get_total_hours(self):
        return sum(hours)
