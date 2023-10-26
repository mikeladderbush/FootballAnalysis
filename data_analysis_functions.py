import matplotlib.pyplot as plt
import numpy as np

def create_graph(*args):
    week = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    
    for item in args:
        print(item)
        for stat in item:
            print(stat)
            plt.plot(week,stat)
    
    plt.show()
