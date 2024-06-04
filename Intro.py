import gooeypie as gp

def say_hello(event):
    hello_lbl.text = "This is a password checker"

app = gp.GooeyPieApp("Hello!")
app.width = 250

hello_btn = gp.Button(app, "Begin Checker", say_hello)
hello_lbl = gp.Label(app, "")

app.set_grid(2, 1)
app.add(hello_btn, 1, 1, align="center")
app.add(hello_lbl, 2, 1, align="center")

app.run()