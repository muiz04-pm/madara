import tkinter as tk

def check_numbers():
    data = entry.get()
    if not data.strip():
        result_label.config(text="Введите данные!")
        return
    items = [item.strip() for item in data.split(',')]
    count = sum(1 for item in items if any(c.isdigit() for c in item))
    result_label.config(text=f"Элементов с цифрами: {count}")

root = tk.Tk()
root.title("Поиск чисел")
root.geometry("400x150")

tk.Label(root, text="Введите через запятую:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Проверить", command=check_numbers).pack(pady=5)
result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()