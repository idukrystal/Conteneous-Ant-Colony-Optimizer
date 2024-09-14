
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
    

    property_names = ["p_i", "q", "β", "h", "ø", "c_t", "∪", "r_w"] 
    def __init__(self, properties):
        for property_name in self.property_names:
            if property_name not in properties:
                exit(f"{property_name} not found")
        self.properties = properties
    def simulate_test(self, solution, test_data):
        return get_pwf(
            self.properties,
            test_data["time"],
            solution.parameters["s"],
            solution.parameters["k"]
        )


def get_pwf(properties, t, s, k):
    p_i  = properties["p_i"]
    q = properties["q"]
    β = properties["β"]
    U = properties["∪"]
    h = properties["h"]
    ø = properties["ø"]
    c_t= properties["c_t"]
    r_w = properties["r_w"]
    log_a = log(k/(ø*U*c_t*(r_w**2)))
    pwf = p_i - (162.6*((q*β*U)/(k*h))*(log(t)+log_a+(0.8686*s)-3.2274))
    return pwf
