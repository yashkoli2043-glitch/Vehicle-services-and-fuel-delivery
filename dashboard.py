from tkinter import *
from db import connect_db

def view_requests():
    con = connect_db()
    cursor = con.cursor()

    cursor.execute("SELECT * FROM requests")
    data = cursor.fetchall()

    win = Toplevel()
    win.title("All Requests")
    win.geometry("400x300")

    for row in data:
        Label(win, text=f"ID:{row[0]} | User:{row[1]} | Qty:{row[3]} | Status:{row[4]}").pack()


def update_status():
    def update():
        req_id = id_entry.get()
        new_status = status_var.get()

        con = connect_db()
        cursor = con.cursor()

        cursor.execute("UPDATE requests SET status=%s WHERE id=%s", (new_status, req_id))
        con.commit()

        result_label.config(text="Status Updated")

    win = Toplevel()
    win.title("Update Status")
    win.geometry("300x200")

    Label(win, text="Request ID").pack()
    id_entry = Entry(win)
    id_entry.pack()

    Label(win, text="Select Status").pack()
    status_var = StringVar()
    status_var.set("Accepted")

    OptionMenu(win, status_var, "Accepted", "Delivered").pack()

    Button(win, text="Update", command=update).pack(pady=10)

    result_label = Label(win, text="")
    result_label.pack()

def request_petrol(user):
    def submit_request():
        qty = qty_entry.get()

        con = connect_db()
        cursor = con.cursor()

        query = "INSERT INTO requests (user_id, quantity, status) VALUES (%s, %s, %s)"
        cursor.execute(query, (user[0], qty, "Pending"))
        con.commit()

        status_label.config(text="Request Sent Successfully")

    win = Toplevel()
    win.title("Request Petrol")
    win.geometry("300x200")

    Label(win, text="Enter Quantity (Liters)").pack()
    qty_entry = Entry(win)
    qty_entry.pack()

    Button(win, text="Submit", command=submit_request).pack(pady=10)

    status_label = Label(win, text="")
    status_label.pack()

def show_emergency():
    con = connect_db()
    cursor = con.cursor()

    cursor.execute("SELECT area, contact_number FROM emergency_contacts")
    data = cursor.fetchall()

    win = Toplevel()
    win.title("Emergency Contacts")
    win.geometry("300x200")

    for row in data:
        Label(win, text=f"{row[0]} : {row[1]}").pack()

def show_services():
    con = connect_db()
    cursor = con.cursor()

    # Only approved providers
    cursor.execute("""
        SELECT name, service_type, phone 
        FROM users 
        WHERE role='provider' AND status='approved'
    """)
    
    data = cursor.fetchall()

    win = Toplevel()
    win.title("Available Services")
    win.geometry("350x300")

    if not data:
        Label(win, text="No services available").pack()
        return

    for row in data:
        Label(win, text=f"{row[1]} | {row[0]} | {row[2]}").pack()

def open_dashboard(user):
    role = user[4]   # role column (id, name, phone, password, role)

    dash = Toplevel()
    dash.title("Dashboard")
    dash.geometry("400x300")

    Label(dash, text=f"Welcome {user[1]}", font=("Arial", 14)).pack(pady=10)

    if role == "customer":
        Label(dash, text="Customer Dashboard", fg="blue").pack()

        Button(dash, text="Request Petrol", width=20, command=lambda: request_petrol(user)).pack(pady=5)
        Button(dash, text="Find Nearby Pumps", width=20).pack(pady=5)
        Button(dash, text="🚨 Emergency Help", width=20, command=show_emergency).pack(pady=5)
        Button(dash, text="Find Services", width=20, command=show_services).pack(pady=5)

    elif role == "provider":
         Label(dash, text="Provider Dashboard", fg="green").pack()
         Button(dash, text="View Requests", width=20, command=view_requests).pack(pady=5)
         Button(dash, text="Update Status", width=20, command=update_status).pack(pady=5)
   