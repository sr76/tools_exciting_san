import matplotlib as mpl
import matplotlib.pyplot as plt

def plotxysimple(x,y):

    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(x,y)
    plt.show()

