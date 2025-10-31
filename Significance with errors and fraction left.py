# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:17:40 2023

@author: 44759
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from Excel spreadsheet
excel_path = r"C:\Users\44759\Documents\Y4 PROJECT\V0_Significance_data.xlsx"
sheet_name = "dcanegtopv"
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# Extract data from columns
cut_values = df['Cut'][0:11]
cut_values1 = df['Cut'][2:9]
significance_values = df['Significance'][0:11]
significance_values1 = df['Significance'][2:9]
error_values = df['Error'][0:11]
fraction_left_values = df['Frac Left'][0:11]
MC_fraction_left_values = df['MCTR FL'][0:11]

# Fit the data with a 2nd order polynomial
coefficients = np.polyfit(cut_values1, significance_values1, 2)
poly_fit = np.poly1d(coefficients)

# Generate more points for the fitted curve
fit_values_smooth = poly_fit(np.linspace(min(cut_values1), max(cut_values1), 100))

# Calculate the maximum point of the fitted curve
a = coefficients[0]
b = coefficients[1]
max_cut_value = -b / (2 * a)

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)

# Plot significance against cut with error bars
ax1.errorbar(cut_values, significance_values, yerr=error_values, color='green', label='Error bars', linestyle='None')
ax1.scatter(cut_values, significance_values, color='red', label='Significance')
ax1.plot(np.linspace(min(cut_values1), max(cut_values1), 100), fit_values_smooth, '--k')  # Plot the smooth fit
ax1.axvline(x=max_cut_value, color='grey', linestyle='--', label='Optimal cut = 0.10145311')  # Vertical line at the maximum point
ax1.set_ylabel('Significance, ' r'$\frac{S}{\sqrt{S + B}}$')
#ax1.set_title('Significance of $K^0_s$ mass plot and signal loss fraction against DCAnegtoPV cut')
ax1.legend(loc='lower right')

# Plot fraction left against cut
ax2.plot(cut_values, fraction_left_values, '.', color='red', label='data')
ax2.plot(cut_values, MC_fraction_left_values, '.', color='blue', label='MC')
ax2.axvline(x=max_cut_value, color='grey', linestyle='--')
ax2.set_xlabel('DCAnegtoPV Cut (≥) [cm]')
ax2.set_ylabel('Frac. of sig. remaining')
#ax2.set_title('Fraction Left vs. Cut')
ax2.legend()

# Add a dotted grid
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()

# Print the best fit coefficients
print("Best Fit Coefficients:", coefficients)
print("Max sig cut:", max_cut_value)
