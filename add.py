import csv
import tkinter as tk

def add_show(csv_file):
    def add():
        # вземат се въведените данни от полетата
        stoka_number = stoka_number_entry.get()
        stoka_name = stoka_name_entry.get()
        group = group_entry.get()
        
        # отваряне на CSV файл за добавяне на нов запис
        with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # запис на новия продукт във файла
            writer.writerow([stoka_number, stoka_name, group])
        
        # изчистване на полетата след добавянето на продукта
        stoka_number_entry.delete(0, tk.END)
        stoka_name_entry.delete(0, tk.END)
        group_entry.delete(0, tk.END)
        
        # показване на съобщение за успешно добавяне на продукта
        message_label.config(text="Новият продукт е добавен успешно.")
    
    # създаване на главното прозорец на GUI приложението
    root = tk.Tk()
    root.title("Добавяне на Продукт")
    root.geometry("350x200")
    
    # създаване на надписи и полета за въвеждане на данни
    stoka_number_label = tk.Label(root, text="Код на продукта: ", bg="#F6F1E9", fg="#000000")
    stoka_number_label.grid(row=0, column=0, padx=10, pady=5)
    stoka_number_entry = tk.Entry(root)
    stoka_number_entry.grid(row=0, column=1, padx=5, pady=5)
    
    stoka_name_label = tk.Label(root, text="Име на продукта: ", bg="#F6F1E9", fg="#000000")
    stoka_name_label.grid(row=1, column=0, padx=10, pady=5)
    stoka_name_entry = tk.Entry(root)
    stoka_name_entry.grid(row=1, column=1, padx=5, pady=5)
    
    group_label = tk.Label(root, text="Група: ", bg="#F6F1E9", fg="#000000")
    group_label.grid(row=4, column=0, padx=10, pady=5)
    group_entry = tk.Entry(root)
    group_entry.grid(row=4, column=1, padx=5, pady=5)
    
    # създаване на бутон за добавяне на продукта
    add_stoki_button = tk.Button(root, text="Добави Артикула", activebackground="#FF8400", activeforeground="#F6F1E9", bg="#F6F1E9", fg="#000000", command=add)
    add_stoki_button.grid(row=6, column=0, columnspan=1, padx=5, pady=5)
    
    # показване на съобщението
    message_label = tk.Label(root, text="", fg="#000000")
    message_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
    
    root.mainloop()
