import tkinter as tk
from windows.train_model_window import TrainModelWindow
from windows.predict_window import ClassifyWindow


class MainWindow(tk.Tk):

    def __init__(self, width=1200, height=700):
        super().__init__()
        self.geometry(f'{width}x{height}')
        self.title('Программа интеллектуальной адаптивной классификации неструктурируемых текстовых данных по степени конфиденциальности')
        self.image = tk.PhotoImage(file='kvvu.png')
        self._bg = tk.Label(self, image=self.image)
        self._bg.place(x=0, y=0, relwidth=1, relheight=1)

        self._create_buttons()

    def _create_buttons(self):
        # button of mode "create"
        self.make_criteria_btn = tk.Button(
            self,
            text='Обучить модель',
            width=40,
            height=5,
            background='green',
            font='Helvetica 12 bold',
            command=self.create_window_mode_create
        )
        self.make_criteria_btn.pack(side=tk.LEFT, padx=15,)

        # button of mode "choose"
        self.choose_criteria_btn = tk.Button(
            self,
            text='Осуществить классификацию',
            width=40,
            height=5,
            bg='green',
            font='Helvetica 12 bold',
            command=self.create_window_mode_choose
        )
        self.choose_criteria_btn.pack(side=tk.RIGHT, padx=15)

    def create_window_mode_create(self):
        mode_create = TrainModelWindow(self)
        mode_create.grab_focus()

    def create_window_mode_choose(self):
        choose_window = ClassifyWindow(self)
        choose_window.grab_focus()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    window = MainWindow()
    window.run()
