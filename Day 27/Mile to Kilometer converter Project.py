from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)
# Entry input miles
entry_mile = Entry(width=7)
entry_mile.grid(column=1,row=0)

#Label mile
label_mile = Label(text="Miles")
label_mile.grid(column=2,row=0)

#Label equal
label = Label(text="is equal to")
label.grid(column=0,row=1)

#Entry output km
entry_km = Label(text="0")
entry_km.grid(column=1,row=1)

#Label Km
label_km = Label(text="Km")
label_km.grid(column=2,row=1)
def convert():
    m = float(entry_mile.get())
    km = m * 1.609
    entry_km.config(text = f"{km}")
#Button
button = Button(text="Calculate",command=convert)
button.grid(column=1,row=2)
window.mainloop()
