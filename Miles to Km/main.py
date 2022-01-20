from tkinter import *

def calculate():
    miles =float(miles_input.get())
    km = round(miles *1.609,1)
    result.config(text=f"{km}")
window = Tk()
window.title("MILES TO KM")
window.config(padx=20,pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)


miles_label =Label(text ="Miles")
miles_label.grid(column=2,row=0)

is_equal =Label(text ="is equal to")
is_equal.grid(column=0,row=1)

result = Label(text =0)
result.grid(column=1 ,row =1)

km= Label(text ="Km")
km.grid(column=2,row=1)

calc= Button(text ="Calculate", command=calculate)
calc.grid(column=1,row=2)















window.mainloop()