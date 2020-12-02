'''
    AUTHOR: Eric Becerril-Blas
'''
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import pandas as pd
from pandas import *

def create_dataframe(f_name,skip):
    # Open the FileName
    f = open(f_name,'r')
    # Skip over the first 3 lines of the .aei ffile
    lines = f.readlines()[skip:]
    #print(lines)
    # Close the File
    f.close()
    # Get the header file and create the header using a super complicated brute force method that could have been easily solved by going into the raw data and deleting the space between "Time" and "(years)" in the .aei file
    header_line = lines.pop(0)
    header_line = header_line.split()
    #print(header_line)
    header = []
    first_element = 'Name'
    header.append(first_element)
    for element in header_line:
        header.append(element)


    #print(lines)
    # Turning data to float values and dataframe
    new_lines = []
    for l in lines:
         l = l.split()
         for idx,item in enumerate(l):
             if idx != 0:
                 l[idx] = float(item)
         new_lines.append(l)
    #print(new_lines)

    # Make dataframe out of the list of lists
    df = pd.DataFrame.from_records(new_lines)
    df.columns= header
    #print(" ")
    #print("Initial conditions of run are")
    #print(df.iloc[:1])
    df = df.iloc[1:]

    #print(df)
    return df

def append_dataframe(df, f_name):
    f = open(f_name,'r')
    # Skip over the first 3 lines of the .aei ffile
    lines = f.readlines()
    #print(lines)
    # Close the File
    f.close()
    new_lines = []
    for l in lines:
         l = l.split()
         for idx,item in enumerate(l):
             if idx != 0:
                 l[idx] = float(item)
         new_lines.append(l)
    #print(new_lines)
    df2 = pd.DataFrame.from_records(new_lines)
    df2.columns = [ 'Name'  ,'a'  ,'e'  ,'i' ,'mass'  ,'Rot/day' ,'Obl']
    #print(df2)
    df = df.append(df2, ignore_index=True)
    return(df)

def rm_the_planets(df):
    for index, row in df.iterrows():
        if row['Name'] == 'EARTHMOO':
            df.drop(index, inplace=True)
        if row['Name'] == 'SATURN':
            df.drop(index, inplace=True)
        if row['Name'] == 'JUPITER':
            df.drop(index, inplace=True)
    return(df)



def main():
    print("Hello World From asteroid_madness.py ")
    elementout = create_dataframe('run_5/element.out',3)
    elementout = append_dataframe(elementout, 'run_5/element1.out')
    elementout = append_dataframe(elementout, 'run_5/element2.out')
    elementout = append_dataframe(elementout, 'run_5/element3.out')
    elementout = append_dataframe(elementout, 'run_5/element4.out')
    elementout = append_dataframe(elementout, 'run_5/element5.out')
    elementout = append_dataframe(elementout, 'run_5/element6.out')
    elementout = append_dataframe(elementout, 'run_5/element7.out')
    elementout = append_dataframe(elementout, 'run_5/element8.out')
    elementout = append_dataframe(elementout, 'run_5/element9.out')
    elementout = append_dataframe(elementout, 'run_5/element10.out')

    elementout = rm_the_planets(elementout)

    print(elementout)

    ax = elementout.plot(kind='scatter',x='a',y='e',color='red',s=5)


    ax.set_xlabel("Semi-Major Axis")
    ax.set_ylabel("Eccentricity")
    plt.axvline(x = 1.00001) #Earths spot after 10 million years

    plt.axvline(x = 2.05, c = 'g', label = "v_6") #Earths spot after 10 million years


    plt.show()
    plt.clf()


if __name__== "__main__":
    main()
