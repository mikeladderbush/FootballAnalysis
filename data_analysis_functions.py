import matplotlib.pyplot as plt
import numpy as np

def create_graph(*args):
    input_vector = []
    input_numpy_arrays = []
    opponent_array = args[0].pop()
    week = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    
    ax = plt.axes()
    ax.set_xticks(week)
    ax.set_xticklabels(opponent_array)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    
    for vector in args:
        input_vector.append(vector)
    for vector in input_vector:
        input_numpy_arrays.append(np.array(vector))
    for item in input_numpy_arrays:
        for stat in item:
            plt.plot(week,stat)
    plt.tight_layout()
    plt.show()
