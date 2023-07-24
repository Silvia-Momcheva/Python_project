import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

# Функция за показване на обобщените данни


def show_merged_data(merged_data):
    root = tk.Tk()
    root.title('2 задача')

    # Създаване на таблица
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)

    # Конфигуриране на стила на таблицата
    style = ttk.Style()
    style.configure("Treeview", borderwidth=1, relief="solid")

    columns = ["Код на стока", "Дата продажба", "Ед.цена",
               "Количество", "Продукт", "Група", "Описание"]

    # Задаване на колоните на таблицата
    table["columns"] = columns
    table.column("#0", width=50, anchor="center")

    # Задаване на заглавия и ширина на колоните
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, anchor="center")

    # Вмъкване на редовете в таблицата
    for i, row in enumerate(merged_data):
        table.insert("", "end", text=i + 1, values=row)

    root.mainloop()

# Функция за показване на обобщените данни


def show_merged_data2(data):
    root = tk.Tk()
    root.title('Таблица с данни')

    table = ttk.Treeview(root)
    table["columns"] = ("code", "date", "price", "quantity", "total")

    table.column("#0", width=0, stretch=tk.NO)
    table.column("code", anchor=tk.CENTER, width=100)
    table.column("date", anchor=tk.CENTER, width=100)
    table.column("price", anchor=tk.CENTER, width=100)
    table.column("quantity", anchor=tk.CENTER, width=100)
    table.column("total", anchor=tk.CENTER, width=100)

    table.heading("code", text="Код на стока")
    table.heading("date", text="Дата на продажба")
    table.heading("price", text="Единична цена")
    table.heading("quantity", text="Количество")
    table.heading("total", text="Сума")

    for row in data:
        table.insert("", tk.END, values=row)

    table.pack()

    root.mainloop()

# Функция за показване на филтрираните данни


def show_filtered_data(filtered_data):
    root = tk.Tk()
    root.title('Таблица с филтрирани данни')
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)

    style = ttk.Style()
    style.configure("Treeview", borderwidth=1, relief="solid")

    columns = ["Код на стока", "Дата продажба",
               "Ед.цена", "Количество", "Сума"]

    # Задаване на колоните на таблицата
    table["columns"] = columns
    table.column("#0", width=50, anchor="center")

    # Задаване на заглавия и ширина на колоните
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, anchor="center")

    # Вмъкване на редовете в таблицата
    for i, row in enumerate(filtered_data):
        code = row[0]
        date = row[1]
        price = row[2]
        quantity = row[3]
        total = float(price) * int(quantity)
        table.insert(parent="", index=i, iid=i, values=(
            code, date, price, quantity, total))

    root.mainloop()
