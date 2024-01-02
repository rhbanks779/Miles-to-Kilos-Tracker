from tkinter import *
import tkinter

window = Tk()
window.title("Mile to Kilo Project")

#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


text1 = Label(text="Miles")
text1.grid(column=2, row=0)

text2 = Label(text="is equal to")
text2.grid(column=0, row=1)

kilo_label = Label(text="0")
kilo_label.grid(column=1, row=1)

text3 = Label(text='Km')
text3.grid(column=2, row=1)

def calculate_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilo_label.config(text=km)

button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)











window.mainloop()