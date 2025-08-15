# marimo==0.8.15
# Author: Data Scientist @ Research Institution
# Contact: 24f2001293@ds.study.iitm.ac.in
#
# This Marimo notebook demonstrates interactive, self-documenting analysis
# of the relationship between variables in a synthetic dataset.
# Data flow overview:
#   - Cell 1: Imports & App initialization (no outputs)
#   - Cell 2: UI widget definitions (slider controlling noise level)
#   - Cell 3: Data generation depends on slider value (reactive)
#   - Cell 4: Visualization depends on generated data
#   - Cell 5: Dynamic markdown summary depends on computed statistics
#   - Cell 6: (optional) Table preview depends on data
#
# Variable dependency chain:
#   slider_noise -> (noise_level) -> (x, y, df) -> (fig, corr) -> (md_summary)
#
# To run:
#   pip install marimo matplotlib pandas numpy
#   marimo run this_file.py      # launches the interactive app in your browser
#   marimo edit this_file.py     # opens editor to view cells

import marimo as mo

__generated_with = "0.8.15"
app = mo.App()

@app.cell
def _():
    # Core imports
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from io import BytesIO

    # Utility: compute Pearson correlation
    def pearson_corr(x, y):
        # Small guard for constant arrays
        if np.std(x) == 0 or np.std(y) == 0:
            return 0.0
        return float(np.corrcoef(x, y)[0, 1])

    return np, pd, plt, BytesIO, pearson_corr
# Commentary: This cell defines foundation utilities used by downstream cells.

@app.cell
def _():
    # --- UI WIDGETS ---
    # Interactive slider controlling noise level in data generation.
    # Range 0.0 (perfect linear) to 2.0 (high noise).
    slider_noise = mo.ui.slider(0.0, 2.0, value=0.6, step=0.05, label="Noise level (σ)")
    # Expose widget to the UI
    mo.hstack([slider_noise, mo.md("Use the slider to control noise added to y = 3x + 5 + ε")])
    return slider_noise
# Commentary: This cell emits the UI. Downstream cells access slider_noise.value reactively.

@app.cell
def _(np, pd, slider_noise):
    # --- DATA GENERATION (reactive) ---
    rng = np.random.default_rng(42)
    n = 200
    x = rng.uniform(-5, 5, n)
    sigma = float(slider_noise.value)  # <-- dependency on widget
    noise = rng.normal(0, sigma, n)
    y = 3 * x + 5 + noise

    # Build DataFrame for convenience
    df = pd.DataFrame({"x": x, "y": y})

    # Expose variables to downstream cells
    return x, y, df, sigma
# Commentary: This cell depends on slider_noise and produces x, y, df, sigma.

@app.cell
def _(plt, x, y, sigma, pearson_corr):
    # --- VISUALIZATION ---
    # Single-figure scatter plot with regression line (via least squares)
    # NOTE: Avoid specifying colors to comply with style guidance.
    fig, ax = plt.subplots(figsize=(5, 4))

    # Scatter
    ax.scatter(x, y, alpha=0.7)

    # Fit simple linear regression y = a*x + b using least squares
    # (without external libs, keeps the notebook self-contained)
    X = np.vstack([x, np.ones_like(x)]).T
    a, b = np.linalg.lstsq(X, y, rcond=None)[0]
    xx = np.linspace(min(x), max(x), 100)
    yy = a * xx + b
    ax.plot(xx, yy, linewidth=2)

    ax.set_title("Relationship between x and y with adjustable noise")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)

    corr = pearson_corr(x, y)

    fig
    return fig, corr, a, b
# Commentary: This cell depends on (x, y, sigma) and produces (fig, corr, a, b).

@app.cell
def _(mo, sigma, corr, a, b):
    # --- DYNAMIC MARKDOWN OUTPUT ---
    strength = (
        "very strong" if abs(corr) > 0.9 else
        "strong" if abs(corr) > 0.7 else
        "moderate" if abs(corr) > 0.5 else
        "weak" if abs(corr) > 0.3 else
        "very weak"
    )
    interpretation = (
        "As noise increases, points scatter further from the regression line, reducing correlation."
    )
    md = mo.md(f"""
### Summary

- **Selected noise (σ):** `{sigma:.2f}`  
- **Pearson r:** `{corr:.3f}` → *{strength}* linear relationship  
- **Estimated model:** `y ≈ {a:.2f} x + {b:.2f}`

{interpretation}

> Try lowering σ towards 0.0 for a tight, nearly perfect linear trend; raise it towards 2.0 to weaken the relationship.
""")
    md
    return md
# Commentary: This cell depends on (sigma, corr, a, b) and renders an executive summary.

@app.cell
def _(mo, df):
    # --- OPTIONAL: DATA PREVIEW ---
    mo.accordion({
        "Peek at the data (first 10 rows)": mo.ui.table(df.head(10))
    })
    return
# Commentary: This cell depends on df and provides a reactive preview.

if __name__ == "__main__":
    app.run()