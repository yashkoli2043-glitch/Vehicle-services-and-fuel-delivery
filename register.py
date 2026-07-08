from tkinter import *
from db import connect_db

import re

import re

def go_back():
    root.destroy()
    import login

def register():
    name = name_entry.get()
    phone = phone_entry.get()
    vehicle = vehicle_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    role = "customer"
    # Mobile validation
    if not re.fullmatch(r"[6-9]\d{9}", phone):
        status_label.config(text="Invalid Mobile Number")
        return

    con = connect_db()
    cursor = con.cursor()

    # Check duplicate username
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cursor.fetchone():
        status_label.config(text="Username already exists")
        return

    query = """
    INSERT INTO users (name, phone, vehicle_number, username, password, role)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, phone, vehicle, username, password, role))
    con.commit()

    status_label.config(text="Registration Successful")

# UI
root = Tk()
root.title("Customer Registration")
root.geometry("600x600")
root.configure(bg="#dfe6e9")

# 🔲 Card
card = Frame(root, bg="white", padx=40, pady=40)
card.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(card, text="Register", font=("Arial", 22, "bold"), bg="white").pack(pady=20)

# 👤 NAME
Label(card, text="Name", bg="white").pack(anchor="w")
name_entry = Entry(card, width=35, font=("Arial", 12))
name_entry.pack(pady=10, ipady=5)

# 📱 PHONE
Label(card, text="Phone", bg="white").pack(anchor="w")
phone_entry = Entry(card, width=35, font=("Arial", 12))
phone_entry.pack(pady=10, ipady=5)

# 🚗 VEHICLE
Label(card, text="Vehicle Number", bg="white").pack(anchor="w")
vehicle_entry = Entry(card, width=35, font=("Arial", 12))
vehicle_entry.pack(pady=10, ipady=5)

# 👤 USERNAME
Label(card, text="Username", bg="white").pack(anchor="w")
username_entry = Entry(card, width=35, font=("Arial", 12))
username_entry.pack(pady=10, ipady=5)

# 🔒 PASSWORD + SHOW
def toggle_password():
    if pass_entry.cget('show') == '':
        pass_entry.config(show='*')
        show_btn.config(text='Show')
    else:
        pass_entry.config(show='')
        show_btn.config(text='Hide')

Label(card, text="Password", bg="white").pack(anchor="w")

pass_frame = Frame(card, bg="white")
pass_frame.pack(pady=10)

pass_entry = Entry(pass_frame, show="*", width=27, font=("Arial", 12))
pass_entry.pack(side=LEFT, ipady=5)

show_btn = Button(pass_frame, text="Show", command=toggle_password)
show_btn.pack(side=LEFT, padx=5)

# 🔘 REGISTER BUTTON
Button(card, text="Register",
       width=25,
       height=2,
       bg="#3498db",
       fg="white",
       font=("Arial", 12, "bold"),
       command=register).pack(pady=20)

# 📢 STATUS
status_label = Label(card, text="", bg="white")
status_label.pack()

Button(root, text="⬅ Back to Login",
       bg="white", fg="blue", bd=0,
       cursor="hand2",
       command=go_back).pack(pady=10)

root.mainloop()