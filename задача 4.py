import tkinter as tk
from tkinter import messagebox
import csv
import os

def hash_password(password):
    return sum(ord(char) for char in password)

def save_to_csv():
    password = entry.get()
    if not password:
        messagebox.showerror("Ошибка", "Введите пароль")
        return
    hashed = hash_password(password)
    with open("passwords.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([password, hashed])
    entry.delete(0, tk.END)
    messagebox.showinfo("Успех", "Сохранено!")

def clear_csv():
    if os.path.exists("passwords.csv"):
        os.remove("passwords.csv")
        messagebox.showinfo("Успех", "Файл очищен")
    else:
        messagebox.showwarning("Внимание", "Файла не существует")

root = tk.Tk()
root.title("Хеширование паролей")
root.geometry("300x200")

tk.Label(root, text="Введите пароль:").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack()

tk.Button(root, text="Хеш (посчитать)", command=lambda: messagebox.showinfo("Хеш", f"Сумма Unicode: {hash_password(entry.get())}")).pack(pady=5)
tk.Button(root, text="Сохранить в CSV", command=save_to_csv).pack()
tk.Button(root, text="Очистить CSV", command=clear_csv).pack(pady=5)

root.mainloop()