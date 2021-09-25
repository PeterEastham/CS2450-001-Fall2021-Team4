"""
Almost the same as Receipt-See it.
"""

class Timecard():

    def __init__(self, id):
        self.id = id
        self.hours = []

    def add_hours(self, shift):
        self.hours.append(float(shift))

    def remove_hour(self, shift):
        self.hours.remove(float(shift))

    def get_total_hours(self):
        return sum(self.hours)

    def save_format(self):
        temp = self.id
        for hours in self.hours:
            temp += "," + str(hours)
        return temp + "\n"

    def __str__(self):
        temp = self.id
        for hours in self.hours:
            temp += ", " + str(hours)
        return temp
