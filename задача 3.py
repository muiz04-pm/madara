import tkinter as tk
from tkinter import messagebox

def submit():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        messagebox.showinfo("Успех", f"Добро пожаловать, {username}!")
    else:
        messagebox.showerror("Ошибка", "Введите логин и пароль")

def clear():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

root = tk.Tk()
root.title("Task 2: Авторизация")
root.geometry("300x200")

tk.Label(root, text="Логин:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Пароль:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Войти", command=submit).pack(pady=10)
tk.Button(root, text="Очистить", command=clear).pack()
tk.Button(root, text="Закрыть", command=root.quit).pack(pady=5)

root.mainloop()