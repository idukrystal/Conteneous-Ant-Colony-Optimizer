""" Algorithm parameters. """

from src.main.data import properties
from src.main.simulators import DrawdownTestSimulator, WellboreStorageSimulator, PseudoSteadyBoundarySimulator

# No of discovered solutions to store fore ACOR algorithm
solution_archive_size = 100

# When q is small, the best-ranked solutions are strongly preferred.
# When it is large, the probability becomes more uniform.
q_value  = 1.5

# Must be greater than 0.
# Inversely affects convergence speed.
# influences the way the long term memory is used.
# >e: less biased towards the points of the search space already explored.
e_value = 1.5

# No of times to run algorithm.
no_of_iterations = 5000

simulator = WellboreStorageSimulator(properties)
#simulator = DrawdownTestSimulator(properties)
#simulator = PseudoSteadyBoundarySimulator(properties)
