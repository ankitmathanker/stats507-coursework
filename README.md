# STATS 507 Coursework Final Project

This repository contains the final project materials for STATS 507. The
analysis compares computed molecular, slab, and adsorption energies across
methods and explores delta-learning models for adsorption-energy correction.

The repository includes analysis notebooks, generated figures, tabular model
outputs, sample calculation inputs, and the final report.

## Repository Contents

- `energy_analysis.ipynb` - main notebook for energy comparison, parity plots,
  adsorption-energy analysis, and system-level visualizations.
- `delta_learning_adsorption.ipynb` - notebook for fitting and evaluating
  delta-learning models for adsorption energies.
- `energies_comparison.xlsx` - source workbook used by the energy-analysis
  notebook.
- `delta_values_from_adsorption_sheet.csv` - extracted delta values used for
  adsorption-energy modeling.
- `delta_learning_metrics.csv` - summary metrics from the delta-learning
  experiments.
- `delta_learning_predictions_oof.csv` - out-of-fold predictions from the
  delta-learning workflow.
- `figures/` - exported plots used in the analysis and report.
- `sample calculation/` - example OC25 calculation script, POSCAR inputs, and
  sample energy output.
- `OC25_SPC.tar` and `UMA.tar` - archived project data/assets.
- `Report.pdf` - final written report.
- `run_oc25_test_script.py` - example OC25 calculation script.
- `requirements.txt` - python packages required for the analysis and sample calculation.