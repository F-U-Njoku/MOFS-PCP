# Many-Objective Feature Selection - Parallel Coordinate Plots

## Exploring Pareto Fronts on Fairness Datasets

This repository presents interactive visualizations of the results from a Many-Objective Feature Selection (MOFS) optimization process applied across 16 diverse fairness datasets.

The core of this work involves optimizing for multiple, often conflicting, objectives simultaneously. This leads to a set of non-dominated solutions (the Pareto front), where improving one objective typically means compromising another. Understanding these trade-offs is crucial for selecting the most appropriate feature subset for a given application.

### Interactive Visualizations

To facilitate an exploration of these trade-offs, we provide interactive Parallel Coordinate Plots (PCPs) for each of the 16 datasets. PCPs are a useful tool for visualizing high-dimensional data, allowing users to:

* **See Objective Trade-offs:** Observe the relationships and conflicts between the four optimization objectives (e.g., Accuracy, Fairness, Feature Count, Model Complexity).
* **Identify Optimal Solutions:** Pinpoint solutions that represent favorable compromises across the objectives.
* **Explore Solution Diversity:** Understand the range and distribution of the obtained non-dominated solutions.

**👉 Explore the interactive plots here: [https://f-u-njoku.github.io/MOFS-PCP/](https://f-u-njoku.github.io/MOFS-PCP/)**

### Repository Contents

* **`online_plots/`**: Contains the individual HTML files for each dataset's interactive Parallel Coordinate Plot, generated using Plotly.
* **`data/`**: Stores the raw Pareto front data (CSV files) for all 16 datasets, which were used to generate the visualizations.
* **`scripts/`**: Includes the Python script (`generate_plotly_html.py`) used to automate the generation of the interactive plots.

### About the Project

This work is part of a thesis exploring advanced optimization techniques for feature selection in the context of fairness-aware machine learning. The analysis within the thesis discusses representative examples in detail, while this repository serves as a supplementary resource for a complete and interactive exploration of all results.