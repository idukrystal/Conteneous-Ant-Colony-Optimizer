""" Stores and handles data from real world tests"""

# a*b*t = p

# Model parameters and thier expected range of values
parameters = {"s":(-2, 8), "k":(50, 85)}

# Name of Independent Variable
test_value_name  = "time"

# Name of Dependent Variable
test_result_name = "pressure"

# Real World Test Data

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

3216.27
3200.34
3175.40
3162.30
3139.87

test_datas = [
    {"pressure": 3361.60, "time": 1.34230},
    {"pressure": 3318.80, "time": 1.55366},
    {"pressure": 3289.38, "time": 1.79829},
    {"pressure": 3263.02, "time": 2.08144},
    {"pressure": 3231.28, "time": 2.40918},
    {"pressure": 3216.27, "time": 2.78852},
    {"pressure": 3200.34, "time": 3.22758},
    {"pressure": 3175.40, "time": 3.73579},
    {"pressure": 3162.30, "time": 4.32401},
    {"pressure": 3139.87, "time": 5.00485}
]

