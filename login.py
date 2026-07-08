from tkinter import *
from db import connect_db
from dashboard import open_dashboard
from admin_panel import open_admin_panel



def login():
    username = username_entry.get()
    password = pass_entry.get()

    con = connect_db()
    cursor = con.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:
        role = result[4]  # role column

        if role == "admin":
            open_admin_panel(result)
        else:
            open_dashboard(result)

        status_label.config(text="Login Successful")
    else:
        status_label.config(text="Invalid Username or Password")

# UI
def toggle_password():
    if pass_entry.cget('show') == '':
        pass_entry.config(show='*')
        show_btn.config(text='Show')
    else:
        pass_entry.config(show='')
        show_btn.config(text='Hide')

def open_register():
    root.destroy()
    import register

def open_service_provider_register():
    root.destroy()   # close login window
    import service_provider_register

def forgot_password():
    from tkinter import messagebox
    messagebox.showinfo("Forgot Password", "Contact Admin to reset password")
    
root = Tk()
root.title("Fuel Delivery System")
root.geometry("600x500")
root.configure(bg="#dfe6e9")

# 🔲 CARD FRAME (center box)
card = Frame(root, bg="white", padx=40, pady=40)
card.place(relx=0.5, rely=0.5, anchor=CENTER)

# 🔤 TITLE
Label(card, text="Login", font=("Arial", 22, "bold"), bg="white").pack(pady=20)

# 👤 USERNAME
Label(card, text="Username", font=("Arial", 11), bg="white").pack(anchor="w")
username_entry = Entry(card, width=35, font=("Arial", 12), bd=2, relief=GROOVE)
username_entry.pack(pady=10, ipady=5)

# 🔒 PASSWORD
Label(card, text="Password", font=("Arial", 11), bg="white").pack(anchor="w")

pass_frame = Frame(card, bg="white")
pass_frame.pack(pady=10)

pass_entry = Entry(pass_frame, show="*", width=27, font=("Arial", 12), bd=2, relief=GROOVE)
pass_entry.pack(side=LEFT, ipady=5)

show_btn = Button(pass_frame, text="Show", command=toggle_password)
show_btn.pack(side=LEFT, padx=5)

# 🔘 LOGIN BUTTON
Button(card, text="Login",
       width=25,
       height=2,
       bg="#2ecc71",
       fg="white",
       font=("Arial", 12, "bold"),
       command=login).pack(pady=20)
# 🔗 OPTIONS
Label(card, text="Don't have an account?", bg="white").pack()

Button(card, text="Register",
       bg="white", fg="blue", bd=0,
       cursor="hand2",
       command=open_register).pack()

Button(card, text="Provide Service",
       bg="white", fg="blue", bd=0,
       cursor="hand2",
       command=open_service_provider_register).pack()

Button(card, text="Forgot Password?",
       bg="white", fg="red", bd=0,
       cursor="hand2",
       command=forgot_password).pack(pady=10)
# 📢 STATUS
status_label = Label(card, text="", bg="white", font=("Arial", 10))
status_label.pack()



root.mainloop()