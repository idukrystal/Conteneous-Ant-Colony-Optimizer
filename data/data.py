""" Stores and handles data from real world tests"""

# Model parameters and thier expected range of values
parameters = {"c":(0, 1)}
#parameters = {"s":(-10, 10), "k":(1, 1000)}
#parameters = {"s":(5, 8), "k":(60, 90), "t1":(0.05, 0.15), "t2":(1.5,3.5),"c":(0, 0.1),"p_i": (5000, 7000)}
#parameters = {"r_e": (100, 5000), "k":(1, 1000), "s":(-5, 5)}

# Name of Independent Variable
independent_test_variable = "time"

# Name of Dependent Variable
dependent_test_variable = "pressure"

# Reservoir and Well properties

properties = {
    "q" : 2500,
    "t_i": 0,
    "p_i": 6009,
    "β" : 1.21,
    "h" : 23,
    "ø" :0.21,
    "c_t" : 8.72*(10**(-6)),
    "∪" : 0.92,
    "r_w" : 0.401
}

""""
properties  = {
    "p_i" : 5200,
    "q" : 2000,
    "β" : 1.5,
    "h" : 50,
    "ø" :0.24,
    "c_t" : 14.8*(10**(-6)),
    "∪" : 0.3,
    "r_w" : 0.4
}
"""

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
]



"""
[
    {'pressure': 5521.66, 'time': 0.06227},
    {'pressure': 5459.70, 'time': 0.07207},
    {'pressure': 5389.75, 'time': 0.08342},
    {'pressure': 5306.48, 'time': 0.09655},
    {'pressure': 5211.11, 'time': 0.11176},
    {'pressure': 5117.79, 'time': 0.12935},
    {'pressure': 5009.74, 'time': 0.14972},
    {'pressure': 4886.13, 'time': 0.1733},
    {'pressure': 4769.13, 'time': 0.20058},
    {'pressure': 4635.16, 'time': 0.23217},
    {'pressure': 4501.08, 'time': 0.26872},
    {'pressure': 4365.85, 'time': 0.31103},
    {"pressure": 4219.70, "time": 0.36001},
    {"pressure": 4089.84, "time": 0.41669},
    {"pressure": 3960.16, "time": 0.48230},
    {"pressure": 3835.59, "time": 0.55824},
    {"pressure": 3727.20, "time": 0.64614},
    {"pressure": 3630.08, "time": 0.74788},
    {"pressure": 3538.77, "time": 0.86564},
    {"pressure": 3465.23, "time": 1.00194},
    {"pressure": 3411.56, "time": 1.1597},
    {"pressure": 3361.60, "time": 1.34230},
    {"pressure": 3318.80, "time": 1.55366},
    {"pressure": 3289.38, "time": 1.79829}
    {"pressure": 3263.02, "time": 2.08144},
    {"pressure": 3231.28, "time": 2.40918},
]
"""



"""
test_data = [
    {"pressure": 3216.27, "time": 2.78852},
    {"pressure": 3200.34, "time": 3.22758},
    {"pressure": 3175.40, "time": 3.73579},
    {"pressure": 3162.30, "time": 4.32401},
    {"pressure": 3139.87, "time": 5.00485},
    {"pressure": 3133.46, "time": 5.79289},
    {"pressure": 3114.87, "time": 6.70502},
    {"pressure": 3092.78, "time": 7.76076},
    {"pressure": 3081.99, "time": 8.98274},
    {"pressure": 3062.07, "time": 10.3971},
    {"pressure": 3047.29, "time": 12.0342},
    {"pressure": 3037.98, "time": 13.9291},
    {"pressure": 3018.23, "time": 16.1223},
    {"pressure": 3002.85, "time": 18.6608},
    {"pressure": 2988.93, "time": 21.6},
]
"""

"""
test_data = [
    {"pressure": 3002.85, "time": 18.6608}, 
    {"pressure": 2988.93, "time": 21.6},
    {"time": 24.25, "pressure": 2939.3},
    {"time": 26.37, "pressure": 2921.5},
    {"time": 28.67, "pressure": 2902.3},
    {"time": 31.17, "pressure": 2881.4},
    {"time": 33.90, "pressure": 2858.7},
    {"time": 36.86, "pressure": 2834.0},
    {"time": 40.07, "pressure": 2807.2},
    {"time": 43.57, "pressure": 2778.0},
    {"time": 47.38, "pressure": 2746.2},
    {"time": 51.51, "pressure": 2711.7},
    {"time": 56.01, "pressure": 2674.2},
    {"time": 60.90, "pressure": 2633.4},
    {"time": 72.00, "pressure": 2540.7},
]
"""

"""    
[
    {"pressure": 5010.74, "time": 1.00000},
    {"pressure": 4998.50, "time": 1.20226},
    {"pressure": 4985.55, "time": 1.44544},
    {"pressure": 4971.89, "time": 1.73780},
    {"pressure": 4957.68, "time": 2.08930},
    {"pressure": 4942.91, "time": 2.51189},
    {"pressure": 4927.61, "time": 3.01995},
    {"pressure": 4911.77, "time": 3.63078},
    {"pressure": 4895.03, "time": 4.36516},
    {"pressure": 4878.17, "time": 5.24808},
    {"pressure": 4861.32, "time": 6.30957},
    {"pressure": 4844.35, "time": 7.58578},
    {"pressure": 4826.47, "time": 9.12011},
    {"pressure": 4808.59, "time": 10.9648},
    {"pressure": 4790.31, "time": 13.1826},
    {"pressure": 4771.89, "time": 15.8489},
    {"pressure": 4753.29, "time": 19.0546},
    {"pressure": 4734.54, "time": 22.9087},
    {"pressure": 4715.66, "time": 27.5423},
    {"pressure": 4696.68, "time": 33.1131}
]
"""


test_data_size = len(test_data)
