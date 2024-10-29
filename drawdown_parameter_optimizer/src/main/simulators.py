
""" Module to handle various type of simulations """

import random

from numpy import log10 as log

class Simulator:
    """ Generic Simulation Object """

    property_names = ["x", "y"]
    def __init__(self, dataset):
        """ Constructor function """
        for property_name in self.property_names:
            if property_name not in dataset:
                exit(f"{property_name} not found")
        self.properties = dataset

    def simulate_test(self, solution):
        """" Runs the simulation """
        #implement
        pass


class DrawdownTestSimulator(Simulator):
    
    property_names = ["p_i", "q", "β", "h", "ø", "c_t", "∪", "r_w"]
    def __init__(self, properties):
        super().__init__(properties)
    def simulate_test(self, solution, test_data):
        return get_pwf(
            self.properties,
            test_data["time"],
            solution.parameters["s"],
            solution.parameters["k"]

        )


class WellboreStorageSimulator(Simulator):
    property_names=["p_i", "q", "β"]
    def __init__(self, properties):
        super().__init__(properties)
    def simulate_test(self, solution, test_data):
        return self.get_pwf(
            self.properties,
            test_data["time"],
            solution.parameters["c"]
        )
    @staticmethod
    def get_pwf(properties, t, c):
        p_i = properties["p_i"]
        t_i = properties["t_i"]
        q = properties["q"]
        β = properties["β"]
        pwf = p_i - ((0.234*q*β*(t-t_i))/(5.615*c))
        return pwf

class PseudoSteadyBoundarySimulator(Simulator):
        property_names=["p_i", "t_i", "q", "β", "h", "ø", "c_t"]
        def __init__(self, properties):
            super().__init__(properties)
        def simulate_test(self, solution, test_data):
            return self.get_pwf(
                self.properties,
                test_data["time"],
                solution.parameters["A"]
            )
        @staticmethod
        def get_pwf(properties, t, area):
            p_i  = properties["p_i"]
            t_i = properties["t_i"]
            q = properties["q"]
            β = properties["β"]
            h = properties["h"]
            ø = properties["ø"]
            c_t= properties["c_t"]
            pwf = p_i - ((0.2342*q*β*(t-t_i))/(ø*c_t*h*area))
            return pwf


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
