import gooeypie as gp

def display_text(event):
    entered_text = secret.text
    result_label.text = f'{entered_text}'

def toggle_mask(event):
    secret.toggle()

app = gp.GooeyPieApp('Passowrd')

question = gp.Label(app, "What's your Password?")

submit_button = gp.Button(app, 'Submit', display_text)

result_label = gp.Label(app, '')

secret = gp.Secret(app)
secret.width = 50

check = gp.Checkbox(app, 'Show passowrd')
check.add_event_listener('change', toggle_mask)

app.set_grid(5, 1)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(check, 3, 1)
app.add(submit_button, 4, 1)
app.add(result_label, 5, 1)

app.run()