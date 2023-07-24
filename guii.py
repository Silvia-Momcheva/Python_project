import tkinter as tk
import tkinter.font as tkFont
from table_utils import show_merged_data
from oborot import show_merged_data1
import tkinter.filedialog as filedialog
import os
from kalendar import show_data_by_date
from data_utils import merge_data, merge_group_data
import csv 
from tkinter import messagebox

csv_file1 = "vidove.csv"
csv_file2 = "prodajbi.csv"
csv_file3 = "stoki.csv"

class App:
    def __init__(self, root, merged_data):
        self.merged_data = merged_data
        #заглавие
        root.title("Курсова работа - Силвия, Сахем, Рабие")
        #размер на прозореца
        width=864
        height=572
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_335=tk.Label(root)
        GLabel_335["anchor"] = "center"
        GLabel_335["bg"] = "#dce8f7"
        ft = tkFont.Font(family='Times',size=38)
        GLabel_335["font"] = ft
        GLabel_335["fg"] = "#0a1b55"
        GLabel_335["justify"] = "center"
        GLabel_335["text"] = "Хранителен Магазин ССР"
        GLabel_335.place(x=0,y=0,width=863,height=120)

        GButton_321=tk.Button(root)
        GButton_321["activebackground"] = "#3d6571"
        GButton_321["activeforeground"] = "#ffffff"
        GButton_321["bg"] = "#c7fef8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_321["font"] = ft
        GButton_321["fg"] = "#000000"
        GButton_321["justify"] = "center"
        GButton_321["text"] = "ДОБАВЯНЕ НА ПРОДУКТИ"
        GButton_321["relief"] = "raised"
        GButton_321.place(x=80,y=150,width=311,height=72)
        GButton_321["command"] = self.GButton_321_command

        GButton_300=tk.Button(root)
        GButton_300["activebackground"] = "#b4e3e3"
        GButton_300["activeforeground"] = "#000000"
        GButton_300["bg"] = "#3f8184"
        ft = tkFont.Font(family='Times',size=10)
        GButton_300["font"] = ft
        GButton_300["fg"] = "#000000"
        GButton_300["justify"] = "center"
        GButton_300["text"] = "ТЪРСЕНЕ ПО ИМЕ НА СТОКА"
        GButton_300["relief"] = "raised"
        GButton_300.place(x=80,y=320,width=311,height=113)
        GButton_300["command"] = self.GButton_300_command

        GButton_923=tk.Button(root)
        GButton_923["activebackground"] = "#2c5871"
        GButton_923["activeforeground"] = "#ffffff"
        GButton_923["bg"] = "#6fcbf2"
        ft = tkFont.Font(family='Times',size=10)
        GButton_923["font"] = ft
        GButton_923["fg"] = "#000000"
        GButton_923["justify"] = "center"
        GButton_923["text"] = "ТЪРСЕНЕ ПО ЦЕНА НА СТОКА"
        GButton_923["relief"] = "raised"
        GButton_923.place(x=80,y=230,width=311,height=79)
        GButton_923["command"] = self.GButton_923_command

        GButton_975=tk.Button(root)
        GButton_975["activebackground"] = "#309eb4"
        GButton_975["activeforeground"] = "#ffffff"
        GButton_975["bg"] = "#4adee3"
        ft = tkFont.Font(family='Times',size=10)
        GButton_975["font"] = ft
        GButton_975["fg"] = "#000000"
        GButton_975["justify"] = "center"
        GButton_975["text"] = "ПОКАЖИ ВСИЧКИ ПРОДАЖБИ"
        GButton_975["relief"] = "raised"
        GButton_975.place(x=400,y=270,width=339,height=142)
        GButton_975["command"] = self.GButton_975_command

        GButton_992=tk.Button(root)
        GButton_992["activebackground"] = "#d4dbea"
        GButton_992["activeforeground"] = "#000000"
        GButton_992["bg"] = "#455981"
        ft = tkFont.Font(family='Times',size=10)
        GButton_992["font"] = ft
        GButton_992["fg"] = "#000000"
        GButton_992["justify"] = "center"
        GButton_992["text"] = "СТОКИ ПО ОБОРОТ"
        GButton_992["relief"] = "raised"
        GButton_992.place(x=400,y=150,width=339,height=104)
        GButton_992["command"] = self.GButton_992_command

        GButton_753=tk.Button(root)
        GButton_753["activebackground"] = "#172f2e"
        GButton_753["activeforeground"] = "#ffffff"
        GButton_753["bg"] = "#bceee4"
        ft = tkFont.Font(family='Times',size=10)
        GButton_753["font"] = ft
        GButton_753["fg"] = "#000000"
        GButton_753["justify"] = "center"
        GButton_753["text"] = "ВИЖ ПРОДАЖБИ ПО ДАТА"
        GButton_753["relief"] = "raised"
        GButton_753.place(x=400,y=420,width=339,height=97)
        GButton_753["command"] = self.GButton_753_command

        GButton_283=tk.Button(root)
        GButton_283["activebackground"] = "#e8e9f8"
        GButton_283["activeforeground"] = "#000000"
        GButton_283["bg"] = "#405188"
        ft = tkFont.Font(family='Times',size=10)
        GButton_283["font"] = ft
        GButton_283["fg"] = "#000000"
        GButton_283["justify"] = "center"
        GButton_283["text"] = "ЗАПАЗИ ДАННИ ЗА ОБОРОТ"
        GButton_283["relief"] = "raised"
        GButton_283.place(x=80,y=450,width=311,height=65)
        GButton_283["command"] = self.GButton_283_command
      
    #добавяне на данни във файл
    def GButton_321_command(self):
        import add
        add.add_show(csv_file3)

    #търсене по име
    def GButton_300_command(self):
         import name_search
         file1=name_search.read1(csv_file1)
         file2=name_search.read1(csv_file2)
         file3=name_search.read1(csv_file3)
         name_search.show_csv_data(file1,file2,file3)
    

    #търсене по цена
    def GButton_923_command(self):
        import filtar_suma
        file1=filtar_suma.read1(csv_file1)
        file2=filtar_suma.read1(csv_file2)
        file3=filtar_suma.read1(csv_file3)
        filtar_suma.show_csv_data(file1,file2,file3)

    #покажи всичко
    def GButton_975_command(self):
        show_merged_data(self.merged_data)

    #стоки по оборот
    def GButton_992_command(self):
        show_merged_data1(self.merged_data)


    #продажби по дата
    def GButton_753_command(self):
        show_data_by_date(self.merged_data)

   

   #запис в текстов файл
    def GButton_283_command(self):
     
     # Избор на местоположение и име на файла
     filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv")]
        )

     if filepath:
        # Създаване на текстовия файл и отваряне за запис
        with open(filepath, "w") as file:
            writer = csv.writer(file, delimiter="\t")

            # Записване на заглавията на колоните
            writer.writerow(["Група", "Оборот"])
            writer.writerow(['====================='])

            # Инициализиране на променлива за общия оборот
            total_oborot = 0

            # Създаване на речник за съхранение на оборота по групи
            group_oborot = {}

            # запис на обединените данни
            for row in self.merged_data:
                code = row[0]
                vid = row[6]
                name = row[1]
                quantity = int(row[3])
                price = float(row[2])
                total = quantity * price

                # Проверка дали групата вече съществува в речника group_oborot
                if vid in group_oborot:
                    # Ако групата съществува, да се добави оборота към съществуващата стойност
                    group_oborot[vid] += total
                else:
                    # Ако групата не съществува, създава нова стойност за групата
                    group_oborot[vid] = total

                # Добавете оборота към общия оборот
                total_oborot += total

            # Записване на данните за оборота по групи в текстовия файл
            for vid, oborot in group_oborot.items():
                writer.writerow([vid, oborot])

             # Записване на общия оборот в текстовия файл
            writer.writerow(['====================='])
            writer.writerow(["Общо", total_oborot,"лв."])
            os.startfile(filepath)  # извеждане на текстовия файл след записването

         # Съобщение за успешно създаване на текстовия файл
     messagebox.showinfo("Готово", "Текстовият файл е създаден успешно.")
       
     

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
