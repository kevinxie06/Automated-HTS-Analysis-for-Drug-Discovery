import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Kevin Xie

# Processes the excel sheet
def process_excel(data_path, columns, sheet):

    return pd.read_excel(data_path, usecols = columns, sheet_name= sheet)

    # The following gives all data entries in column B print(data_frame.iloc[1])
    # The following gives all entires in ROW B print(data_frame.iloc[[1]]). For rows, you should start at index 0
    # Gives the entry in the first row, column 24, 126135: print(data_frame.iloc[0, 24])

def plot_standard_curve():

    # Process desired excel sheet
    data_path = '/Users/kevinxie/Desktop/Personal Projects/Data Analysis Project/Data/IL-2_CBLB_Jurkat_HTS_20240125 Jurkat Pharmaron array 20uM plate2 40min.xlsx'
    columns = [i for i in range(0,25)]
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

        elif counter < 2:
            total += data_frame.iloc[i, 24]  
            counter += 1

        elif counter == 2:
            average_standard_curve_list.append(total / 2)
            total = 0
            counter = 0

            total += data_frame.iloc[i, 24]  
            counter += 1

    # Plot the averages in a scatterplot
    # X-axis values consist of IL-2 (pg/ml)
    x = np.array([25000, 8065, 2601, 839, 271, 87.3, 28.2, 0])
    y = np.array(average_standard_curve_list)

    # Obtain m (slope) and b (intercept) of linear regression line 
    m, b = np.polyfit(x, y, 1)

    # Calculates background RLU
    background = (data_frame.iloc[15,24] + data_frame.iloc[15, 24])/2
    
    # Graph formatting
    plt.title(f"Standard Curve \n y = {round(m, 4)}x + {background}")
    plt.ylabel('RLU')
    plt.xlabel('IL-2 (pg/ml)')

    # Plot data points
    plt.plot(x, y, 'o', label = "Data points")

    # Plots line of best fit
    plt.plot(x, m * x, color = 'red', label = 'Linear regression')

    # # Labels for each data point; may not be necessary
    # for i, j in zip(x, y):
    #     plt.text(i, j+0.5, '({}, {})'.format(i, j), )

    # Show legend and plot
    plt.legend()
    plt.show()


# Plots the positive control curve
def plot_positive_control():
    
    data_path = '/Users/kevinxie/Desktop/Personal Projects/Data Analysis Project/Data/IL-2_CBLB_Jurkat_HTS_20240125 Jurkat Pharmaron array 20uM plate2 40min.xlsx'
    columns = [1, 2]
    sheet = "Sheet1"
    data_frame = process_excel(data_path, columns, sheet)
    
    # Averages the positive control; stores in new list
    averaged_positive_control = []
    total = 0

    # First and last two rows are not used
    for row in range(2, 14):
        if row == 15:
            total = data_frame.iloc[row, 0] + data_frame.iloc[row, 1]
            averaged_positive_control.append(total / len(columns))
            break
        else:
            total = data_frame.iloc[row, 0] + data_frame.iloc[row, 1]
            averaged_positive_control.append(total / len(columns))

            total = 0

    # Plot
    # Axes: x axis -> micromolar concetration values (set by experimenter)
    x = []
    for i in range(0,12):
        x.append(2.5/(2**i))
    y = (averaged_positive_control)

    # Best-fit curve
    curve = np.polyfit(x, y, 5)
    polynomial_equation = np.poly1d(curve)
    x = np.array(x)

    poly_y = (curve[0]* x**5) + (curve[1]* x**4)+ (curve[2]*x**3) + (curve[3]*x**2) + (curve[4]*x) + (curve[5])

    # Max and EC-50 (When Max = 50%, what is the x-axis value)
    maximum = max(y)
    half_max = maximum/2

    # Finds the roots of the equation when max/2
    roots = np.roots([curve[0], curve[1], curve[2], curve[3], curve[4], curve[5] - half_max])

    # Select the real root
    real_roots = roots[np.isreal(roots)].real

    ec_50 = []
    # Searches for the root within the domain of the function
    for root in real_roots:
        if root >= min(x) and root <= max(x):
            ec_50.append(root)

    # Rounding max and EC50
    if len(ec_50) == 1:
        ec_50 = round(ec_50[0], 5)
    maximum = round(maximum, 3)

    # Chart labels
    plt.xlabel('uM')
    plt.ylabel('RLU')
    plt.title(f'Positive Control Curve\nMax = {maximum}\nEC-50 = {ec_50}')

    plt.plot(x, y, 'o', label = 'Data points')
    plt.plot(x, poly_y, label = 'Nonlinear regression line')
    plt.legend()

    plt.show()

            
# Call function
plot_standard_curve()
plot_positive_control()








