""" Algorithm parameters. """


from .simulators import Simulator

# Model parameters to optimize: thier range .
parameters = {"a":(10, 100), "b":(201, 400)}

# No of discovered solutions to s.tore fore ACOR algorithm
solution_archive_size = 10  * len(parameters)

# Inversely affects convergence speed etc.
q_value  = 0.5

e_value = 0.5

# no times to iteration
no_of_iterations = 10
