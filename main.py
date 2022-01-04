from tkinter import *
from tkinter import messagebox
import os
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# pwd_character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0123456789'
# pwd = ''
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_word():
    cwd = os.getcwd()
    site_details = ""
    with open(os.path.join(cwd, "Users.json"), mode="r") as f:
        site_result = json.loads(f.read())
        site_json = site_result[site_entry.get()]
        for key in site_json:
            site_details += key + ": " + site_json[key] + "\n"
    messagebox.showinfo(title="Website Details", message=f"{site_details}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pwd():
    # global pwd
    # pwd = ''
    # pwd_entry.delete(0, END)
    # while len(pwd) < 15:
    #     pwd = pwd + random.choice(pwd_character)
    # pwd_entry.insert(END, pwd)

    #   Another method of generating secure password.
    pwd_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters = [choice(letters) for _ in range(randint(8, 10))]
    pwd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pwd_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pwd_letters + pwd_symbols + pwd_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pwd_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD AS JSON ------------------------------- #
def save_user_details():
    cwd = os.getcwd()
    user = {
        site_entry.get(): {
            "email": email_entry.get(),
            "password": pwd_entry.get(),
        }
    }

    if len(site_entry.get()) <= 0 and len(pwd_entry.get()) <= 0:
        messagebox.showinfo(title="Warning", message="Your can't save empty record to file. Fill the require details.")
        site_entry.focus()
    else:
        answer = messagebox.askokcancel(title=site_entry.get().title(),
                                        message=f"You have entered these details:\nEmail: {email_entry.get()}\n"
                                                f"Password: {pwd_entry.get()}\nAre they correct to be saved?")
    if answer:
        with open(os.path.join(cwd, "Users.json"), mode='w') as f:
            json.dump(user, f)
            site_entry.delete(0, END)
            pwd_entry.delete(0, END)
        messagebox.showinfo(title="Confirmation", message="Your details are saved to file.")
    else:
        messagebox.showinfo(title="Cancel", message="Your details are not saved to file.")
        site_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

key_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=250, bg=YELLOW)
canvas.create_image(100, 112, image=key_image)
canvas.create_text(100, 12, text="Password Manager", fill="red", font=(FONT_NAME, 15, "bold"))
canvas.grid(column=1, row=0)

site_label = Label(text="WebSite:", font=(FONT_NAME, 10, "bold"))
site_label.grid(row=2, column=0)

site_entry = Entry(width=33)
site_entry.grid(row=2, column=1)
site_entry.focus()

add_search = Button(text="Search", width=15, command=search_word)
add_search.grid(row=2, column=2)

email_label = Label(text="Email/Username: ", font=(FONT_NAME, 10, "bold"))
email_label.grid(row=3, column=0)

email_entry = Entry(width=52)
email_entry.grid(row=3, column=1, columnspan=2)
email_entry.insert(END, "python@gmail.com")

pwd_label = Label(text="Password", font=(FONT_NAME, 10, "bold"))
pwd_label.grid(row=4, column=0)

pwd_entry = Entry(width=33)
pwd_entry.grid(row=4, column=1)

pwd_button = Button(text="Generate Password", command=gen_pwd)
pwd_button.grid(row=4, column=2)

add_button = Button(text="Add", width=44, command=save_user_details)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
