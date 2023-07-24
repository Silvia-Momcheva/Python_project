import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def read1(csv_file):
    # Функция за четене на данните от CSV файл
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        data_list1 = []
        for row in csvreader:
            data_list1.append(row)  
        return data_list1

def show_csv_data(data_list1, data_list2, data_list3):
    # Функция за показване на данните

    def tyrsene():
        # Функция за търсене на продукт със същата или по-ниска цена спрямо въведената сума
        
        stoka_cena = stoka_cena_entry.get() 
        stoka_cena_entry.delete(0, tk.END)
        data_list = {}
        data_list4 = []
        
        # Създаване на речник, където ключовете са кодовете на стоките от data_list2, а стойностите са 1
        for i2 in data_list2[1:]:
            data_list[i2[0]] = 1
                
        # Изчисляване на общата сума на продуктите със същите кодове като тези от data_list2
        for i2 in data_list2[1:]:
            for i3 in data_list.keys():
                if i2[0] == i3:
                    data_list[i2[0]] += (float(i2[2]) * float(i2[3])) 
                    break
        
        # Обновяване на данните в data_list3 с информация от data_list1
        for i1 in data_list3:
            for i2 in data_list1:
                if i1[2] == i2[0]:
                    i1.insert(2, i2[1])
                    i1.remove(i2[0])
                    break
        
        # Добавяне на стойност "Сума" във втората позиция на първия ред от data_list3
        for i1 in data_list3:
            value = "Сума"
            i1.insert(3, value)
            data_list4.append(i1)
            break
    
        # Добавяне на общата сума на продуктите към съответния ред от data_list3
        for i1 in data_list3[1:]:
            check = False
            for i3 in data_list.keys():
                if i1[0] == i3:
                    value = round(data_list.get(i3), 2)
                    i1.insert(3, value)
                    check = True
                    break
            if check == True:
                data_list4.append(i1)
        
        data_list_search = {}
        data_list5 = {}
        data_list_search_cena = []
        
        # Създаване на речник, където ключовете са общите суми от data_list4, а стойностите са 1
        for i2 in data_list.values():
            data_list5[round(i2, 2)] = 1
                
        # Групиране на редовете от data_list4 по общи суми
        for i2 in data_list4[1:]:
            for i3 in data_list5.keys():
                if i2[3] == i3:
                    data_list_search.setdefault(float(i2[3]), []).append(i2)
        
        # Добавяне на реда с общата сума към data_list_search_cena
        for i2 in data_list4:
            data_list_search_cena.append(i2)
            break
        
        # Филтриране на редовете според въведената сума
        for item in data_list_search.keys():
            if item <= float(stoka_cena):
                value = data_list_search.get(item)
                for i in value:
                    data_list_search_cena.append(i)
        
        root.destroy()
        
        if len(data_list_search_cena) == 1:
            # Проверка за наличие на данни за въведената сума
            response = messagebox.askyesno('Грешка', 'Няма данни за въведената сума.')
            if response:
                root.destroy()
        else: 
            import show
            show.show(data_list_search_cena)
    
    root = tk.Tk()
    root.title('Търсене по цена на Стока')
    
    stoka_cena_label = tk.Label(root, text="Въведете сума до: ", bg="#F6F1E9", fg="#000000")
    stoka_cena_label.grid(row=0, column=0, padx=20, pady=20)
    
    stoka_cena_entry = tk.Entry(root)
    stoka_cena_entry.grid(row=0, column=1, padx=20, pady=20)
    
    search_cena_button = tk.Button(root, text="Търсене на продукт със същата или по-ниска цена спрямо въведената горе.",
                                   activebackground="#1e90ff", activeforeground="#ffd700", bg="#F6F1E9", fg="#000000", command=tyrsene)
    search_cena_button.grid(row=0, column=3, columnspan=2, padx=10, pady=10)
    
    root.mainloop()
