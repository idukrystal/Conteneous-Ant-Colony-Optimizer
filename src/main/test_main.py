import random

from .solution import Solution
from .params import parameters
from src.main.simulation_helper import SimulationHelper
from src.main.params import no_of_iterations
from src.main.data import test_datas
from src.main.ant import Ant
simulation_helper = SimulationHelper()
solution_archive = simulation_helper.solution_archive

simulation_helper.initialize_simulation()

ants = []

for i in range(len(test_datas)):
    ants.append(Ant(i, test_datas[i]))

for i in range(no_of_iterations):
    simulation_helper.print_solution_archive()
    print("******************")
    print()
    for ant in ants:
        #solution = random.choices(solution_archive, [solution.weight for solution in solution_archive], k=1)[0]
        
        solution  = Solution()
        for variable in solution.variables:
            solution.variables[variable] = random.uniform(
                *parameters[variable]
            )
        sds = simulation_helper.calculate_sd(solution)
        new_solution = ant.find_solution(solution, sds)
        #sim_result = simulation_helper.simulator.simulate_test(new_solution)
        new_solution.set_deviation(simulation_helper.simulator)
        #new_solution.update_pheromone(sim_result)
        simulation_helper.update_solution_archive(new_solution)

#simulation_helper.generate_solution_deviations()
print("final")

simulation_helper.print_solution_archive()
