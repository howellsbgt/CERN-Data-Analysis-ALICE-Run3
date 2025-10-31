# Source Code Overview

This folder contains the core Python scripts used for the V⁰ (K⁰<sub>S</sub> and Λ) analysis and optimisation workflow.

## Structure

| Script | Purpose |
|--------|----------|
| `batch_apply_v0_cuts.py` | Automates batch application of selection cuts to JSON configs and runs reconstruction macros. |
| `cut_optimisation_plot.py` | Basic quadratic fit of significance vs. cut using NumPy (unweighted). |
| `cut_optimisation_curvefit.py` | Weighted quadratic fit using SciPy for more accurate cut optimisation. |
| `cut_optimisation_curvefit_lambda_v0radius.py` | Λ analysis script: optimises v0radius cut and compares fixed vs. optimal cuts visually. |

## Usage
Each script can be run independently after activating the `alienv` environment and ensuring the relevant data/Excel files are available.

Example:
```bash
python cut_optimisation_curvefit_lambda_v0radius.py
