import tkinter as tk
import tkinter.font as tkFont
from table_utils import show_merged_data
from tkinter import ttk


class AppGUI:
    def __init__(self, root, merged_data):
        self.merged_data = merged_data

        # Setting title
        root.title(
            "Курсова работа Силвия, Сахем, Рабие")
        # Setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_517 = tk.Button(root)
        GButton_517["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_517["font"] = ft
        GButton_517["fg"] = "#000000"
        GButton_517["justify"] = "center"
        GButton_517["text"] = "2 Задача"
        GButton_517.place(x=230, y=210, width=70, height=25)
        GButton_517["command"] = self.GButton_517_command

        GButton_summary = tk.Button(root)
        GButton_summary["bg"] = "#f0f0f0"
        GButton_summary["font"] = ft
        GButton_summary["fg"] = "#000000"
        GButton_summary["justify"] = "center"
        GButton_summary["text"] = "Обобщение"
        GButton_summary.place(x=320, y=210, width=100, height=25)
        GButton_summary["command"] = self.GButton_summary_command

        self.date_entry = tk.Entry(root)
        self.date_entry.place(x=420, y=210, width=80, height=25)

        search_button = tk.Button(root)
        search_button["bg"] = "#f0f0f0"
        search_button["font"] = ft
        search_button["fg"] = "#000000"
        search_button["justify"] = "center"
        search_button["text"] = "Търси"
        search_button.place(x=510, y=210, width=70, height=25)
        search_button["command"] = self.search_button_command

    def GButton_517_command(self):
        show_merged_data(self.merged_data)

    def GButton_summary_command(self):
        summary = self.generate_summary()
        self.show_summary(summary)

    def search_button_command(self):
        date = self.date_entry.get()
        results = self.search_by_date(date)
        self.show_search_results(results)

    def generate_summary(self):
        summary = {}
        for row in self.merged_data:
            product_code = row[0]
            total_price = float(row[2]) * int(row[3])
            product = row[4]
            description = row[6]
            if product_code in summary:
                summary[product_code]['total_price'] += total_price
            else:
                summary[product_code] = {
                    'total_price': total_price,
                    'product': product,
                    'description': description
                }
        return summary

    def show_summary(self, summary):
        root = tk.Tk()
        root.title('Обобщение')
        table = ttk.Treeview(root)
        table.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure("Treeview", borderwidth=1, relief="solid")

        columns = ["Код на стока", "Продукт",
                   "Описание", "Обща сума"]

        table["columns"] = columns
        table.column("#0", width=50, anchor="center")
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=100, anchor="center")

        for i, (product_code, data) in enumerate(summary.items()):
            table.insert("", "end", text=i + 1, values=[
                product_code,
                data['product'],
                data['description'],
                data['total_price']
            ])
        root.mainloop()

    def search_by_date(self, date):
        results = []
        for row in self.merged_data:
            if row[1] == date:
                total_price = float(row[2]) * int(row[3])
                row.append(total_price)
                results.append(row)
        return results

    def show_search_results(self, results):
        root = tk.Tk()
        root.title('Резултати от търсенето')
        table = ttk.Treeview(root)
        table.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure("Treeview", borderwidth=1, relief="solid")

        columns = ["Код на стока", "Дата продажба",
                   "Ед. цена", "Количество", "Продукт", "Обща сума"]

        table["columns"] = columns
        table.column("#0", width=50, anchor="center")
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=100, anchor="center")

        for i, row in enumerate(results):
            table.insert("", "end", text=i + 1, values=row)
        root.mainloop()


def main():
    pr_file = "product.csv"
    st_file = "stock.csv"
    vidove_file = "vidove.csv"


if __name__ == '__main__':
    main()
