# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:53:03 2024

@author: 44759
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load data from Excel spreadsheet
excel_path = r"C:\Users\44759\Documents\Y4\Y4 PROJECT\Lambda_Significance_data.xlsx"
sheet_name = "v0rad"
df = pd.read_excel(excel_path, sheet_name=sheet_name)

a=0
b=22
c=8
d=13

# Extract data from columns
cut_values = df['Cut'][a:b]
cut_values1 = df['Cut'][c:d]
significance_values = df['Significance'][a:b]
significance_values1 = df['Significance'][c:d]
error_values = df['Error'][a:b]
fraction_left_values = df['Frac Left'][a:b]
MC_fraction_left_values = df['MCTR FL'][a:b]

# Define the significance function
def significance_function(cut, a, b, c):
    return a * cut**2 + b * cut + c

# Fit the data with a 2nd order polynomial using curve_fit
params, covariance = curve_fit(significance_function, cut_values1, significance_values1, sigma=error_values[c:d])

# Extract the fit parameters
a_fit, b_fit, c_fit = params

# Generate more points for the fitted curve
fit_values_smooth = significance_function(np.linspace(min(cut_values1), max(cut_values1), 100), a_fit, b_fit, c_fit)

# Calculate the maximum point of the fitted curve
max_cut_value = -b_fit / (2 * a_fit)

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)

# Plot significance against cut with error bars
ax1.errorbar(cut_values, significance_values, yerr=error_values, color='green', label='Error bars', linestyle='None')
ax1.plot(cut_values, significance_values, '.', color='red', label='Significance')
ax1.axvline(x=1.4, color='purple', linestyle='--', label='Cut = 1.4')
ax1.plot(np.linspace(min(cut_values1), max(cut_values1), 100), fit_values_smooth, '--k')  # Plot the smooth fit
ax1.axvline(x=max_cut_value, color='grey', linestyle='--', label=f'Optimal cut = {max_cut_value:.8f}')  # Vertical line at the maximum point
#max_cut_value
ax1.set_ylabel('Significance, ' r'$\frac{S}{\sqrt{S + B}}$')
ax1.legend()
#loc='upper left'
# Plot fraction left against cut
ax2.plot(cut_values, fraction_left_values, '.', color='red', label='data')
#ax2.plot(cut_values, MC_fraction_left_values, '.', color='blue', label='MC')
ax2.axvline(x=max_cut_value, color='grey', linestyle='--')
ax2.axvline(x=1.4, color='purple', linestyle='--')

#max_cut_value
ax2.set_xlabel('Lambda v0radius Cut [cm]')
ax2.set_ylabel('Frac. of sig. remaining')
ax2.legend()


# Add a dotted grid
ax1.grid(True, linestyle='--', alpha=0.5)
ax2.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

#plt.savefig('v0radius_Lambda_significance_plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()


# Print the best fit coefficients
print("Best Fit Coefficients:", a_fit, b_fit, c_fit)

print("Max sig cut:", max_cut_value)
