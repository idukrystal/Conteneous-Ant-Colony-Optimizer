

""" Module to handle various type of simulations """

import random

from numpy import log10 as log, log as ln

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
    
    property_names = ["q", "β", "h", "ø", "c_t", "∪", "r_w"]
    def __init__(self, properties):
        super().__init__(properties)
    def simulate_test(self, solution, test_data):
        return get_pwf(
            self.properties,
            test_data["time"],
            test_data["pressure"],
            solution.parameters["s"],
            solution.parameters["k"],
            solution.parameters["p_i"],
            solution.parameters["t1"],
            solution.parameters["t2"],
            solution.parameters["c"]
        )

    
class InfiniteActingRadialSimulator(Simulator):
    property_names = ["q", "β", "h", "ø", "c_t", "∪", "r_w"]
    def __init__(self, properties):
        super().__init__(properties)
        
    def simulate_test(self, solution, test_data):
        #solution.parameters["p_i"] = 6009
        #solution.parameters["k"] = 77.1
        #solution.parameters["s"] = 6.09
        return self.get_pwf(
            self.properties,
            test_data["time"],
            #solution.parameters["p_i"],
            solution.parameters["k"],
            solution.parameters["s"],
        )
    @staticmethod
    def get_pwf(properties, t, k, s):
        q = properties["q"]
        t_i = properties["t_i"]
        p_i = properties["p_i"]
        β = properties["β"]
        U = properties["∪"]
        h = properties["h"]
        ø = properties["ø"]
        c_t= properties["c_t"]
        r_w = properties["r_w"]
        log_a = log(k/(ø*U*c_t*(r_w**2)))
        pwf = p_i - (162.6*((q*β*U)/(k*h))*(log(t-t_i)+log_a+(0.8686*s)-3.2274))
        return pwf
            


class WellboreStorageSimulator(Simulator):
    property_names=["q", "β"]
    def __init__(self, properties):
        super().__init__(properties)
    def simulate_test(self, solution, test_data):
        #solution.parameters["p_i"] = 6009
        #solution.parameters["c"] = 0.01541
        return self.get_pwf(
            self.properties,
            test_data["time"],
            solution.parameters["c"],
            #solution.parameters["p_i"]
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
            #solution.parameters["p_i"] = 2989
            #solution.parameters["t_i"] = 21.6
            #solution.parameters["A"] = 1969700
            return self.get_pwf(
                self.properties,
                test_data["time"],
                solution.parameters["r_e"],
                solution.parameters["k"],
                solution.parameters["s"],
            )
        @staticmethod
        def get_pwf(properties, t, r_e, k, s):
            p_i = properties["p_i"]
            t_i = properties["t_i"]
            q = properties["q"]
            B = properties["β"]
            U = properties["∪"]
            h = properties["h"]
            r_w = properties["r_w"]
            ø = properties["ø"]
            c_t= properties["c_t"]
            #pwf = p_i - ((0.2342*q*β*(t-t_i))/(ø*c_t*h*area))
            pwf = p_i - (((141.2*q*B*U)/(h*k))*(ln(r_e/r_w)-(3/4)+s))
            return pwf


def get_pwf(properties, t, p,  s, k, p_i, t1, t2, c):
    q = properties["q"]
    β = properties["β"]
    U = properties["∪"]
    h = properties["h"]
    ø = properties["ø"]
    c_t= properties["c_t"]
    r_w = properties["r_w"]
    log_a = log(k/(ø*U*c_t*(r_w**2)))
    if t >= t2:
        pwf = p_i - (162.6*((q*β*U)/(k*h))*(log(t)+log_a+(0.8686*s)-3.2274))
    elif t <= t1:
        pwf = p_i - ((0.234*q*β*(t))/(5.615*c))
    else:
        pwf = p - 50
    return pwf
