from tkinter import *
from db import connect_db

def go_back():
    root.destroy()
    import login

def register_provider():
    name = name_entry.get()
    phone = phone_entry.get()
    service = service_var.get()
    password = pass_entry.get()

    con = connect_db()
    cursor = con.cursor()

    # Check duplicate phone
    cursor.execute("SELECT * FROM users WHERE phone=%s", (phone,))
    if cursor.fetchone():
        status_label.config(text="Already Registered")
        return

    query = """
    INSERT INTO users (name, phone, password, role, service_type, status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, phone, password, "provider", service, "pending"))
    con.commit()

    status_label.config(text="Request Sent to Admin")

# UI
from tkinter import *
from db import connect_db

def register_provider():
    name = name_entry.get()
    phone = phone_entry.get()
    service = service_var.get()
    password = pass_entry.get()

    con = connect_db()
    cursor = con.cursor()

    cursor.execute("SELECT * FROM users WHERE phone=%s", (phone,))
    if cursor.fetchone():
        status_label.config(text="Already Registered", fg="red")
        return

    query = """
    INSERT INTO users (name, phone, password, role, service_type, status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, phone, password, "provider", service, "pending"))
    con.commit()

    status_label.config(text="Request Sent to Admin", fg="green")


def toggle_password():
    if pass_entry.cget('show') == '':
        pass_entry.config(show='*')
        show_btn.config(text='Show')
    else:
        pass_entry.config(show='')
        show_btn.config(text='Hide')


def go_back():
    root.destroy()
    import login


# 🎨 WINDOW
root = Tk()
root.title("Service Provider Registration")
root.geometry("600x600")
root.configure(bg="#dfe6e9")

# 🔲 CARD
card = Frame(root, bg="white", padx=40, pady=40)
card.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(card, text="Provide Service", font=("Arial", 22, "bold"), bg="white").pack(pady=20)

# 👤 NAME
Label(card, text="Name", bg="white").pack(anchor="w")
name_entry = Entry(card, width=35, font=("Arial", 12))
name_entry.pack(pady=10, ipady=5)

# 📱 PHONE
Label(card, text="Phone", bg="white").pack(anchor="w")
phone_entry = Entry(card, width=35, font=("Arial", 12))
phone_entry.pack(pady=10, ipady=5)

# ⚙️ SERVICE TYPE
Label(card, text="Service Type", bg="white").pack(anchor="w")

service_var = StringVar()
service_var.set("Petrol Delivery")

dropdown = OptionMenu(card, service_var,
                      "Petrol Delivery",
                      "Mechanical Service",
                      "Towing Service")

dropdown.config(
    width=25,
    font=("Arial", 12),
    bg="#ecf0f1",
    fg="black",
    activebackground="#bdc3c7",
    highlightthickness=0
)

dropdown["menu"].config(
    font=("Arial", 11),
    bg="white"
)

dropdown.pack(pady=10, ipady=5)

# 🔒 PASSWORD
Label(card, text="Password", bg="white").pack(anchor="w")

pass_frame = Frame(card, bg="white")
pass_frame.pack(pady=10)

pass_entry = Entry(pass_frame, show="*", width=27, font=("Arial", 12))
pass_entry.pack(side=LEFT, ipady=5)

show_btn = Button(pass_frame, text="Show", command=toggle_password)
show_btn.pack(side=LEFT, padx=5)

# 🔘 REGISTER BUTTON
Button(card, text="Submit Request",
       width=25,
       height=2,
       bg="#e67e22",
       fg="white",
       font=("Arial", 12, "bold"),
       command=register_provider).pack(pady=20)

# 🔙 BACK BUTTON
Button(card, text="⬅ Back to Login",
       bg="white", fg="blue",
       bd=0, cursor="hand2",
       command=go_back).pack()

# 📢 STATUS
status_label = Label(card, text="", bg="white")
status_label.pack()

root.mainloop()