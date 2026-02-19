import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow
import random
import csv
import os

# ===== Файл для хранения пользователей =====
USER_FILE = "users.csv"

# ===== Инициализация CSV файла =====
def init_user_file():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password", "name", "email"])

# ===== Регистрация =====
def register_user():
    username = entry_reg_username.get()
    password = entry_reg_password.get()
    confirm = entry_reg_confirm.get()
    name = entry_reg_name.get()
    email = entry_reg_email.get()

    if not all([username, password, confirm, name, email]):
        messagebox.showerror("Ошибка", "Заполните все поля")
        return

    if password != confirm:
        messagebox.showerror("Ошибка", "Пароли не совпадают")
        return

    # Проверка, существует ли уже пользователь
    with open(USER_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row and row[0] == username:
                messagebox.showerror("Ошибка", "Пользователь уже существует")
                return

    # Сохраняем
    with open(USER_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, password, name, email])
    messagebox.showinfo("Успех", "Регистрация прошла успешно!")
    clear_reg_fields()
    notebook.select(frame_login)  # переключаем на вкладку авторизации

def clear_reg_fields():
    entry_reg_username.delete(0, tk.END)
    entry_reg_password.delete(0, tk.END)
    entry_reg_confirm.delete(0, tk.END)
    entry_reg_name.delete(0, tk.END)
    entry_reg_email.delete(0, tk.END)

