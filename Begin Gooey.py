import gooeypie as gp

def say_hello(event):
    hello_lbl.text = "This is a password checker"

def display_text(event):
    entered_text = text_input.text
    result_label.text = f'You entered: {entered_text}'

app = gp.GooeyPieApp("Hello!")
app.width = 250

hello_btn = gp.Button(app, "Begin Checker", display_text)
hello_lbl = gp.Label(app, "")

# app.set_grid(2, 1)
# app.add(hello_btn, 1, 1, align="center")
# app.add(hello_lbl, 2, 1, align="center")

app = gp.GooeyPieApp('Text Entry Example')

text_input = gp.Input(app)

submit_button = gp.Button(app, 'Submit', display_text)

result_label = gp.Label(app, '')

app.set_grid(3, 1)
app.add(text_input, 1, 1, align='center')
app.add(submit_button, 2, 1, align='center')
app.add(result_label, 3, 1, align='center')

app.run()