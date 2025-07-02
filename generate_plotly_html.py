import os
import pandas as pd
import plotly.express as px

# Define your objectives (replace with your actual objective names)
OBJECTIVES = ["Subset size", "Accuracy", "DP", "EO"]

# Input and output directories
DATA_DIR = 'data'
ONLINE_PLOTS_DIR = 'online_plots'
os.makedirs(ONLINE_PLOTS_DIR, exist_ok=True)

# List of your dataset files (or iterate through DATA_DIR)
dataset_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
dataset_files.sort() # Ensure consistent order

html_links = [] # To build the index.html content

for filename in dataset_files:
    dataset_name = os.path.splitext(filename)[0] # e.g., 'adult'
    html_filename = f"{dataset_name}.html"
    output_path = os.path.join(ONLINE_PLOTS_DIR, html_filename)

    print(f"Generating plot for {dataset_name}...")

    try:
        df = pd.read_csv(os.path.join(DATA_DIR, filename), sep=";")

        # Ensure the DataFrame has the expected objective columns
        if not all(obj in df.columns for obj in OBJECTIVES):
            print(f"Warning: {filename} does not contain all specified objectives. Skipping.")
            continue

        fig = px.parallel_coordinates(df,
                                     dimensions=OBJECTIVES,
                                     color=OBJECTIVES[0], # Color by the first objective, or pick another
                                     color_continuous_scale=px.colors.sequential.Viridis,
                                     title=f"Pareto Front for {dataset_name.replace('_', ' ').title()}")

        # Further customizations for interactivity (optional, but good practice)
        fig.update_layout(
            hovermode="x unified", # Tooltips show all objective values for a hovered solution
            title_font_size=18,
            margin=dict(l=80, r=80, t=80, b=80),
            paper_bgcolor='rgba(0,0,0,0)', # Transparent background
            plot_bgcolor='rgba(0,0,0,0)'
        )

        # Save the interactive HTML file
        fig.write_html(output_path, include_plotlyjs='cdn') # 'cdn' loads Plotly.js from a CDN

        html_links.append(f'<li><a href="{html_filename}">{dataset_name.replace("_", " ").title()}</a></li>')
        print(f"Successfully generated {html_filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Create an index.html file to list all plots
index_html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Many-Objective Optimization Pareto Fronts</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; margin: 20px; }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; }}
        a {{ text-decoration: none; color: #007bff; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Interactive Pareto Front Visualizations</h1>
    <p>This repository contains interactive parallel coordinate plots for the Pareto fronts obtained from many-objective feature selection optimization across 16 datasets.</p>
    <p>Click on a dataset name below to view its interactive plot. Use your mouse to zoom, pan, and hover over lines to see detailed objective values for each solution.</p>
    <h2>Datasets:</h2>
    <ul>
        {''.join(html_links)}
    </ul>
    <p>Return to <a href="https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME">GitHub Repository</a></p>
    <p>Learn more about the research in the <a href="YOUR_THESIS_URL_IF_AVAILABLE">full thesis</a>.</p>
</body>
</html>
"""

with open(os.path.join(ONLINE_PLOTS_DIR, 'index.html'), 'w') as f:
    f.write(index_html_content)
print(f"Generated {ONLINE_PLOTS_DIR}/index.html")