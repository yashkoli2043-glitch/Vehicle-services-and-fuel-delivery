from tkinter import *
from db import connect_db

# 🔹 Add Petrol Pump
def add_pump():
    def save():
        name = name_entry.get()
        location = loc_entry.get()
        contact = contact_entry.get()

        con = connect_db()
        cursor = con.cursor()

        cursor.execute(
            "INSERT INTO petrol_pumps (name, location, contact) VALUES (%s, %s, %s)",
            (name, location, contact)
        )
        con.commit()

        status.config(text="Pump Added")

    win = Toplevel()
    win.title("Add Petrol Pump")
    win.geometry("300x250")

    Label(win, text="Pump Name").pack()
    name_entry = Entry(win)
    name_entry.pack()

    Label(win, text="Location").pack()
    loc_entry = Entry(win)
    loc_entry.pack()

    Label(win, text="Contact").pack()
    contact_entry = Entry(win)
    contact_entry.pack()

    Button(win, text="Save", command=save).pack(pady=10)
    status = Label(win, text="")
    status.pack()


# 🔹 View Users
def view_users():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT id, name, phone, role FROM users WHERE role != 'admin'")

    data = cursor.fetchall()

    win = Toplevel()
    win.title("All Users")

    for row in data:
        Label(win, text=f"{row[0]} | {row[1]} | {row[2]} | {row[3]}").pack()


# 🔹 View Requests
def view_requests():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM requests")

    data = cursor.fetchall()

    win = Toplevel()
    win.title("All Requests")

    for row in data:
        Label(win, text=f"ID:{row[0]} User:{row[1]} Qty:{row[3]} Status:{row[4]}").pack()


# 🔹 Main Admin Panel
def open_admin_panel(user):
    name = user[1]

    admin = Toplevel()
    admin.title("Admin Panel")
    admin.geometry("700x550")
    admin.configure(bg="#ecf0f1")

    # 🔷 HEADER
    header = Frame(admin, bg="#2c3e50", height=60)
    header.pack(fill="x")

    Label(header, text="Admin Dashboard",
          bg="#2c3e50", fg="white",
          font=("Arial", 16, "bold")).pack(side="left", padx=20)

    Button(header, text="Logout",
           bg="#e74c3c", fg="white",
           command=admin.destroy).pack(side="right", padx=20, pady=10)

    # 👤 INFO
    info = Frame(admin, bg="#ecf0f1")
    info.pack(pady=20)

    Label(info, text=f"Welcome, {name}",
          font=("Arial", 18, "bold"),
          bg="#ecf0f1").pack()

    Label(info, text="Role: Admin",
          font=("Arial", 12),
          bg="#ecf0f1", fg="gray").pack()

    # 🔲 MAIN CARD
    card = Frame(admin, bg="white", padx=30, pady=30)
    card.pack(pady=10)

    Label(card, text="Admin Controls",
          font=("Arial", 14),
          bg="white", fg="gray").pack(pady=10)

    # 🔘 BUTTONS
    Button(card, text="➕ Add Petrol Pump",
           width=30, height=2,
           bg="#27ae60", fg="white",
           font=("Arial", 11, "bold"),
           command=add_pump).pack(pady=8)

    Button(card, text="👥 View Users",
           width=30, height=2,
           bg="#2980b9", fg="white",
           font=("Arial", 11, "bold"),
           command=view_users).pack(pady=8)

    Button(card, text="📦 View Requests",
           width=30, height=2,
           bg="#8e44ad", fg="white",
           font=("Arial", 11, "bold"),
           command=view_requests).pack(pady=8)

    Button(card, text="✔ Approve Providers",
           width=30, height=2,
           bg="#16a085", fg="white",
           font=("Arial", 11, "bold"),
           command=approve_providers).pack(pady=8)