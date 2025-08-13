import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")

# Cell 1: Import Marimo library for widgets and reactive UI
@app.cell
def _():
    import marimo as mo
    return (mo,)

# Cell 2: Create slider widget
# OUTPUT: slider (used in Cell 3 for dynamic markdown)
@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100)  # Slider between 1 and 100
    return (slider,)

# Cell 3: Dynamic markdown based on slider value
# INPUT: slider from Cell 2
# OUTPUT: Displays slider value with green dots
@app.cell
def _(mo, slider):
    mo.md(f"{slider} {'🟢' * slider.value}")
    return

# Cell 4: Dynamic markdown showing variables x and y
# INPUT: x from Cell 5, y from Cell 6
@app.cell
def _(mo, x, y):
    mo.md(f"Let's find the product of {x} and {y} along with 5")
    return

# Cell 5: Define variable x
# OUTPUT: x (used in Cells 4 and 7)
@app.cell
def _():
    x = 8
    return (x,)

# Cell 6: Define variable y
# OUTPUT: y (used in Cells 4 and 7)
@app.cell
def _():
    y = 10
    return (y,)

# Cell 7: Compute and print product of x and y multiplied by 5
# INPUT: x from Cell 5, y from Cell 6
@app.cell
def _(x, y):
    print(x * y * 5)
    return

# Cell 8: Comment with email (as required)
@app.cell
def _():
    # Email is 24f2001293@ds.study.iitm.ac.in
    return

# Cell 9: Markdown output showing email
@app.cell
def _(mo):
    mo.md("Email is 24f2001293@ds.study.iitm.ac.in")
    return

if __name__ == "__main__":
    app.run()
