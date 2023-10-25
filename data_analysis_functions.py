import matplotlib.pyplot as plt
import numpy as np

def create_graph(input):
    week = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    stat = np.array(input)
    print(stat)
    
    plt.plot(week,stat,label="Chosen Stat Per Game")
    
    plt.show()
