'''
    AUTHOR: Eric Becerril-Blas
'''
import matplotlib.pyplot as plt
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


def plot_data(df, title, savename):
    '''
        PURPOSE:
            The following function creates the line graph
    '''
    df.plot(x ='Time (years)', y='e', kind = 'line', title = title)
    plt.savefig(savename)



def main():
    print("Hello World From dataplotter.py ")
    # Handling run1 data
    print("Plotting data from run1----------------------")

    print("EARTHMOO.aei:")
    earthmoo_df = create_dataframe('./run1/EARTHMOO.aei')
    print(" ")

    print("JUPITERMOO.aei")
    jupiter_df = create_dataframe('./run1/JUPITER.aei')
    print(" ")

    # Plot EARTHMOO
    plot_data(earthmoo_df,"Earth Sized Planet", "./run1/earthmoo.eps")

    # Plot JUPITER



if __name__== "__main__":
    main()
