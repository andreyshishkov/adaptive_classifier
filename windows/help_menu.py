import tkinter as tk


class HelpMenu(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Справка')
        self.geometry('550x300+200+200')

        self.create_label()

    def create_label(self):
        with open('app_data/help.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        label = tk.Label(
            self,
            text=text,
            justify=tk.LEFT
        )
        label.pack(pady=10, )

    def grab_focus(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()