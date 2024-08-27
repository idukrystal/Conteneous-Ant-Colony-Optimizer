""" Algorithm parameters. """

# Test model parameters.
from src.main.data import parameters

# No of discovered solutions to store fore ACOR algorithm
solution_archive_size = 10  * len(parameters)

# When q is small, the best-ranked solutions are strongly preferred.
# When it is large, the probability becomes more uniform.
q_value  = 2

# Must be greater than 0.
# Inversely affects convergence speed.
# influences the way the long term memory is used.
# >e: less biased towards the points of the search space already explored.
e_value = 0.7

# No of times to run algorithm.
no_of_iterations = 20000
