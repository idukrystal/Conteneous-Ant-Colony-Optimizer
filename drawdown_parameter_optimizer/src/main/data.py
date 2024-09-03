""" Stores and handles data from real world tests"""

# a*b*t = p

# Model parameters and thier expected range of values
parameters = {"s":(-50, 50), "k":(0.001, 1000)}

# Name of Independent Variable
test_value_name  = "time"

# Name of Dependent Variable
test_result_name = "pressure"

# Real World Test Data

"""
dataset = {
    "p_i" : 6009,
    "q" : 2500,
    "β" : 1.21,
    "h" : 23,
    "ø" :0.21,
    "c_t" : 8.72*(10**(-6)),
    "∪" : 0.92,
    "r_w" : 0.401
}
"""

dataset = {
    "p_i" : 5200,
    "q" : 2000,
    "β" : 1.5,
    "h" : 50,
    "ø" :0.24,
    "c_t" : 14.8*(10**(-6)),
    "∪" : 0.3,
    "r_w" : 0.4
}


"""test_datas = [
    {"pressure": 3361.60, "time": 1.34230},
    {"pressure": 3318.80, "time": 1.55366},
    {"pressure": 3289.38, "time": 1.79829},
    {"pressure": 3263.02, "time": 2.08144},
    {"pressure": 3231.28, "time": 2.40918},
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
    {"pressure": 2988.93, "time": 21.6000}
]"""

"""
test_datas = [
    {"pressure": 2989.39, "time": 21.6000},
    {"pressure": 3156.31, "time": 21.6200},
    {"pressure": 3384.61, "time": 21.6500},
    {"pressure": 3715.46, "time": 21.7000},
    {"pressure": 3994.55, "time": 21.7500},
    {"pressure": 4431.29, "time": 21.8500},
    {"pressure": 4740.80, "time": 21.9477},
    {"pressure": 5068.25, "time": 22.1000},
    {"pressure": 5273.46, "time": 22.2500},
    {"pressure": 5461.40, "time": 22.4798}
]
"""

test_data = [
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
