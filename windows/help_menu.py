import tkinter as tk
from tkinter import ttk


class HelpMenu(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Справка')
        self.geometry('680x350+200+200')

        self._info = self._instruction = None

        self._notebook = ttk.Notebook(self)
        self.create_tabs()
        self.create_labels()

    def create_tabs(self):
        self._instruction = ttk.Frame(self._notebook)
        self._info = ttk.Frame(self._notebook)

        self._notebook.add(self._instruction, text='Инструкция')
        self._notebook.add(self._info, text='О программе')
        self._notebook.pack(expand=1, fill="both")

    def create_labels(self):
        with open('app_data/instruction.txt', 'r', encoding='utf-8') as file:
            instruction = file.read()
        ttk.Label(
            self._instruction,
            text=instruction,
            justify=tk.LEFT
        ).pack(pady=10)

        with open('app_data/info.txt', 'r', encoding='utf-8') as file:
            info = file.read()
        ttk.Label(
            self._info,
            text=info,
            justify=tk.LEFT
        ).pack(pady=10)

    def grab_focus(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()