import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100)

    return (slider,)


@app.cell
def _(mo, slider):
    # Create dynamic Markdown
    mo.md(f"{slider} {"🟢" * slider.value}")

    return


@app.cell
def _(mo, x, y):
    mo.md(f"""Lets find the product of {x} and {y} along with 5 """)
    return


@app.cell
def _():
    x=8
    return (x,)


@app.cell
def _():
    y=10
    return (y,)


@app.cell
def _(x, y):
    print(x*y*5)
    return


@app.cell
def _():
    #Email is 24f2001293@ds.study.iitm.ac.in
    return


@app.cell
def _(mo):
    mo.md("Email is 24f2001293@ds.study.iitm.ac.in")
    return


if __name__ == "__main__":
    app.run()
