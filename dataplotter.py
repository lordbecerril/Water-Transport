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
    '''
    # Handling run1 data
    print("Plotting data from run1----------------------")
    dataplotter('./run1/EARTHMOO.aei','./run1/JUPITER.aei',"./run1/earthmoo.png","./run1/jupiter.png","./run1/together.png")
    print(" ")

    # Handling run2 data
    print("Plotting data from run2----------------------")
    dataplotter('./run2/EARTHMOO.aei','./run2/JUPITER.aei',"./run2/earthmoo.png","./run2/jupiter.png","./run2/together.png")
    print(" ")

    # Handling run3 data
    print("Plotting data from run3----------------------")
    dataplotter('./run3/EARTHMOO.aei','./run3/JUPITER.aei',"./run3/earthmoo.png","./run3/jupiter.png","./run3/together.png")
    print(" ")

    # Handling run4 data
    print("Plotting data from run4----------------------")
    dataplotter('./run4/EARTHMOO.aei','./run4/JUPITER.aei',"./run4/earthmoo.png","./run4/jupiter.png","./run4/together.png")
    print(" ")

    # Handling run5 data
    print("Plotting data from run5----------------------")
    dataplotter('./run_5/EARTHMOO.aei','./run_5/JUPITER.aei',"./run_5/earthmoo.png","./run_5/jupiter.png","./run_5/together.png")
    print(" ")

    # Handling run6 data
    print("Plotting data from run6----------------------")
    dataplotter('./run_6/EARTHMOO.aei','./run_6/JUPITER.aei',"./run_6/earthmoo.png","./run_6/jupiter.png","./run_6/together.png")
    print(" ")

    # Handling run7 data
    print("Plotting data from run7----------------------")
    dataplotter('./run_7/EARTHMOO.aei','./run_7/JUPITER.aei',"./run_7/earthmoo.png","./run_7/jupiter.png","./run_7/together.png")
    print(" ")

    # Handling run8 data
    print("Plotting data from run8----------------------")
    dataplotter('./run_8/EARTHMOO.aei','./run_8/JUPITER.aei',"./run_8/earthmoo.png","./run_8/jupiter.png","./run_8/together.png")
    print(" ")

    # Handling run9 data
    print("Plotting data from run9----------------------")
    dataplotter('./run_9/EARTHMOO.aei','./run_9/JUPITER.aei',"./run_9/earthmoo.png","./run_9/jupiter.png","./run_9/together.png")
    print(" ")

    # Handling run10 data
    print("Plotting data from run10----------------------")
    dataplotter('./run_10/EARTHMOO.aei','./run_10/JUPITER.aei',"./run_10/earthmoo.png","./run_10/jupiter.png","./run_10/together.png")
    print(" ")
    '''


    # jupiter Eccentricity changes
    run0_df = create_dataframe("./run_5/EARTHMOO.aei")
    run1_df = create_dataframe("./run1/EARTHMOO.aei")
    run2_df = create_dataframe("./run_6/EARTHMOO.aei")
    run3_df = create_dataframe("./run2/EARTHMOO.aei")
    run4_df = create_dataframe("./run_9/EARTHMOO.aei")
    run5_df = create_dataframe("./run_7/EARTHMOO.aei")

    #starting graph
    fig, ax = plt.subplots(figsize=(7,2))

    ax = run0_df.plot(x ='Time (years)', y='e', kind = 'line', color = 'blue', title = "Earth Sized Planets Eccentricities Based on Jupiter Eccentricities")
    run1_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'red')
    run2_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'green')
    run3_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'yellow')
    run4_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'm')
    run5_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'k')



    ax.legend(["$e_j$ = 0.0","$e_j$ = 0.1", "$e_j$ = 0.2", "$e_j$ = 0.3","$e_j$ = 0.4","$e_j$ = 0.5"],bbox_to_anchor=(1.05, 1))#,title='Jupiter Eccentricities'
    ax.set_ylabel("Eccentricity")
    plt.tight_layout()
    #plt.show()
    plt.savefig("all_Earth_e.png")
    plt.clf()


    #print(run0_df)
    ################################################
    print("STUFFFFFFFFFFFF for e")
    y = [run0_df['e'].mean(),run1_df['e'].mean(),run2_df['e'].mean(),run3_df['e'].mean(),run4_df['e'].mean(),run5_df['e'].mean()]
    x = [0.0,0.1,0.2,0.3,0.4,0.5]
    #Kozai Lidov mechanism
    lower_error = [run0_df['e'].mean()-run0_df['e'].min(),run1_df['e'].mean()-run1_df['e'].min(),run2_df['e'].mean()-run2_df['e'].min(),run3_df['e'].mean()-run3_df['e'].min(),run4_df['e'].mean()-run4_df['e'].min(),run5_df['e'].mean()-run5_df['e'].min()]
    print("Lower Error is ", lower_error)
    upper_error = [run0_df['e'].max(),run1_df['e'].max(),run2_df['e'].max(),run3_df['e'].max(),run4_df['e'].max(),run5_df['e'].max()]
    print("Upper Error is ", upper_error)

    asymmetric_error = [lower_error, upper_error]
    #plt.scatter(x,y)
    plt.errorbar(x,y,yerr=asymmetric_error, fmt='o')
    plt.title("Average of Earth Eccentricities vs Jupiter Eccentricity")
    plt.xlabel("Jupiter Eccentricities")
    plt.ylabel("Average of Earth Eccentricities")
    #plt.show()
    plt.savefig("averageswithej.png")
    plt.clf()
    ################################################


    # jupiter inclination changes
    run0_df = create_dataframe("./run_5/EARTHMOO.aei")
    run1_df = create_dataframe("./run_10/EARTHMOO.aei")
    run2_df = create_dataframe("./run3/EARTHMOO.aei")
    run3_df = create_dataframe("./run_8/EARTHMOO.aei")
    run4_df = create_dataframe("./run4/EARTHMOO.aei")

    #starting graph
    fig, ax = subplots()

    ax = run0_df.plot(x ='Time (years)', y='e', kind = 'line', color = 'blue', title = "Earth Sized Planets Eccentricities Based on Jupiter Inclinations")
    run1_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'red')
    run2_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'green')
    run3_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'yellow')
    run4_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'm')



    ax.legend(["$i_j$ = 0","$i_j$ = 15", "$i_j$ = 30", "$i_j$ = 45","$i_j$ = 60"],bbox_to_anchor=(1.05, 1))#title='Jupiter Inclinations'
    ax.set_ylabel("Eccentricity of Earth Sized Planet")
    plt.tight_layout()
    #plt.show()
    plt.savefig("all_Earth_e_i.png")
    plt.clf()


    # jupiter distance changes---------------------------------------------
    run0_df = create_dataframe("./run_11/EARTHMOO.aei")
    run1_df = create_dataframe("./run_12/EARTHMOO.aei")
    run2_df = create_dataframe("./run_5/EARTHMOO.aei")
    run3_df = create_dataframe("./run_13/EARTHMOO.aei")
    run4_df = create_dataframe("./run_14/EARTHMOO.aei")
    run5_df = create_dataframe("./run_15/EARTHMOO.aei")


    #starting graph
    fig, ax = subplots()

    ax = run0_df.plot(x ='Time (years)', y='e', kind = 'line', color = 'blue', title = "Earth Sized Planets Eccentricities Based on Jupiter Distance")
    run1_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'red')
    run2_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'green')
    run3_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'yellow')
    run4_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'm')
    run5_df.plot(ax=ax, x ='Time (years)', y='e', kind = 'line', color = 'k')



    ax.legend(["$a_j$ = 3.20336","$a_j$ = 4.20336", "$a_j$ = 5.20336", "$a_j$ = 6.20336","$a_j$ = 7.20336","$a_j$ = 8.20336"],bbox_to_anchor=(1.05, 1))#title='Jupiter Inclinations'
    ax.set_ylabel("Eccentricity of Earth Sized Planet")
    plt.tight_layout()
    #plt.show()
    plt.savefig("all_Earth_e_a.png")
    plt.clf()

    y = [run0_df['e'].mean(),run1_df['e'].mean(),run2_df['e'].mean(),run3_df['e'].mean(),run4_df['e'].mean(),run5_df['e'].mean()]
    x = [3.20336,4.20336,5.20336,6.20336,7.20336,8.20336]
    #Kozai Lidov mechanism
    lower_error = [run0_df['e'].mean()-run0_df['e'].min(),run1_df['e'].mean()-run1_df['e'].min(),run2_df['e'].mean()-run2_df['e'].min(),run3_df['e'].mean()-run3_df['e'].min(),run4_df['e'].mean()-run4_df['e'].min(),run5_df['e'].mean()-run5_df['e'].min()]
    print("Lower Error is ", lower_error)
    upper_error = [run0_df['e'].max(),run1_df['e'].max(),run2_df['e'].max(),run3_df['e'].max(),run4_df['e'].max(),run5_df['e'].max()]
    print("Upper Error is ", upper_error)

    asymmetric_error = [lower_error, upper_error]
    #plt.scatter(x,y)
    plt.errorbar(x,y,yerr=asymmetric_error, fmt='o')
    plt.title("Average of Earth Eccentricities vs Jupiter Eccentricity")
    plt.xlabel("Jupiter Distances")
    plt.ylabel("Average of Earth Eccentricities")
    #plt.show()
    plt.savefig("averageswithia.png")
    plt.clf()





    print("STUFFFFFFFFFFFF for i")
    y = [run0_df['e'].mean(),run1_df['e'].mean(),run2_df['e'].mean(),run3_df['e'].mean(),run4_df['e'].mean()]
    x = [0,15,30,45,60]
    #Kozai Lidov mechanism
    lower_error = [run0_df['e'].mean()-run0_df['e'].min(),run1_df['e'].mean()-run1_df['e'].min(),run2_df['e'].mean()-run2_df['e'].min(),run3_df['e'].mean()-run3_df['e'].min(),run4_df['e'].mean()-run4_df['e'].min()]
    print("Lower Error is ", lower_error)
    upper_error = [run0_df['e'].max(),run1_df['e'].max(),run2_df['e'].max(),run3_df['e'].max(),run4_df['e'].max()]
    print("Upper Error is ", upper_error)

    asymmetric_error = [lower_error, upper_error]
    #plt.scatter(x,y)
    plt.errorbar(x,y,yerr=asymmetric_error, fmt='o')
    plt.title("Average of Earth Eccentricities vs Jupiter Eccentricity")
    plt.xlabel("Jupiter Inclinations")
    plt.ylabel("Average of Earth Eccentricities")
    #plt.show()
    plt.savefig("averageswithij.png")
    plt.clf()

if __name__== "__main__":
    main()
