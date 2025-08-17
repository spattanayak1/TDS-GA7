import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")

# ==========================================================
# Cell 1: Import Marimo library
# OUTPUT: mo (used in later cells for widgets and markdown)
# ==========================================================
@app.cell
def _():
    import marimo as mo
    return (mo,)


# ==========================================================
# Cell 2: Create slider widget
# OUTPUT: slider (used in Cell 3 for dynamic markdown)
# ==========================================================
@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100)  # Slider between 1 and 100
    return (slider,)


# ==========================================================
# Cell 3: Dynamic markdown based on slider value
# INPUT: slider (from Cell 2)
# OUTPUT: Shows slider value + green dots
# ==========================================================
@app.cell
def _(mo, slider):
    mo.md(f"{slider} {'🟢' * slider.value}")
    return


# ==========================================================
# Cell 4: Dynamic markdown combining x and y
# INPUT: x (from Cell 5), y (from Cell 6)
# OUTPUT: Statement referencing x and y
# ==========================================================
@app.cell
def _(mo, x, y):
    mo.md(f"Let's find the product of {x} and {y} along with 5")
    return


# ==========================================================
# Cell 5: Define variable x
# OUTPUT: x (used in Cell 4 and Cell 7)
# ==========================================================
@app.cell
def _():
    x = 8
