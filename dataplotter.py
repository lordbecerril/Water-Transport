'''
    AUTHOR: Eric Becerril-Blas
'''
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import pandas as pd
from pandas import *

def create_dataframe(f_name):
    # Open the FileName
    f = open(f_name,'r')
    # Skip over the first 3 lines of the .aei ffile
    lines = f.readlines()[3:]
    # Close the File
    f.close()
    # Get the header file and create the header using a super complicated brute force method that could have been easily solved by going into the raw data and deleting the space between "Time" and "(years)" in the .aei file
    header_line = lines.pop(0)
    header_line = header_line.split()
    #print(header_line)
    header = []
    first_element = header_line[0] + ' ' + header_line[1]
    header.append(first_element)
    for element in header_line[2:]:
        header.append(element)




    # Turning data to float values and dataframe
    new_lines = []
    for l in lines:
         l = l.split()
         for idx,item in enumerate(l):
             l[idx] = float(item)
         new_lines.append(l)

    # Make dataframe out of the list of lists
    df = pd.DataFrame.from_records(new_lines)
    df.columns= header
    print(" ")
    print("Initial conditions of run are")
    print(df.iloc[:1])

    return df
    #print(df)


def line_graph(df, title, savename, color):
    '''
        PURPOSE:
            The following function creates the line graph
    '''
    fig, ax = subplots()

    df.plot(x ='Time (years)', y='e', kind = 'line', title = title, color = color, ax=ax)
    ax.legend(["Eccentricity"])
    ax.set_ylabel("Eccentricity")
    plt.tight_layout()

    plt.savefig(savename)
    plt.clf()


def plot_together(df1, df2, savename):
    fig, ax = subplots()

    ax = df1.plot(x ='Time (years)', y='e', kind = 'line', color = 'blue', title = "Earth and Jupiter")
    df2.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'red')
    ax.legend(["Earth Sized Planet e", "Jupiter Sized Planet e"])
    ax.set_ylabel("Eccentricity")
    plt.tight_layout()

    plt.savefig(savename)
    plt.clf()

def dataplotter(earthmoo, jupiter, earthplot, jupiterplot, togetherplot):
    print("EARTHMOO.aei:")
    earthmoo_df = create_dataframe(earthmoo)
    print(" ")

    print("JUPITERMOO.aei")
    jupiter_df = create_dataframe(jupiter)
    print(" ")

    # Plot EARTHMOO
    line_graph(earthmoo_df, "Earth Sized Planet", earthplot, "blue")

    # Plot JUPITER
    line_graph(jupiter_df, "Jupiter Sized Planet", jupiterplot, "red")

    # plot them together
    plot_together(earthmoo_df, jupiter_df, togetherplot)


def main():
    print("Hello World From dataplotter.py ")

    # Handling run1 data
    print("Plotting data from run1----------------------")
    dataplotter('./run1/EARTHMOO.aei','./run1/JUPITER.aei',"./run1/earthmoo.eps","./run1/jupiter.eps","./run1/together.eps")
    print(" ")

    # Handling run2 data
    print("Plotting data from run2----------------------")
    dataplotter('./run2/EARTHMOO.aei','./run2/JUPITER.aei',"./run2/earthmoo.eps","./run2/jupiter.eps","./run2/together.eps")
    print(" ")

    # Handling run3 data
    print("Plotting data from run3----------------------")
    dataplotter('./run3/EARTHMOO.aei','./run3/JUPITER.aei',"./run3/earthmoo.eps","./run3/jupiter.eps","./run3/together.eps")
    print(" ")

    # Handling run4 data
    print("Plotting data from run4----------------------")
    dataplotter('./run4/EARTHMOO.aei','./run4/JUPITER.aei',"./run4/earthmoo.eps","./run4/jupiter.eps","./run4/together.eps")
    print(" ")


if __name__== "__main__":
    main()
