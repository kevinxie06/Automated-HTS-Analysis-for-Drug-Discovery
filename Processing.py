import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Kevin Xie

# Import the data file

# This function simply processes the excel sheet into a data frame
# Ignore
def process_excel(data_path, columns, sheet):

    return pd.read_excel(data_path, usecols = columns, sheet_name= sheet)

    # The following gives all data entries in column B print(data_frame.iloc[1])
    # The following gives all entires in ROW B print(data_frame.iloc[[1]]). For rows, you should start at index 0

    # Gives the entry in the first row, column 24, 126135: print(data_frame.iloc[0, 24])

    

def plot_standard_curve():

    # Process desired excel sheet
    data_path = '/Users/kevinxie/Desktop/Personal Projects/Data Analysis Project/Data/IL-2_CBLB_Jurkat_HTS_20240125 Jurkat Pharmaron array 20uM plate2 40min.xlsx'
    columns = [i**1 for i in range(0,25)]
    sheet = "Sheet1"

    data_frame = process_excel(data_path, columns, sheet)

    # Averaging every two rows in column 24; creates a list that stores these averages.
    average_standard_curve_list = []
    counter = 0
    total = 0
    for i in range(0, 16):
        if i == 15:
            total += data_frame.iloc[i, 24]
            average_standard_curve_list.append(total / 2)
            #print(data_frame.iloc[i, 24])

        elif counter < 2:
            total += data_frame.iloc[i, 24]  
            #print(data_frame.iloc[i, 24])
            counter += 1

        elif counter == 2:
            average_standard_curve_list.append(total / 2)
            total = 0
            counter = 0

            total += data_frame.iloc[i, 24]  
            #print(data_frame.iloc[i, 24])
            counter += 1


    # Plot the averages in a scatterplot
    x = np.array([7, 6, 5, 4, 3, 2, 1, 0])
    y = np.array(average_standard_curve_list)
    plt.plot(x, y, 'o')

    # Obtain m (slope) and b(intercept) of linear regression line 
    m, b = np.polyfit(x, y, 1)
    
    # Graph formatting
    plt.title(f"Standard Curve \n y = {m}x + {b}'")
    plt.ylabel('RLU')
    plt.xlabel('X Axis')

    # Line of best fit
    plt.plot(x, m * x, color = 'red')

    for i, j in zip(x, y):
        plt.text(i, j+0.5, '({}, {})'.format(i, j), )

    # Plot show
    plt.show()


# Call function
plot_standard_curve()




# x = [7, 6, 5, 4, 3, 2, 1, 0]
# y = average_standard_curve_list
# Converting m, a numpy.float, into a python float, and then into an int.
# m = int(m.item())









