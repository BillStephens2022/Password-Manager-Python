from tkinter import *


# TODO:
# Setup UI
# Setup Password Generator
# Save Password

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0) #highlightthickness removes the border around the image
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)



window.mainloop()