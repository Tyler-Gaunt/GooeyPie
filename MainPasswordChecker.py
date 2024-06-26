import gooeypie as gp
import time
import re

def CheckPassword(event):
    loading_bar.value = 0
    result_label.text = ""
    for steps in range(50):
        loading_bar.value += 2
        app.refresh()
        time.sleep(0.02)
    
    entered_text = secret.text
    if CheckPasswordStrength(entered_text) == "Strong":
        result_label.text = "Password Lvl: Strong"
    elif CheckPasswordStrength(entered_text) == "Moderate":
        result_label.text = "Password Lvl: Moderate, Please make sure your password contains at least; \n10 characters, one upper and lower case letter, one number and \none special character!"
    else:
        result_label.text = "Password Lvl: Weak, Please make sure your password contains at least; \n10 characters, one upper and lower case letter, one number and \none special character!"

def ToggleMask(event):
    secret.toggle()

def ContainsUpper(password):
    if re.search(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]', password):
        return True
    else:  
        return False
    
def ContainsLower(password):
    if re.search(r'[abcdefghijklmnopqrstuvwxyz]', password):
        return True
    else:
        return False

def ContainsNumber(password):
    if re.search(r'[1234567890]', password):
        return True
    else:
        return False
    
def ContainsSymbol(password):
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return True
    else:
        return False

def CheckPasswordStrength(password):
    if len(password) < 10:
        return "Weak"
    elif len(password) > 10 and ContainsUpper(password) and ContainsLower(password) and ContainsNumber(password) and ContainsSymbol(password):
        return "Strong"
    elif len(password) > 10 and ContainsUpper(password) or ContainsLower(password) or ContainsNumber(password) or ContainsSymbol(password):
        return "Moderate"


app = gp.GooeyPieApp("PassWizard")

question = gp.Label(app, "What's your Password?")

submit_button = gp.Button(app, "Submit", CheckPassword)

result_label = gp.Label(app, "")

loading_bar = gp.Progressbar(app)

secret = gp.Secret(app)
secret.width = 50

check = gp.Checkbox(app, "Show passowrd")
check.add_event_listener("change", ToggleMask)

app.set_grid(7, 2)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(check, 3, 1)
app.add(submit_button, 4, 1)
app.add(loading_bar, 5, 1, column_span=2, fill=True)
app.add(result_label, 6, 1)

app.run()

