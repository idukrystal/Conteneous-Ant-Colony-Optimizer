""" Module to handle each new solution discovered by ants. """

import random

# Test model parameters
from src.main.params import parameters

# Name of test's dependent variable(i.e pressure)
from src.main.data  import test_result_name, test_datas

test_data_size = len(test_datas)

class Solution:
    """ Represents a single possible solution. """
    
    def __init__(self):
        """ Object constructor function. """
        
        # Variables:values used to generate solution.
        self.variables = {}

        self.deviation = 0

        # Initialize variables based on specified parameters.
        for parameter in parameters:
            self.variables[parameter] = None

        # Test data to compare simulated data against.
        self.test_data = None

        # Level of impact on generating further solutions.
        self.weight = 0

        # How successful the solution was.
        self.pheromone = 0
        
    def update_pheromone(self, sim_result):
        """ Calculate and update pheromone """

        # Result from actual test.
        test_result = self.test_data[test_result_name]

        # % error of simulated result.
        error  = (abs(test_result - sim_result)/test_result)*100

        # Calculates  pheromone.
        self.pheromone = 100 - error

    def set_deviation(self, simulator):
        deviation_sum = 0
        for test_data in test_datas:
            pwf = simulator.simulate_test(self, test_data)
            deviation_sum += abs(pwf - test_data[test_result_name])
        self.deviation = deviation_sum/test_data_size

    # Comparisson functions.
    def __lt__(self, other):
        """ check if less than another solution """
        return self.deviation  > other.deviation
    
    def __le__(self, other):
        """ check if less than or equals another solution """
        return self.deviation >= other.deviation
    
    def __gt__(self, other):
        """ check if greater than another solution """
        return self.deviation < other.deviation
    
    def __ge__(self, other):
        """ check if greater than or equals  another solution """
        return self.deviation <= other.deviation
    
    def __ne__(self, other):
        """ check if not equal to another solution """
        return self.deviation != other.deviation

