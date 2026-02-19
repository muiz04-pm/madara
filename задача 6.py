import tkinter as tk
from tkinter import messagebox

def save_to_file():
    data = [
        entry_name.get(),
        entry_surname.get(),
        entry_class.get(),
        entry_group.get()
    ]
    if all(data):
        with open("students.txt", "a", encoding="utf-8") as f:
            f.write(",".join(data) + "\n")
        messagebox.showinfo("Успех", "Данные сохранены")
        for e in [entry_name, entry_surname, entry_class, entry_group]:
            e.delete(0, tk.END)
    else:
        messagebox.showerror("Ошибка", "Заполните все поля")

root = tk.Tk()
root.title("Запись в файл")
root.geometry("300x250")

fields = ["Имя", "Фамилия", "Класс", "Группа"]
entries = []

for i, field in enumerate(fields):
    tk.Label(root, text=field + ":").pack()
    e = tk.Entry(root)
    e.pack()
    entries.append(e)

entry_name, entry_surname, entry_class, entry_group = entries

tk.Button(root, text="Сохранить", command=save_to_file).pack(pady=10)

root.mainloop()