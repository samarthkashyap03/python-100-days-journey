'''This is a program that converts miles into Kms using python tkinter.'''
from tkinter import *
#Constants
WINDOW_WIDTH=200
WINDOW_HEIGHT=200
#--------Setup--------
window=Tk()
window.minsize(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
window.title("MILES TO KM CONVERTER")

#Functions
def convert():
    try:
        text=miles.get()
        kilometer.config(text=f"Is equal to {round(float(miles.get())*1.60934,2)} Km")
    except ValueError:
        miles.delete(first=0,last=END)
        miles.insert(index=0,string="Enter Integer Value")
#Label
welcome_text=Label(text="Miles --> KMs Converter",font=('Courier',15,'normal'))
welcome_text.grid(row=0,column=1,padx=60)

#Miles entry
miles=Entry(width=20)
miles.insert(index=0,string='Enter Miles here')
miles.grid(row=4,column=1,pady=20)
miles.focus()

#Miles label
miles_label=Label(text='Miles',width=0)
miles_label.grid(row=4,column=2)

#Kilometers Label
kilometer=Label(text=f"Is equal to 0 Km")
kilometer.grid(row=5,column=1)

#Calculate button
calculate=Button(text="Calculate",command=convert)
calculate.grid(row=6,column=1)

window.mainloop()