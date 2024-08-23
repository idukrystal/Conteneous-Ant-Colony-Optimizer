from data  import test_result_name

class Solution:
    def __init__(self):
        self.variables = {}
        self.weight = 0
        self.pheromone = 0
    def update_pheromone(self, sim_result):
        self.pheromone = (abs(self.test_data[test_result_name] - sim_result)/self.test_data[test_result_name])*100
    def __lt__(self, other):
        return self.pheromone < other.pheromone
    def __le__(self, other):
        return self.pheromone <= other.pheromone
    def __gt__(self, other):
        return self.pheromone > other.pheromome
    def __ge__(self, other):
        return self.pheromone >= other.pheromone
    def __ne__(self, other):
        return self.pheromone != other.pheromone
