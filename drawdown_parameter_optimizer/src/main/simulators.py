""" Module to handle various type of simulations """

import random

class Simulator:
    """ Generic Simulation Object """
    
    def __init__(self):
        """ Constructor function """
        pass

    def simulate_test(self, solution):
        """" Runs the simulation """
        return solution.variables["a"]*solution.variables["b"]*solution.test_data["time"]#implement
