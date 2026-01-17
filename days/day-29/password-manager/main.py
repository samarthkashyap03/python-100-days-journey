#Password Generator GUI Application
from tkinter import *
from tkinter import messagebox
import random,string
import json
#---------Constants-------------
LOGO_PATH="logo.png"

#------------Setup---------------
#Create Main Window
window=Tk()
window.title('PASSWORD GENERATOR')
window.config(padx=100,pady=50)

#Create Canvas
canvas=Canvas(width=200,height=200)
logo=PhotoImage(file=LOGO_PATH)
canvas.create_image(100,100,image=logo)
canvas.grid(row=1,column=1,pady=10)

#---------Functions-------------
def generate_password():
    random_password=random.sample(list(string.ascii_letters),k=random.randint(4,7))+random.sample(list(string.digits),k=random.randint(3,5))+random.sample(list(string.punctuation),k=random.randint(4,6))
    random.shuffle(random_password)
    random_password="".join(random_password)
    password_entry.delete(first=0,last=END)
    password_entry.insert(index=END,string=random_password)
    
def add_data():
    #Collect data
    website=website_entry.get()
    email=email_entry.get()
    password=hash(password_entry.get())
    #Input validation, if any field is left blank, raise a warning dialog box
    if website=="":
        messagebox.showerror(title='Invalid Website Arguement',message='Website Field cannot be blank')
        return
    if email=='':
        messagebox.showerror(title='Invalid Email Arguement',message='Email Field cannot be Blank!')
        return
    if password=='':
        messagebox.showerror(title='Invalid Password',message='Password Field cannot be Blank!')
        return 
    #Confirm if details are correct
    message=messagebox.askyesno(title='Please confirm the Details',message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
    user_data={website:
               {
                   'Email':email,
                   'Password':password
               }}
    if message==True:
        #Write the data into a file called password-manager.txt
        try:
            with open('password-manager.json','r') as f:
                old_data=json.load(f)
                old_data.update(user_data)
        except FileNotFoundError:
            with open('password-manager.json','w') as f:
                json.dump(user_data,f,indent=4)
        else:
            with open('password-manager.json','w') as f:
                json.dump(old_data,f,indent=4)
        #Reset the entry Fields with blank
        website_entry.delete(first=0,last=END)
        email_entry.delete(first=0,last=END)
        password_entry.delete(first=0,last=END)
def search_data():
    website_name=website_entry.get()
    if website_name=='':
        messagebox.showerror(title='Error',message='Website name cannot be empty')
        return
    try:
        with open('password-manager.json','r') as f:
            data=json.load(f)
    except FileNotFoundError:
            messagebox.showerror(title='Missing File',message='File does not exist, please store atleast 1 data')
            return
    try:
        email=data.get(website_name)['Email']
        password=data.get(website_name)['Password']
        messagebox.showinfo(title='Data',message=f"Email: {email}\nPassword: {password}")
    except TypeError:
        messagebox.showerror(title='Error',message='No such Entry Found')
        return
            

#--------------------Main Loop-----------------------
#Website Label
website_label=Label(text='Website: ',font=("Helvetica", 11, "bold"))
website_label.grid(row=2,column=0)

#Website Entry
website_entry=Entry(width=20)
website_entry.grid(row=2,column=1,columnspan=1, sticky="ew",pady=5)

#Search button
search=Button(text='Search',font=("Arial", 10, "bold"),width=20,command=search_data)
search.grid(row=2,column=2, padx=10)

#Email Label
email_label=Label(text='Email/Username: ',font=("Helvetica", 11, "bold"))
email_label.grid(row=3,column=0)

#Email Entry
email_entry=Entry(width=20)
email_entry.insert(index=END,string='example@gmail.com')
email_entry.grid(row=3,column=1,columnspan=2, sticky="ew",pady=5)

#Password Label
password_label=Label(text='Password: ',font=("Helvetica", 11, "bold"))
password_label.grid(row=4,column=0)

#Password Entry
password_entry=Entry(width=30)
password_entry.grid(row=4,column=1,sticky='w',pady=5)

#Generate Password Button
generate_button=Button(text='Generate Password',font=("Arial", 10, "bold"),command=generate_password)
generate_button.grid(row=4,column=2,sticky='w',pady=10)

#Add button
add_button=Button(text='Add',font=("Arial", 10, "bold"),command=add_data)
add_button.grid(row=5,column=1,sticky='ew',columnspan=2)

window.mainloop()