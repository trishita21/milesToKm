from tkinter import *

CONSTANT = 1.609

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(pady=20, padx=20)

input = Entry(width=10)
input.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

label4 = Label(text=0)
label4.grid(row=1, column=1)


def calculate():
    mile = float(input.get())
    km = mile * CONSTANT
    label4.config(text=str(km))


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