# ===== Авторизация =====
def login_user():
    username = entry_login_username.get()
    password = entry_login_password.get()
    if not username or not password:
        messagebox.showerror("Ошибка", "Введите логин и пароль")
        return


    with open(USER_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row and row[0] == username and row[1] == password:
                messagebox.showinfo("Успех", f"Добро пожаловать, {row[2]}!")
                open_main_app(row[2], row[3])  # открываем главное окно
                return

    messagebox.showerror("Ошибка", "Неверный логин или пароль")

# ===== Главное приложение (после входа) =====
def open_main_app(user_name, user_email):
    # Закрываем окно авторизации
    root.withdraw()

    # Создаём главное окно
    main_window = tk.Toplevel()
    main_window.title("Форма абитуриента - Ренсингшва")
    main_window.geometry("500x500")

    # Приветствие
    tk.Label(main_window, text=f"Добро пожаловать, {user_name}!", font=("Arial", 12, "bold"), fg="green").pack(pady=5)

    # Кнопка поздравления Ильи
    btn_birthday = tk.Button(main_window, text="🎂 Поздравить Илью", command=show_birthday_card, bg="#ffcc00")
    btn_birthday.pack(pady=5)

    # Вкладки (только Личный кабинет)
    notebook_main = ttk.Notebook(main_window)
    notebook_main.pack(fill='both', expand=True, padx=10, pady=5)

    # === Вкладка 1: Личный кабинет ===
    frame_profile = ttk.Frame(notebook_main)
    notebook_main.add(frame_profile, text="Личный кабинет")

    tk.Label(frame_profile, text="Имя:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_name = tk.Entry(frame_profile)
    entry_name.insert(0, user_name)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_profile, text="Фамилия:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_surname = tk.Entry(frame_profile)
    entry_surname.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_profile, text="Дата рождения:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_birth = tk.Entry(frame_profile)
    entry_birth.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_profile, text="Email:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_email = tk.Entry(frame_profile)
    entry_email.insert(0, user_email)
    entry_email.grid(row=3, column=1, padx=10, pady=5)

    def save_profile():
        # Здесь можно добавить сохранение изменений
        messagebox.showinfo("Сохранено", "Данные личного кабинета сохранены ✅")

    tk.Button(frame_profile, text="Сохранить", command=save_profile, bg="#4CAF50", fg="white").grid(row=4, column=0, columnspan=2, pady=10)

    # === Блок 2: Советник Енгельс ===
    frame_engels = tk.LabelFrame(main_window, text="Дорогия советник Енгельс", padx=10, pady=10)
    frame_engels.pack(fill='x', padx=10, pady=5)

    tk.Label(frame_engels, text="• Не менее 8 сменных").pack(anchor="w")
    tk.Label(frame_engels, text="• У одного секретаря для одного (если он есть)").pack(anchor="w")

    # === Блок 3: После увольнения ===
    frame_dismiss = tk.LabelFrame(main_window, text="После увольнения", padx=10, pady=10)
    frame_dismiss.pack(fill='x', padx=10, pady=5)

    tk.Label(frame_dismiss, text="• Капитанский К. 234 старый Лейб С.").pack(anchor="w")
    tk.Label(frame_dismiss, text="• Название").pack(anchor="w")

    # Кнопка выхода
    tk.Button(main_window, text="Выйти", command=lambda: exit_app(main_window), bg="red", fg="white").pack(pady=5)

def exit_app(window):
    window.destroy()
    root.deiconify()  # показываем окно авторизации

# ===== Поздравительная функция для Ильи =====
def show_birthday_card():
    card = tk.Toplevel()
    card.title("С Днём Рождения, Илья! 🎂")
    card.geometry("400x300")
    card.configure(bg="#ffe6f0")

    try:
        image = Image.open("birthday.jpg")
        image = image.resize((200, 150), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label_img = tk.Label(card, image=photo, bg="#ffe6f0")
        label_img.image = photo
        label_img.pack(pady=10)
    except:
        tk.Label(card, text="🎈 🎉 🎂", font=("Arial", 40), bg="#ffe6f0").pack(pady=20)

    tk.Label(card, text="Илья, с Днём Рождения! 🎁", font=("Arial", 16, "bold"), bg="#ffe6f0", fg="#b30059").pack(pady=10)

    wishes = [
        "Желаем счастья, здоровья и успехов!",
        "Пусть сбудутся все мечты!",
        "Ты лучший! 🚀",
        "Удачи в поступлении в Ренсингшву!",
        "Пусть каждый день радует!"
    ]
    tk.Label(card, text=random.choice(wishes), font=("Arial", 12), bg="#ffe6f0", fg="#800080").pack(pady=10)
    tk.Button(card, text="Закрыть", command=card.destroy, bg="#ff99bb").pack(pady=10)

# ===== Окно авторизации/регистрации =====
root = tk.Tk()
root.title("Авторизация / Регистрация")
root.geometry("400x400")

init_user_file()

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

# === Вкладка Авторизация ===
frame_login = ttk.Frame(notebook)
notebook.add(frame_login, text="Авторизация")

tk.Label(frame_login, text="Логин:", font=("Arial", 10)).pack(pady=5)
entry_login_username = tk.Entry(frame_login, width=30)
entry_login_username.pack()

tk.Label(frame_login, text="Пароль:", font=("Arial", 10)).pack(pady=5)
entry_login_password = tk.Entry(frame_login, width=30, show="*")
entry_login_password.pack()

tk.Button(frame_login, text="Войти", command=login_user, bg="#4CAF50", fg="white", width=20).pack(pady=10)

# === Вкладка Регистрация ===
frame_register = ttk.Frame(notebook)
notebook.add(frame_register, text="Регистрация")

tk.Label(frame_register, text="Логин:", font=("Arial", 10)).pack(pady=2)
entry_reg_username = tk.Entry(frame_register, width=30)
entry_reg_username.pack()

tk.Label(frame_register, text="Пароль:", font=("Arial", 10)).pack(pady=2)
entry_reg_password = tk.Entry(frame_register, width=30, show="*")
entry_reg_password.pack()

tk.Label(frame_register, text="Подтвердите пароль:", font=("Arial", 10)).pack(pady=2)
entry_reg_confirm = tk.Entry(frame_register, width=30, show="*")
entry_reg_confirm.pack()

tk.Label(frame_register, text="Имя:", font=("Arial", 10)).pack(pady=2)
entry_reg_name = tk.Entry(frame_register, width=30)
entry_reg_name.pack()

tk.Label(frame_register, text="Email:", font=("Arial", 10)).pack(pady=2)
entry_reg_email = tk.Entry(frame_register, width=30)
entry_reg_email.pack()

tk.Button(frame_register, text="Зарегистрироваться", command=register_user, bg="#2196F3", fg="white", width=20).pack(pady=10)

# Запуск
root.mainloop()