'''
    AUTHOR: Eric Becerril-Blas
'''
import matplotlib as plt
import pandas as pd
from pandas import *


def plot_data():
    '''
        PURPOSE:
            The following function creates the line graph
    '''
    # Create the figure
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Set the labels and title
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

    # Create the actual bar graph
    ax.bar(x_axis,y_axis) # the .bar() creates the bar graph

    # Save the figure
    fig.savefig(name, dpi = 600) # finally this command, shows the plot
    # Clear the plot
    plt.clf()



def main():
    print("Hello World From dataplotter.py")
    # Handling run1 data
    data = read_table('./run1/EARTHMOO.aei', skiprows=4, header=None, sep=" ")
    print(data)



if __name__== "__main__":
    main()
