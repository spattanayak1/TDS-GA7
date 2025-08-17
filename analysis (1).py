import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    # Cell 1: Import Marimo library for widgets and reactive UI
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    # Cell 2: Create slider widget
    # OUTPUT: slider (used in Cell 3 for dynamic markdown)
    slider = mo.ui.slider(1, 100)
    return (slider,)


@app.cell
def _(mo, slider):
    # Cell 3: Dynamic markdown based on slider value
    # INPUT: slider from Cell 2
    # OUTPUT: Displays slider value with green dots
    mo.md(f"{slider} {"🟢" * slider.value}")

    return


@app.cell
def _(mo, x, y):
    # Cell 4: Dynamic markdown showing variables x and y
    # INPUT: x from Cell 5, y from Cell 6
    mo.md(f"""Lets find the product of {x} and {y} along with 5 """)
    return


@app.cell
def _():
    # Cell 5: Define variable x
    # OUTPUT: x (used in Cells 4 and 7)
    x=8
    return (x,)


@app.cell
def _():
    # Cell 6: Define variable y
    # OUTPUT: y (used in Cells 4 and 7)
    y=10
    return (y,)


@app.cell
def _(x, y):
    # Cell 7: Compute and print product of x and y multiplied by 5
    # INPUT: x from Cell 5, y from Cell 6
    print(x*y*5)
    return


@app.cell
def _():
    # Cell 8: Comment with email (as required)
    #Email is 24f3000061@ds.study.iitm.ac.in
    return


@app.cell
def _(mo):
    # Cell 9: Markdown output showing email
    mo.md("Email is 24f3000061@ds.study.iitm.ac.in")
    return


if __name__ == "__main__":
    app.run()
