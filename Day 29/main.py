from Tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="/Users/PravinSelvarajah/Documents/GitHub/100-Days-of-Code/Day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

window.mainloop()