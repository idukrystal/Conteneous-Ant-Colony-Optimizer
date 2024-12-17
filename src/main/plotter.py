import matplotlib.pyplot as plt

from math import log10 as log, log as ln
from src.main.data import test_data, properties

def plot_log_log(data_points, p_i, t_i):
    p_points = [p_i - data_point["pressure"] for data_point in data_points]
    t_points = [data_point["time"] - t_i for data_point in data_points]
    x_points = [ log(data_point["time"] - t_i) for data_point in data_points[1:] ]
    y_points = [ log(p_i - data_point["pressure"]) for data_point in data_points[1:]]
    y2_points = []
    y2_points.append(None)
    for i in range(1, len(y_points) - 1):
        a = (p_points[i+1]-p_points[i])/(ln(t_points[i+1])-ln(t_points[i]))
        y2_points.append(log(a))
    y2_points.append(None)
    print(x_points)
    print(y_points)
    print(y2_points)
    plt.plot(x_points, y_points)
    plt.plot(x_points, y2_points)
    plt.savefig("results/images/result.png")
    
plot_log_log(test_data, properties["p_i"], properties["t_i"])
