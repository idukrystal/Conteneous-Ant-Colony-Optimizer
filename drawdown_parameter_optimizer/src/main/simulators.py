
""" Module to handle various type of simulations """

import random

from numpy import log10 as log

class Simulator:
    """ Generic Simulation Object """
    
    def __init__(self, dataset):
        """ Constructor function """
        pass

    def simulate_test(self, solution):
        """" Runs the simulation """
        return solution.variables["a"]*solution.variables["b"]*solution.test_data["time"]#implement


class DrawdownTestSimulator(Simulator):
    

    parameters = ["p_i", "q", "β", "h", "ø", "c_t", "∪", "r_w"] 
    def __init__(self, dataset):
        for parameter in self.parameters:
            if parameter not in dataset:
                exit(f"{parameter} not found")
        self.dataset = dataset
    def simulate_test(self, solution, test_data = None):
        test_data = solution.test_data if test_data == None else test_data
        return get_pwf(
            self.dataset,
            test_data["time"],
            solution.variables["s"],
            solution.variables["k"]
        )


def get_pwf(dataset, t, s, k):
    p_i  = dataset["p_i"]
    q = dataset["q"]
    β = dataset["β"]
    U = dataset["∪"]
    h = dataset["h"]
    ø = dataset["ø"]
    c_t= dataset["c_t"]
    r_w = dataset["r_w"]
    log_a = log(k/(ø*U*c_t*(r_w**2)))
    pwf = p_i - (162.6*((q*β*U)/(k*h))*(log(t)+log_a+(0.8686*s)-3.2274))
    return pwf
