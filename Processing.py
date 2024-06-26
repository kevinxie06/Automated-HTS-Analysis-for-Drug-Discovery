import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Kevin Xie

# Processes the excel sheet
def process_excel(data_path, columns, sheet):

    return pd.read_excel(data_path, usecols = columns, sheet_name = sheet)

def plot_standard_curve(data_path, sheet):
    columns = [i for i in range(0,25)]

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

    # DMSO Calculation
    DMSO_total = 0
    for row in range(0,2):
        for column in range(1,3):
            DMSO_total += data_frame.iloc[row, column]

    for row in range(14,16):
        for column in range(1,3):
            DMSO_total += data_frame.iloc[row, column]

    # Non-stimulation calculation
    non_stim = 0
    for row in range(0, 16):
        non_stim += data_frame.iloc[row, 23]

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

    # Show legend and plot
    plt.legend()
    plt.show()

    return m, background, DMSO_total, non_stim

# Plots the positive control curve
def plot_positive_control(data_path, sheet):
    columns = [1, 2]
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
        x.append(math.log10((2.5/(2**i))))

    y = (averaged_positive_control)

    # Best-fit curve
    curve = np.polyfit(x, y, 5)
    x = np.array(x)

    poly_y = (curve[0]* x**5) + (curve[1]* x**4)+ (curve[2]*x**3) + (curve[3]*x**2) + (curve[4]*x) + (curve[5])

    # Max and EC-50
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
        ec_50 = round(ec_50[0], 3)
    
    ec_50 = 10**ec_50
    ec_50 = round(ec_50, 3)
    
    maximum = round(maximum, 3)

    # Chart labels
    plt.xlabel('uM (log10)')
    plt.ylabel('RLU')
    plt.title(f'Positive Control Curve\nMax = {maximum}\nEC-50 = {ec_50} uM')

    plt.plot(x, y, 'o', label = 'Data points')
    plt.plot(x, poly_y, label = 'Nonlinear regression line')
    plt.legend()

    plt.show()

    # Plug in data points from plate into the equation from part 1 to get 320 new points.
    # plot on IL-2 vs. Compound number (1 - 320)
def plot_data(data_path, sheet):
    
    # Get the slope and background values calculated from standard curve
    slope, background, DMSO, non_stim = plot_standard_curve(data_path, sheet)

    columns = [i for i in range(3, 23)]

    data_frame = process_excel(data_path, columns, sheet)

    # Creating axes
    x_axis = [i for i in range(1, 321)]
    y_axis = []
   
    # Equation: RLU = m(x) + background
    for row in range(0, 16):
        for column in range(0, 20):
            y_axis.append((data_frame.iloc[row, column] - background) / slope)
            
    # Standard deviation
    standard_deviation = np.std(y_axis)

    # DMSO averaged
    avg_DMSO = DMSO / 8

    # Plug DMSO into IL-2 equation
    DMSO_value = ((avg_DMSO - background) / slope)

    # Non-stimulation; 16 non-stim entries
    avg_non_stim =  non_stim / 160

    # Graph labels
    plt.title('IL-2 CBLB Jurkat HTS Jurkat Pharmaron Array 20uM')
    plt.xlabel('Compound Number')
    plt.ylabel('IL-2 (pg/ml)')
    plt.xticks([20*i for i in range(0,20)])

    # Plots
    plt.plot(x_axis, y_axis, 'o', label = 'Data Points')
    plt.axhline(3*standard_deviation, 0, 1, linestyle = '--', color = 'red', label = '3 x Standard deviation')
    plt.axhline(DMSO_value, 0, 1, linestyle = '--', color = 'green', label = 'DMSO')
    plt.axhline(avg_non_stim, 0, 1, linestyle = '--', color = 'black', label = 'Non-Stimulation')

    # Show
    plt.legend()
    plt.show()


data_path = '/Users/kevinxie/Desktop/Personal Projects/Data Analysis Project/Data/IL-2 CBLB Jurkat HTS Jurkat Pharmaron Array 20uM.xlsx'
sheet = 'Sheet1'

# Function call
plot_standard_curve(data_path, sheet)
plot_positive_control(data_path, sheet)
plot_data(data_path, sheet)








