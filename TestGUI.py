from guizero import App, Text, TextBox, PushButton, Window

def say_my_name():
    welcomeMessage.value = my_name.value

app = App("FastPassOS", bg = "lightgrey", layout = "auto")
welcomeMessage = Text(app, text = "Pass Sign Out ", size = 180, font = "Times New Roman", color="darkblue", visible = True)
subTitle = Text(app, text="Scan A Pass to Start", size = 100, font = "Times New Roman", color = "darkblue", visible = True)
signOutTitle = Text(app, text = "You are signing out:", size = 135, font = "Times New Roman", color = "darkblue", visible = False)
signOutNameText = Text(app, text= "Type your name (first and last):", size = 100, font = "Times New Roman", color = "darkblue", align = "left", visible = False)
#nameTextBox = TextBox(app, width = "fill", text = "First Name", visible = True, align = "center")
subSubTitle = Text(app, text="Browntown Fast Pass System Version 0.1 Copyright Browntown Industries 2022", size = 20, font = "Times New Roman", color = "darkblue", align = "bottom", visible = True)

submitButton = PushButton(app, text = "Enter", visible = False)

#window = Window(app, bg="red")
#app.display()
app.set_full_screen('x')
app.display()
