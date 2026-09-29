import tkinter as tk
from tkinter import ttk, messagebox
import json, os, hashlib


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Авторизация")
        self.geometry("320x260")
        self.resizable(False, False)

        self.mode = "login"
        self.build_ui()

    def build_ui(self):
        self.clear()

        title = "Вход" if self.mode == "login" else "Регистрация"
        btn_text = "Войти" if self.mode == "login" else "Создать"
        switch = "Регистрация" if self.mode == "login" else "Вход"

        tk.Label(self, text=title, font=("Arial", 14, "bold")).pack(pady=10)

        f = tk.Frame(self)
        f.pack(pady=5)

        tk.Label(f, text="Логин:").grid(row=0, column=0, padx=5, sticky="e")
        self.e1 = tk.Entry(f, width=20)
        self.e1.grid(row=0, column=1, padx=5)

        tk.Label(f, text="Пароль:").grid(row=1, column=0, padx=5, sticky="e")
        self.e2 = tk.Entry(f, show="*", width=20)
        self.e2.grid(row=1, column=1, padx=5)

        tk.Label(f, text="Роль:").grid(row=2, column=0, padx=5, sticky="e")
        self.c = ttk.Combobox(f, values=["Администратор", "Пользователь"], state="readonly", width=18)
        self.c.grid(row=2, column=1, padx=5)
        self.c.set("Пользователь")

        tk.Button(self, text=btn_text, command=self.action, width=15).pack(pady=10)
        tk.Button(self, text=switch, fg="blue", command=self.switch, relief="flat", bg=self.cget("bg")).pack()

    def clear(self):
        for w in self.winfo_children():
            w.destroy()

    def switch(self):
        self.mode = "reg" if self.mode == "login" else "login"
        self.build_ui()

    def action(self):
        l, p = self.e1.get().strip(), self.e2.get()
        if not l or not p:
            return messagebox.showerror("Ошибка", "Заполните все поля!")

        users = self.load()

        if self.mode == "login":
            if l in users and users[l]["password"] == self.h(p):
                messagebox.showinfo("Успех", f"Добро пожаловать, {l}!\nРоль: {users[l]['role']}")
            else:
                messagebox.showerror("Ошибка", "Неверный логин или пароль!")
        else:
            if len(l) < 3:
                return messagebox.showerror("Ошибка", "Логин минимум 3 символа!")
            if len(p) < 4:
                return messagebox.showerror("Ошибка", "Пароль минимум 4 символа!")
            if l in users:
                return messagebox.showerror("Ошибка", "Логин уже занят!")
            users[l] = {"password": self.h(p), "role": self.c.get()}
            self.save(users)
            messagebox.showinfo("Успех", "Регистрация успешна!")
            self.switch()

    @staticmethod
    def load():
        try:
            with open("users.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}

    @staticmethod
    def save(u):
        with open("users.json", "w", encoding="utf-8") as f:
            json.dump(u, f, ensure_ascii=False, indent=2)

    @staticmethod
    def h(p):
        return hashlib.sha256(p.encode()).hexdigest()


if __name__ == "__main__":
    App().mainloop()