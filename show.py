import csv
import tkinter as tk
from tkinter import ttk


def show(data_list_search):
    root = tk.Tk()
    root.title("Данните по конкретна стойност")

    # Създаване на таблица
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)

    # Дефиниране на колоните на таблицата
    table["columns"] = data_list_search[0]

    # Заглавие на първа колона
    table.heading("#0", text="Index")
    table.column("#0", width=50)

    # Заглавия и ширина на останалите колони
    for col in data_list_search[0]:
        table.heading(col, text=col)
        table.column(col, width=100)

    # Вмъкване на редовете в таблицата
    for i, row in enumerate(data_list_search[1:]):
        table.insert("", "end", text=i+1, values=row)

    root.mainloop()
