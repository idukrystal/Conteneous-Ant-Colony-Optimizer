from .solution import Solution
from src.main.params import parameters
from scipy.stats import truncnorm

class Ant:
    def __init__(self, no, test_data):
        self.no = no
        self.test_data = test_data
    def find_solution(self, old_solution, sds):
        new_solution = Solution()
        for variable in new_solution.variables:
            mu = old_solution.variables[variable]
            sd = sds[variable]
            a, b = parameters[variable]
            a, b = (a - mu)/sd, (b - mu)/sd
            gus = truncnorm(a, b, loc=mu, scale=sd)
            new_solution.variables[variable] = gus.rvs()
        
        return new_solution
