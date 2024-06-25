import gooeypie as gp
import time
import re

def CheckPassowrd(event):
    loading_bar.value = 0
    result_label.text = ""
    for steps in range(50):
        loading_bar.value += 2
        app.refresh()
        time.sleep(0.02)
    
    entered_text = secret.text
    if check_password_strength(entered_text) == "Strong":
        result_label.text = "Password Lvl: Strong"
    elif check_password_strength(entered_text) == "Moderate":
        result_label.text = "Password Lvl: Moderate, Please make sure your password contains at least; \n13 characters, one upper and lower case letter, one number and \none special character!"
    else:
        result_label.text = "Password Lvl: Weak, Please make sure your password contains at least; \n13 characters, one upper and lower case letter, one number and \none special character!"

def ToggleMask(event):
    secret.toggle()

def check_password_strength(password):
    if len(password) > 13 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'\d', password) and re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Strong"
    elif len(password) > 13 and (re.search(r'[A-Z]', password) or re.search(r'[a-z]', password)) and (re.search(r'\d', password) or re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return "Moderate"
    elif len(password) < 13:
        return "Weak"

app = gp.GooeyPieApp("PassWizard")

question = gp.Label(app, "What's your Password?")

submit_button = gp.Button(app, "Submit", CheckPassowrd)

result_label = gp.Label(app, "")

loading_bar = gp.Progressbar(app)

secret = gp.Secret(app)
secret.width = 50

check = gp.Checkbox(app, "Show passowrd")
check.add_event_listener("change", ToggleMask)

app.set_grid(6, 2)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(check, 3, 1)
app.add(submit_button, 4, 1)
app.add(loading_bar, 5, 1, column_span=2, fill=True)
app.add(result_label, 6, 1)

app.run()

