import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


def show_merged_data1(merged_data):
    # Създаване на основния прозорец
    root = tk.Tk()
    root.title('3 задача')

    # Създаване на таблицата
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)

    # Конфигуриране на стиловете на таблицата
    style = ttk.Style()
    style.configure("Treeview", borderwidth=1, relief="solid")

    # Дефиниране на колоните на таблицата
    columns = ["Код на стока", "Вид", "Дата", "Сума"]

    # Задаване на колоните на таблицата
    table["columns"] = columns

    # Конфигуриране на ширината и текста на колоните
    table.column("#0", width=50, anchor="center")
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, anchor="center")

    # въвеждане на данните в таблицата по редове
    for i, row in enumerate(merged_data):
        code = row[0]
        vid = row[6]
        name = row[1]
        quantity = int(row[3])
        price = float(row[2])
        total = quantity * price

        # Вмъкване на ред в таблицата
        table.insert("", "end", text=i + 1, values=[code, vid, name, total])

    # Стартиране на главния цикъл на прозореца
    root.mainloop()
