
class Simulator:
    def __init__(self, archive_size):

    def simulate_test(solution):
        pass


class Solution:
    def __init__(self):
        self.variables = {}
        self.weight = 0
        self.pheromone = 0


## simulation 
parameters = {a:(0, 5), b:(2, 6), c:(3, 10)}
solution_archive_size = 5 * len(parameters)
algorithm_q  = 0.5
solution_archive = []
simulator = Simulator()

def initialize_simulation():
    for i in range(solution_archive_size):
        solution = Solution()
        for parameter in parameter:
            solution.variables(parameter) = 5#random(Solution.parameters(parameter)
        test_result = simulator.simulate_test(solution)
        solution.pheromone = calculte_pheromone(test_result)
        solution_archive.append(solution)
        modify_weights()


def calculate_pheromone(result):
    pass

def modify_weights():
    reorder_solutions()
    for i in range(len(solution_archive)):
        solution_archive(i).weight = calculate_weight(i)

def reorder_solutions():
    pass

def calculate_weights(rank):
    pass
