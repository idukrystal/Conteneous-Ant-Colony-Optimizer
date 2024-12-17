"""
WELL: WELL TEST ANALYSIS REPORT Example 4.1
LOCATION: MODERN WELL TEST ANALYSIS: A Computer-Aided Approach
OPERATOR: Roland N. Horne
"""


# Model parameters and thier expected range of valueS
parameters = {"s":(-10, 10), "k":(1, 1000), "p_i": (1000, 10000)}

# Name of Independent Variable
independent_test_variable = "time"

# Name of Dependent Variable
dependent_test_variable = "pressure"

# Reservoir and Well properties
properties = {
    "q" : 2500,
    "t_i": 0,
    "β" : 1.21,
    "h" : 23,
    "ø" :0.21,
    "c_t" : 8.72*(10**(-6)),
    "∪" : 0.92,
    "r_w" : 0.401
}

# Real World Test Data
test_data = [
    {'pressure': 5867.82, 'time': 0.0167},
    {'pressure': 5845.93, 'time': 0.01933},
    {'pressure': 5819.44, 'time': 0.02237},
    {'pressure': 5792.50, 'time': 0.0259},
    {'pressure': 5765.01, 'time': 0.02997},
    {'pressure': 5720.90, 'time': 0.03469},
    {'pressure': 5688.36, 'time': 0.04016},
    {'pressure': 5642.92, 'time': 0.04648},
    {'pressure': 5587.43, 'time': 0.0538},
    {'pressure': 5521.66, 'time': 0.06227},
    {'pressure': 5459.70, 'time': 0.07207},
    {'pressure': 5389.75, 'time': 0.08342},
    {'pressure': 5306.48, 'time': 0.09655}
    {'pressure': 5211.11, 'time': 0.11176},
    {'pressure': 5117.79, 'time': 0.12935},
    {'pressure': 5009.74, 'time': 0.14972},
    {'pressure': 4886.13, 'time': 0.1733},
    {'pressure': 4769.13, 'time': 0.20058},
    {'pressure': 4635.16, 'time': 0.23217},
    {'pressure': 4501.08, 'time': 0.26872},
    {'pressure': 4365.85, 'time': 0.31103},
]
