import matplotlib.pyplot as plt
import numpy as np

def create_graph(input):
    week = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    yards = np.array(input)
    print(yards)
    
    plt.plot(week,yards,label="Yards by Week")
    
    plt.show()
