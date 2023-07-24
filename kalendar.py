import tkinter as tk
from tkinter import ttk, messagebox
from data_utils import merge_data

def show_data_by_date(merged_data):
    # Функция за извеждане на данни по дата
    def filter_data():
        # Функция за филтриране на данните според въведената дата
        input_date = entry_date.get()
        filtered_data = [row for row in merged_data if row[1] == input_date]

        if not filtered_data:
            messagebox.showinfo("Няма данни", "Няма налични данни за въведената дата.")
        else:
            show_data_table(filtered_data)

    def show_data_table(data):
        # Функция за показване на таблица с данните
        root = tk.Tk()
        root.title("Таблица с данни")

        table = ttk.Treeview(root)
        table["columns"] = ("Код", "Дата", "Количество", "Единична цена", "Име", "Вид", "Име вид", "Обща цена")

        # Дефиниране на колоните в таблицата
        table.column("#0", width=0, stretch=tk.NO)
        table.column("Код", anchor=tk.W, width=100)
        table.column("Дата", anchor=tk.W, width=100)
        table.column("Количество", anchor=tk.W, width=100)
        table.column("Единична цена", anchor=tk.W, width=100)
        table.column("Име", anchor=tk.W, width=100)
        table.column("Вид", anchor=tk.W, width=100)
        table.column("Име вид", anchor=tk.W, width=100)
        table.column("Обща цена", anchor=tk.W, width=100)

        # Дефиниране на заглавията на колоните
        table.heading("#0", text="", anchor=tk.W)
        table.heading("Код", text="Код", anchor=tk.W)
        table.heading("Дата", text="Дата", anchor=tk.W)
        table.heading("Количество", text="Количество", anchor=tk.W)
        table.heading("Единична цена", text="Единична цена", anchor=tk.W)
        table.heading("Име", text="Име", anchor=tk.W)
        table.heading("Вид", text="Вид", anchor=tk.W)
        table.heading("Име вид", text="Име вид", anchor=tk.W)
        table.heading("Обща цена", text="Обща цена", anchor=tk.W)

        # Добавяне на данните в таблицата
        for row in data:
            quantity = int(row[3])
            price = float(row[2])
            total = quantity * price
            row.append(total)

            table.insert(parent="", index="end", text="", values=row)

        table.pack(fill="both", expand=True)

        root.mainloop()

    # Създаване на графичен интерфейс
    root = tk.Tk()
    root.title("Въведете дата")
    root.geometry("300x100")

    label_date = tk.Label(root, text="Дата (ДД.М.ГГГГ):")
    label_date.pack()

    entry_date = tk.Entry(root)
    entry_date.pack()

    button_submit = tk.Button(root, text="Покажи данните", command=filter_data)
    button_submit.pack()

    root.mainloop()

if __name__ == "__main__":
    pr_file = "prodajbi.csv"
    st_file = "stoki.csv"
    vidove_file = "vidove.csv"

    # Сливане на данните от файловете prodajbi.csv и stoki.csv
    merged_data = merge_data(pr_file, st_file)

    # Показване на данните по дата
    show_data_by_date(merged_data)
