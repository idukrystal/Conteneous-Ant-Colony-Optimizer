""" Algorithm parameters. """

# Test model parameters.
from src.main.data import parameters, dataset
from src.main.simulators import DrawdownTestSimulator

# No of discovered solutions to store fore ACOR algorithm
solution_archive_size = 20  * len(parameters)

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

simulator = DrawdownTestSimulator(dataset)
