"""
A varriation of the Ant Colony Optimization Algorithm for problems
with continueous parameters. Usefull for finding parameter estimates
from test results data.
Test data, parameters and range as well as a suitable test simulator
should be added in the data module
n.b simulator should be compatible with 'SimulationHelper' class.
"""


import random
from src.main.ant import Ant
from src.main.data import test_data_size
from src.main.params import no_of_iterations
from src.main.simulation_helper import SimulationHelper

simulation_helper = SimulationHelper()

solution_archive = simulation_helper.solution_archive

simulation_helper.fill_solution_archive_randomly()

ant_colony = []
new_solutions = []


for i in range(30):
    # Each ant as unique number
    ant_colony.append(Ant(i))


# Start Algorithm.
for i in range(no_of_iterations):
    # Observe Changes in solution archive
    simulation_helper.print_solution_archive()
    
    for ant in ant_colony:
        # The higher ranked solutiond in archive influences newer solutionh
        solution_archive_weights = [solution.weight for solution in solution_archive]
        weight_sum = sum(solution_archive_weights)
        probabilities = [weight/weight_sum for weight in solution_archive_weights]
        solution = random.choices(solution_archive, probabilities, k=1)[0]

        # Chosen solution's variables  deviation from other solution's variables
        standard_deviations  = simulation_helper.calculate_deviations(solution)
        
        # Uses a normal distribution about solution's varriable
        # to generate  varriables in new solution
        new_solution = ant.find_solution(solution, standard_deviations)

        # How closely new solution fits test data: determines ranking
        new_solution.set_deviation(simulation_helper.simulator)
        new_solutions.append(new_solution)

    # Adds to archive if it's good enogh
    simulation_helper.update_archive(new_solutions)
    new_solutions.clear()


print("\n#####Final Result#####")


simulation_helper.print_solution_archive()

simulation_helper.show_final_stats()
