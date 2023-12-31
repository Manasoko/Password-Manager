from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generates a random password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    let = [random.choice(letters) for letter in range(random.randint(8, 10))]
    num = [random.choice(numbers) for number in range(random.randint(2, 4))]
    sym = [random.choice(symbols) for symbol in range(random.randint(2, 4))]

    password_list = let + num + sym
    random.shuffle(password_list)

    psw = "".join(password_list)
    psw_input.insert(0, psw)
    pyperclip.copy(psw)

# ----------------------------SEARCH PASSWORD ------------------------------ #
def search_psw():
    web = web_input.get()
    try:
        with open("C:/Users/lenovo/Desktop/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="Data file is not existing")
    else:
        if web in data:
            website_info = data[web]
            email_info = website_info["email"]
            psw_info = website_info["password"]
            messagebox.showinfo(title=web, message=f"Email: {email_info} \nPassword: {psw_info}")
        elif len(web) == 0:
            messagebox.showwarning(title="Left out", message="Please fill the website field")
        else:
            messagebox.showinfo(title="Oops", message="You have not saved this website")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves the password inputted"""
    website = web_input.get()
    password = psw_input.get()
    email = email_input.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("C:/Users/lenovo/Desktop/data.json", "r") as saved_psw:
                # Read old data
                data = json.load(saved_psw)
        except FileNotFoundError:
            with open("C:/Users/lenovo/Desktop/data.json", "w") as saved_psw:
                json.dump(new_data, saved_psw, indent=4)
        else:
            # Updating old data
            data.update(new_data)
            with open("data.json", "w") as saved_psw:
                # Saving the data
                json.dump(data, saved_psw, indent=4)
        finally:
            web_input.delete(0, END)
            psw_input.delete(0, END)

# ---------------------------- AUTOFILL ------------------------------- #
 def autofill():
        website = web_input.get()
         try:
            with open("C:/Users/lenovo/Desktop/data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Oops", message="Data file is not existing")
         else:
            if website in data:
                password_entry.delete(0, END)
                password_entry.insert(0, data[website]["password"])
            else:
                print(f"No credentials found for {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
psw_label = Label(text="Password:")
psw_label.grid(row=3, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

web_input = Entry(width=25)
web_input.grid(row=1, column=1)
web_input.focus()
email_input = Entry(width=43)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "manajiyah@gmail.com")
psw_input = Entry(width=25)
psw_input.grid(row=3, column=1)

search_btn = Button(text="Search", width=14, command=search_psw)
search_btn.grid(row=1, column=2)
generate_psw = Button(text="Generate Password", width=14, command=generate_password)
generate_psw.grid(row=3, column=2)
add_btn = Button(text="Add", width=37, command=save)
add_btn.grid(row=4, column=1, columnspan=1)
autofill_btn = Button(text="Autofill", command=autofill)
autofill_button.grid(row=4, column=2)

window.mainloop()
