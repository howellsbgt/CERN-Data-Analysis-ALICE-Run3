# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:27:03 2024

@author: 44759

cut_optimisation_curvefit.py
----------------------------
Performs weighted quadratic fit of significance vs. cut parameter for V0 selection optimisation.

- Loads data from Excel sheet.
- Fits using scipy.optimize.curve_fit with error weighting.
- Plots significance with best-fit curve and fractional signal retention.
- Outputs best-fit parameters and optimal cut value.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load data from Excel spreadsheet
excel_path = r"C:\Users\44759\Documents\Y4\Y4 PROJECT\V0_Significance_data.xlsx"
sheet_name = "dcanegtopv#1"
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# Extract data from columns
cut_values = df['Cut'][0:22]
cut_values1 = df['Cut'][1:9]
significance_values = df['Significance'][0:22]
significance_values1 = df['Significance'][1:9]
error_values = df['Error'][0:22]
fraction_left_values = df['Frac Left'][0:22]
MC_fraction_left_values = df['MCTR FL'][0:22]

# Define the significance function
def significance_function(cut, a, b, c):
    return a * cut**2 + b * cut + c

# Fit the data with a 2nd order polynomial using curve_fit
params, covariance = curve_fit(significance_function, cut_values1, significance_values1, sigma=error_values[1:9])

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
#max_cut_value
ax2.set_xlabel('dcanegtopv #1 Cut [cm]')
ax2.set_ylabel('Frac. of sig. remaining')
ax2.legend()


# Add a dotted grid
ax1.grid(True, linestyle='--', alpha=0.5)
ax2.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

#plt.savefig('dcanegtopv#1_K0_significance_plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()


# Print the best fit coefficients
print("Best Fit Coefficients:", a_fit, b_fit, c_fit)
print("Max sig cut:", max_cut_value)

