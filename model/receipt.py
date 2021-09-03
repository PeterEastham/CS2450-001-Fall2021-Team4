

class Receipt():

    def __init__(self, id, costs):
        self.id = id
        self.costs = costs

    def add_costs(self, cost):
        self.costs.append(cost)

    def remove_cost(self, cost):
        self.costs.remove(cost)

    def get_total_costs(self):
        return sum(self.costs)
