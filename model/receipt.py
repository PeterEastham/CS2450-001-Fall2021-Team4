"""
Timecard and Receipt Data models are almost the same,
Potential area to abstract?
"""
class Receipt():
    #A "Payed on Date" might be useful for tracking purposes.
    def __init__(self, id):
        self.id = id
        self.costs = []

    #Potential for functions like add_costs_as_listlike_str(), or add_costs_from_list()
    def add_costs(self, cost):
        self.costs.append(float(cost))

    #Look into maintaining order?
    def remove_cost(self, cost):
        self.costs.remove(float(cost))

    def get_total_costs(self):
        return sum(self.costs)

    #Mirrors the Employee save_format
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
