import csv
from logging import root
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


def show_table(data_list_search):
    # Функция за показване на таблица с данните
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)
    table["columns"] = data_list_search[0]
    table.heading("#0", text="Index")
    table.column("#0", width=50)
    for col in data_list_search[0]:
        table.heading(col, text=col)
        table.column(col, width=100)
    for i, row in enumerate(data_list_search[1:]):
        table.insert("", "end", text=i+1, values=row)


def read1(csv_file):
    # Функция за четене на данни от CSV файл
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        data_list1 = []
        for row in csvreader:
            data_list1.append(row)
        return data_list1


def show_csv_data(data1, data2, data3):
    def search():
        # Функция за търсене на данни по име на стока
        stoka = stokaentry.get()
        stokaentry.delete(0, tk.END)
        datasearch = []

        # Сливане на данните от data2 и data3
        for i1 in data2:
            for i2 in data3:
                if i1[0] == i2[0]:
                    i1.insert(1, i2[1])
                    i1.insert(2, i2[2])
                    break

        # Сливане на данните от data3 и data1
        for i1 in data3:
            for i2 in data1:
                if i1[2] == i2[0]:
                    i1.insert(3, i2[1])
                    break

        # Проверка на съвпадение на името на стоката и създаване на нов списък със съответните данни
        for dat1 in data3:
            datasearch.append(dat1)
            break
        for dat1 in data3:
            if dat1[1] == stoka:
                datasearch.append(dat1)

        root.destroy()

        if len(datasearch) == 1:
            # Проверка за наличие на данни и показване на съобщение за грешка
            a = messagebox.showerror(
                'Грешка', 'Няма информация')
            if a:
                root.destroy()
        else:
            import show
            show.show(datasearch)

    root = tk.Tk()
    root.title('Търене по име на стока')

    stoka_data_label = tk.Label(
        root, text="Въведете име на стока: ", bg="white", fg="black")
    stoka_data_label.grid(row=0, column=0, padx=20, pady=15)

    stokaentry = tk.Entry(root)
    stokaentry.grid(row=0, column=1, padx=20, pady=15)

    search_stoki_button = tk.Button(root, text="Търси по име на стока",
                                    activebackground="white", activeforeground="orange", bg="white", fg="black", command=search)
    search_stoki_button.grid(row=0, column=3, columnspan=2, padx=5, pady=5)

    root.mainloop()
