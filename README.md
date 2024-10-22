# Automated Analysis of High-Throughput Screening for Drug Discovery 

## Overview
The process of drug discovery via high-throughput screening (HTS) is *lengthy* and *resource-intensive*.

For example, many chemical libraries have **hundreds of thousands of compounds** that researchers must *manually* analyze to identify potential new medicines that can safety hit intracellular targets and cure diseases.

**To address this**, I developed a Python program that **automatically processes high-throughput screening results and identifies the most effective drug candidates**.

The goal of this project is to **accelerate drug discovery**, ultimately **enhancing medicines** and **improving patient outcomes**.

## Data Description
This section provides an overview of the data used for the project.

- **Excel Sheet Input**: All HTS results were stored in an Excel sheet.

- **Cell Line**: Jurkat cells, a human T lymphocyte cell line, were used for the experiments. These cells are commonly employed in immunological research due to their well-characterized response to stimuli.

- **Cytokine Measurement**: Interleukin-2 (IL-2) concentrations were measured, as IL-2 is a key cytokine in immune response modulation. The data represents IL-2 levels quantified in picograms per milliliter (pg/ml).

- **Positive Control**: The positive control curve data was used to generate a standard curve plotting Relative Light Units (RLU) against IL-2 concentrations (pg/ml). This curve helps determine the EC-50 and validate assay performance.

- **High-Throughput Screening (HTS) Data**: High-throughput screening was employed to assess a large number of compounds for their effect on IL-2 production in Jurkat cells. The data includes RLU measurements for each compound at various concentrations.


## Requirements
### Installation
Python 3.9+ and the following packages are required:
- [Python](https://www.python.org/downloads/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

Install the necessary dependencies using:
```
pip install pandas
```
```
pip install numpy
```
```
pip install matplotlib
```

## Key Features
### Drug Discovery

- **Plots IL-2 Concentrations**: Visualizes the concentration of IL-2 for each compound.

- **Calculate and Plot Variability**: Computes and displays the **standard deviation**, [Dimethyl Sulfoxide (DMSO) concentration](https://www.acs.org/molecule-of-the-week/archive/d/dimethyl-sulfoxide.html#:~:text=In%20the%201960s%2C%20scientists%20observed,systems%20(i.e.%2C%20patches).) and **Non-Stimulation** concentrations.

- **Visualization of potential drug candidates**: Dots above the STD, DMSO, and Non-Stim lines indicate highly active and statistically significant compounds.

<p align = "center">
<img width="800" alt="Sample IL2 Plot" src="https://github.com/kevinxie06/Automated-HTS-Analysis-for-Drug-Discovery/assets/135569406/80cc5d85-5df8-476d-a3ea-fb9d4901b12a">

### Experiment Validation and EC-50

- **Generate Positive Control Curve**: Plots the Relative Light Units (RLU) versus micromolar (µM) concentration to visualize the response of the positive control samples.

- **EC-50 Calculation**: Determines the EC-50 (half-maximal effective concentration), which signifies the concentration of a compound where 50% of its maximal effect is observed. This is crucial for assessing the potency of the compound and convenient way of comparing drug potencies.

- **Sigmoidal Dose-Response Curve**: Proper experiments should expect a characteristic S-shaped curve.

- **Evaluate Experimental Accuracy**: Use the positive control curve to validate the accuracy and reliability of experimental results, ensuring consistent and reproducible outcomes.


<p align = "center">
<img width="800" alt="Positive Control Curve" src="https://github.com/kevinxie06/Data-Analysis-Project/assets/135569406/55131730-46eb-494b-9a8b-f3eaae2f4dab">


### Determine Concentration of an Unknown Sample

- **Quantification of IL-2 Concentration**: Accurately determine the concentration of IL-2 in unknown samples by comparing their Relative Light Units (RLU) to the standard curve.

- **Validation of Assay Sensitivity and Performance**: Ensure the assay is performing correctly and sensitively within a defined range by establishing a reliable relationship between RLU and known IL-2 concentrations.

- **Normalization and Quality Control**: Use the standard curve to normalize data across different experiments and maintain quality control, identifying any inconsistencies or deviations in the assay.


<p align = "center">
<img width="800" alt="Standard Curve Plot" src="https://github.com/kevinxie06/Data-Analysis-Project/assets/135569406/286b3f20-23a4-4384-9c62-c6ab0f199a24">


Thank you for considering my work and using my program! I hope it aids your research in drug discovery!

I am also welcome to any contributions! If you encounter any issues, please contact me at kevinxie2024@gmail.com.

Kevin Xie

