""" Stores and handles data from real world tests"""

# a*b*t = p

# Model parameters and thier expected range of values
parameters = {"a":(1, 1000), "b":(1, 1000)}

# Name of Independent Variable
test_value_name  = "time"

# Name of Dependent Variable
test_result_name = "pressure"

# Real World Test Data
test_datas = [
    {"pressure": 99900, "time": 10},
    {"pressure": 195000, "time": 20},
    {"pressure": 305000, "time": 30},
    {"pressure": 401000, "time": 40},
    {"pressure": 499000, "time": 50}
]
