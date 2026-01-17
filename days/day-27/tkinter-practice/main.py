from tkinter import *
#Constants
FONT=('Courier',20,'bold')
#-------Setup---------
window=Tk()
window.minsize(width=500,height=400)
window.title('My first GUI')

#------functions-------
def on_click():
    user_input=entry.get()
    label.config(text=user_input)
    label.update()

#label
label=Label(text='Click the button',font=FONT)
label.grid(row=0,column=0)

#Button 1
button1=Button(text='Click me!',font=('Times New Roman',10,'normal'),command=on_click)
button1.grid(row=1,column=1)

#Button 2
button2=Button(text="Dont click")
button2.grid(row=0,column=2)

#Input field
entry=Entry()
entry.focus()
entry.insert(index=0,string='Enter text here')
entry.grid(row=2,column=3)

window.mainloop()