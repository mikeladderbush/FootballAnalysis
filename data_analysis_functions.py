import matplotlib.pyplot as plt

def create_graph(x):
    y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    plt.plot(y,x)
    plt.xlabel('x - axis')
    plt.xlim(1,17)
    plt.ylabel('y - axis')
    plt.ylim(0,400)
    plt.title('Tits')
    plt.show()