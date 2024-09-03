"""
Useful functions and variables for simulation of
test data and running of algorithm
"""


from numpy import e, square, pi, sqrt
from src.main.data import test_datas, test_value_name, test_result_name, dataset
import random
from scipy.stats import norm
from src.main.solution import Solution
from src.main.params import solution_archive_size, q_value, parameters, e_value, simulator

test_data_size = len(test_datas)

class SimulationHelper:
    """ Helps run a the simulation: useful functions and variables """
    
    def __init__(self):
        """ Constructor: initilizes object variables. """

        # To temprorarily store best solutions so far.
        self.solution_archive = []

        # Simulates test and returs sim data
        self.simulator = simulator

        self.test_datas_size = len(test_datas)
    def initialize_simulation(self):
        """ Populates the solution archive with random solutions. """
        for i in range(solution_archive_size):
            solution = Solution()

            # Random test data to compare sim data to.
            solution.test_data  = random.choice(test_datas)

            # Random value for each model parameter thats a solution.
            for variable in solution.variables:
                solution.variables[variable] = random.uniform(
                    *parameters[variable]
                )

            # Simulate a test result.
            #sim_result = self.simulator.simulate_test(solution)

            # Update solutions pheromone level.
            #solution.update_pheromone(sim_result)

            solution.set_deviation(self.simulator)
            # Add to solutipn archive.
            self.solution_archive.append(solution)

        # Adjust solution weights to reflect newly added solutions.
        self.__modify_weights()
    
    def __modify_weights(self, reorder=True):
        """ Adjust solution weights to reflect newly added solutions. """

        # Rearange solutions in other
        if reorder:
            self.__reorder_solution_archive()

        # Calculate new weighta for each solution in archive
        for i in range(solution_archive_size):
            solution = self.solution_archive[i]
            solution.weight = get_weight(i)

    def __reorder_solution_archive(self, orderBy = None):
        """ Rearranges solutioms in archive in decending
        amount of pheromone """
        self.solution_archive.sort(key=orderBy, reverse=True)

    def print_solution_archive(self):
        """ Prints out the solution archive in a human readable way. """
        for solution in self.solution_archive:
            print(
                solution.variables, '**',
                solution.weight, '**',
                solution.pheromone, '**',
                solution.deviation
            )

    def update_solution_archive(self, new_solution):
        """
        Adds new_solution to archive if its better than any
        of the current ones then  removes the worst solution
        Return: returns true if archive updated false otherwise
        """
        
        for i in range (solution_archive_size):
            if new_solution >= self.solution_archive[i]:
                self.solution_archive.insert(i, new_solution)
                self.solution_archive.pop()
                self.__modify_weights(reorder=False)
                return True
        return False
    
    def calculate_sd(self, solution):
        """
        Generates a list of  standard deviations: one for each
        variable in [solution] based on distance from corresponding
        variables in other solutions in archive.
        Returns: computed list of standard deviations
        """
        sd = {}
        for variable in solution.variables:
            sd[variable] = calculate_sd(
                solution.variables[variable],
                [
                    value.variables[variable] for value in self.solution_archive
                ]
            )
        return sd
    def generate_solution_deviations(self):
        for solution in self.solution_archive:
            get_deviation(solution, self.simulator)
        self.__reorder_solution_archive(lambda solution: solution.deviation)


        


def get_weight(i):
    """
    Calculates weights based on rank[i] in a list
    Return: returns computed weight. 
    """
    a = (1/(q_value*solution_archive_size*sqrt(2*pi)))
    b = (e**(-(square(i-1)/(2*square(q_value*solution_archive_size)))))

    # To 5 d.p
    return a*b


def calculate_sd(x, values):
    """
    Calculates the standard deviation of no's in [values] from [x]
    Return: returns computef standard deviation
    """
    sum = 0

    found = False

    for value in values:
        if value == x and not found:
            found = True
            continue
        sum += abs(value - x)

    # e_value controls convengence speed
    return e_value*(sum/(solution_archive_size - 1))
