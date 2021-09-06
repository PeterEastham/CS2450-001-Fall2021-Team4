"""
Getters/Setters for the Receipt Data Object
"""
#TODO: To-CSV for the Receipt Database
class Receipt():

    def __init__(self, id):
        self.id = id
        self.costs = []

    def add_costs(self, cost):
        self.costs.append(float(cost))

    def remove_cost(self, cost):
        self.costs.remove(float(cost))

    def get_total_costs(self):
        return sum(self.costs)

    def save_format(self):
        temp = self.id
        for cost in self.costs:
            temp += "," + str(cost)
        return temp + "\n"

    def __str__(self):
        temp = self.id
        for cost in self.costs:
            temp += ", " + str(cost)
        return temp
