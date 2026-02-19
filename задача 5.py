import tkinter as tk
from tkinter import messagebox

def submit():
    username = entry_user.get()
    password = entry_pass.get()
    if username and password:
        label_status.config(text="Выполнен вход", fg="green")
    else:
        label_status.config(text="Заполните поля", fg="red")

def clear():
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)
    label_status.config(text="")

root = tk.Tk()
root.title("Форма входа")
root.geometry("300x200")

tk.Label(root, text="Username:").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password:").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Submit", command=submit).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack()
tk.Button(root, text="Close", command=root.quit).pack(pady=5)

label_status = tk.Label(root, text="", font=("Arial", 10))
label_status.pack()

root.mainloop()