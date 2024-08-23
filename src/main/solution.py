""" Module to handle each new solution discovered by ants. """


# Name of variable generated  by test (i.e pressure).
from data  import test_result_name


class Solution:
    """ Represents a single possible solution. """
    
    def __init__(self):
        """ Object constructor function. """
        
        # variables:values used to generate solution
        self.variables = {}

        # Level of impact on generating further solutions
        self.weight = 0

        # How successful the solution was
        self.pheromone = 0
        
    def update_pheromone(self, sim_result):
        """ Calculate and update pheromone """

        # Result from actual test
        test_result = self.test_data[test_result_name]

        # % error of simulated result 
        error  = (abs(test_result - sim_result)/test_result)*100

        # calculate pheromone
        self.pheromone = 100 - error

    # Comparisson functions 
    def __lt__(self, other):
        """ check if less than another solution """
        return self.pheromone < other.pheromone
    
    def __le__(self, other):
        """ check if less than or equals another solution """
        return self.pheromone <= other.pheromone
    
    def __gt__(self, other):
        """ check if greater than another solution """
        return self.pheromone > other.pheromome
    
    def __ge__(self, other):
        """ check if greater than or equals  another solution """
        return self.pheromone >= other.pheromone
    
    def __ne__(self, other):
        """ check if not equal to another solution """
        return self.pheromone != other.pheromone