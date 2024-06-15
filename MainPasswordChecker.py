import gooeypie as gp
import time

def CheckPassowrd(event):
    loading_bar.value = 0
    result_label.text = ''
    for steps in range(50):
        loading_bar.value += 2
        app.refresh()
        time.sleep(0.02)
    entered_text = secret.text
    result_label.text = f'{entered_text}'
    
def ToggleMask(event):
    secret.toggle()

app = gp.GooeyPieApp('Passowrd')

question = gp.Label(app, "What's your Password?")

submit_button = gp.Button(app, 'Submit', CheckPassowrd)

result_label = gp.Label(app, '')

loading_bar = gp.Progressbar(app)

secret = gp.Secret(app)
secret.width = 50

check = gp.Checkbox(app, 'Show passowrd')
check.add_event_listener('change', ToggleMask)

app.set_grid(6, 2)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(check, 3, 1)
app.add(submit_button, 4, 1)
app.add(loading_bar, 5, 1, column_span=2, fill=True)
app.add(result_label, 6, 1)

app.run()
