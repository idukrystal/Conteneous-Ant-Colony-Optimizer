""" Module to handle each new solution discovered by ants. """

import random 
from src.main.data import parameters, test_data, test_data_size, dependent_test_variable


class Solution:
    """ Represents a single possible solution. """
    
    def __init__(self):
        """ Object constructor function. """
        
        self.parameters = {}
        
        for parameter in parameters:
            self.parameters[parameter] = None

        # Simulated result's deviation from test data results
        self.deviation = 0

        # Level of impact on generating further solutions.
        self.weight = 0

    def set_deviation(self, simulator):
        """ Calculate solution's simulation's deviation from test data """
        
        deviation_sum = 0
        
        for data_point in test_data:
            sim_result = simulator.simulate_test(self, data_point)
            deviation_sum += abs(sim_result  - data_point[dependent_test_variable])
        
        self.deviation = deviation_sum/test_data_size

        
    # Comparisson functions.
    def __lt__(self, other):
        """ checks if less than another solution """
        return self.deviation  > other.deviation
    
    def __le__(self, other):
        """ checks  if less than or equals another solution """
        return self.deviation >= other.deviation
    
    def __gt__(self, other):
        """ checks if greater than another solution """
        return self.deviation < other.deviation
    
    def __ge__(self, other):
        """ checks if greater than or equals  another solution """
        return self.deviation <= other.deviation
    
    def __ne__(self, other):
        """ checks if not equal to another solution """
        return self.deviation != other.deviation

