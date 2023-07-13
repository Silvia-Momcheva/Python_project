import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


def show_merged_data(merged_data):
    root = tk.Tk()
    root.title('2 задача')
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)

    style = ttk.Style()
    style.configure("Treeview", borderwidth=1, relief="solid")

    columns = ["Код на стока", "Дата продажба",
               "Ед.цена", "Количество", "Продукт", "Група", "Описание"]

    table["columns"] = columns
    table.column("#0", width=50, anchor="center")
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, anchor="center")

    for i, row in enumerate(merged_data):
        table.insert("", "end", text=i + 1, values=row)
    root.mainloop()
