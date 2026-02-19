import tkinter as tk
from tkinter import messagebox

# Функция для показа сообщения
def show_position(position_name):
    messagebox.showinfo("Позиция", f"Кнопка расположена: {position_name}")

# Создаём главное окно
root = tk.Tk()
root.title("Кнопки по диагонали")
root.geometry("400x300")

# Кнопка в верхнем левом углу (NW)
btn_nw = tk.Button(root, text="NW", command=lambda: show_position("в верхнем левом углу"))
btn_nw.place(x=10, y=10)

# Кнопка в верхнем правом углу (NE)
btn_ne = tk.Button(root, text="NE", command=lambda: show_position("в верхнем правом углу"))
btn_ne.place(x=350, y=10, anchor="ne")

# Кнопка в нижнем левом углу (SW)
btn_sw = tk.Button(root, text="SW", command=lambda: show_position("в нижнем левом углу"))
btn_sw.place(x=10, y=270, anchor="sw")

# Кнопка в нижнем правом углу (SE)
btn_se = tk.Button(root, text="SE", command=lambda: show_position("в нижнем правом углу"))
btn_se.place(x=390, y=290, anchor="se")

# Запуск приложения
root.mainloop()