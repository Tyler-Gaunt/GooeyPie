import gooeypie as gp

def say_hello(event):
    hello_lbl.text = "This is a password checker"
    app.add(hidden_lbl, 3, 1)

app = gp.GooeyPieApp("Hello!")
app.width = 250

hello_lbl = gp.Button(app, "Begin Checker", say_hello)
hello_inp = gp.Label(app, "")

hidden_lbl = gp.Label(app, 'Now you see me')

app.set_grid(3, 1)
app.add(hello_lbl, 1, 1, align="center")
app.add(hello_inp, 2, 1, align="center")

app.run()