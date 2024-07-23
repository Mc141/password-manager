from tkinter import *
from PIL import Image
from tkinter import messagebox
from password_generator.password import Password
import pyperclip





def write_data():
    file = open("data.txt", "a")
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            structured_data = f"{website} | {email} | {password}"
            file.write(f"{structured_data}\n")
            file.close()
            
            email_entry.delete(0, END)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
            
    


def generate_password():
    password_entry.delete(0, END)
    password = Password().generate_password(12)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)
    




root = Tk()
root.title("Password Manager")
root.resizable(False, False)
root.config(padx=50, pady=50)





canvas = Canvas(root, width=200, height=200)
canvas.grid(row=0, column=1)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)






website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=53, highlightcolor="blue", highlightthickness=1)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()





email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=53, highlightcolor="blue", highlightthickness=1)
email_entry.grid(row=2, column=1, columnspan=2)





password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=35, highlightcolor="blue", highlightthickness=1)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", highlightthickness = 0, bd = 0, bg="gray80", command=generate_password)
generate_button.grid(row=3, column=2)





add_button = Button(text="Add", width=45, highlightthickness = 0, bd = 0, bg="gray80", command=write_data)
add_button.grid(row=4, column=1, columnspan=2)




























root.mainloop()