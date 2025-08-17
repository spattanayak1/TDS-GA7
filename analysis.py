import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")

# ==========================================================
# Cell 1: Import Marimo library
# OUTPUT: mo (used in all later cells for UI and markdown)
# ==========================================================
@app.cell
def _():
    import marimo as mo
    return (mo,)


# ==========================================================
# Cell 2: Create interactive slider widget
# OUTPUT: slider (used in Cell 3 for markdown)
# ==========================================================
@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100)  # Slider ranges from 1 to 100
    return (slider,)


# ==========================================================
# Cell 3: Dynamic markdown reacting to slider state
# INPUT: slider (from Cell 2)
# OUTPUT: Displays slider value with green dots
# ==========================================================
@app.cell
def _(mo, slider):
    mo.md(f"Slider value = {slider.value} {'🟢' * slider.value}")
    return


# ==========================================================
# Cell 4: Define variable x
# OUTPUT: x (used in Cell 6 and Cell 7)
# ==========================================================
@app.cell
def _():
    x = 8
    return (x,)


# ==========================================================
# Cell 5: Define variable y
# OUTPUT: y (used in Cell 6 and Cell 7)
# ==========================================================
@app.cell
def _():
    y = 10
    return (y,)


# ==========================================================
# Cell 6: Markdown explanation of relationship between x and y
# INPUT: x (from Cell 4), y (from Cell 5)
# OUTPUT: Textual description of variables
# ==========================================================
@app.cell
def _(mo, x, y):
    mo.md(f"Exploring the relationship: x = {x}, y = {y}.")
    return


# ==========================================================
# Cell 7: Compute a derived value from x and y
# INPUT: x (from Cell 4), y (from Cell 5)
# OUTPUT: printed product of x, y, and 5
# ==========================================================
@app.cell
def _(x, y):
    print("Computed result (x * y * 5):", x * y * 5)
    return


# ==========================================================
# Cell 8: Comment with email (research requirement)
# ==========================================================
@app.cell
def _():
    # Email: 24f3000061@ds.study.iitm.ac.in
    return


# ==========================================================
# Cell 9: Markdown output showing email
# ==========================================================
@app.cell
def _(mo):
    mo.md("Contact: **24f3000061@ds.study.iitm.ac.in**")
    return


# ==========================================================
# Entry point
# ==========================================================
if __name__ == "__main__":
    app.run()
