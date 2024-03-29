import tkinter as tk
from tkinter import messagebox

from guii import App
from data_utils import merge_data, merge_group_data

def exit_app():
    if messagebox.askokcancel("Изход", "Сигурни ли сте, че искате да излезете?"):
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()

    pr_file = "prodajbi.csv"
    st_file = "stoki.csv"
    vidove_file = "vidove.csv"

    merged_data = merge_data(pr_file, st_file)
    merged_data_with_group = merge_group_data(merged_data, vidove_file)

    # Добавете меню към главния прозорец
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Изход", command=exit_app)
    menubar.add_cascade(label="Файл", menu=file_menu)

    root.config(menu=menubar)
    app_gui = App(root, merged_data_with_group)
    root.mainloop()
