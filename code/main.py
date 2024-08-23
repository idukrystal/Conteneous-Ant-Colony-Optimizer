import random

class Simulator:
    def __init__(self):
        pass
    
    def simulate_test(self, solution):
        pass


class Solution:
    def __init__(self):
        self.variables = {}
        self.weight = 0
        self.pheromone = 0


## simulation 
parameters = {"a":(1, 5), "b":(1, 10)}
solution_archive_size = 5 * len(parameters)
algorithm_q  = 0.5
solution_archive = []
simulator = Simulator()

def initialize_simulation():
    for i in range(solution_archive_size):
        solution = Solution()
        for parameter in parameters:
            solution.variables[parameter] = random.uniform(*parameters[parameter])
        test_result = simulator.simulate_test(solution)
        solution.pheromone = calculate_pheromone(test_result)
        solution_archive.append(solution)
        modify_weights()


def calculate_pheromone(result):
    return random.random() #implement

def modify_weights():
    reorder_solutions()
    for i in range(len(solution_archive)):
        solution_archive[i].weight = calculate_weight(i)

def reorder_solutions():
    pass

def calculate_weight(rank):
    return random.random() #implement 


def print_solution_archive():
    for solution in solution_archive:
        print(solution.variables, solution.weight, solution.pheromone)

initialize_simulation()
print_solution_archive()
