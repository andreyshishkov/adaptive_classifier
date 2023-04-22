import tkinter as tk
import tkinter.filedialog as fd
from windows.help_menu import HelpMenu
from finetune_model.fine_tune import fine_tune
from utils.prediction import get_prediction


class MenuWindow(tk.Tk):

    def __init__(self, width=1200, height=700):
        super().__init__()
        self.geometry(f'{width}x{height}')
        self.title('Программа интеллектуальной адаптивной классификации неструктурируемых текстовых данных по степени конфиденциальности')
        self.image = tk.PhotoImage(file='kvvu.png')
        self._bg = tk.Label(self, image=self.image)
        self._bg.place(x=0, y=0, relwidth=1, relheight=1)

        self._main_menu = self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self)
        self.create_train_menu(menu)
        self.create_classify_menu(menu)
        menu.add_command(
            label='Справка',
            command=self.create_helper
        )

        self.config(menu=menu)

        return menu

    def create_train_menu(self, menu):
        train_menu = tk.Menu(menu, tearoff=0)
        train_menu.add_command(
            label='Выбрать конфигурационный файл',
            command=self.mode_train
        )
        menu.add_cascade(
            label='Обучение',
            menu=train_menu
        )

    def create_classify_menu(self, menu):
        cls_menu = tk.Menu(menu, tearoff=0)
        cls_menu.add_command(
            label='Выбрать документ классификации',
            command=self.mode_classify
        )
        menu.add_cascade(
            label='Классификация',
            menu=cls_menu
        )

    def create_helper(self):
        helper = HelpMenu(self)
        helper.grab_focus()

    def mode_train(self):
        filetypes = (("Текстовый файл", "*.txt"),
                     ("Любой", "*"))
        filename = self.choose_files(filetypes)
        if filename:
            f1, length, step = self.__get_params(filename)
            train_warn_window = self.__create_train_warning(f1, length, step)
            train_warn_window.grab_set()
            train_warn_window.focus_set()
            train_warn_window.wait_window()

            result_window = self.create_train_window(f1, length, step)
            result_window.focus_set()
            result_window.grab_set()
            result_window.wait_window()

    def __create_train_warning(self, f1, length, step):
        train_window = tk.Toplevel(self)
        train_window.title('Режим обучения')
        start_label = tk.Label(
            train_window,
            text='Сейчас начнется обучение. Пожалуйста, подождите, это может занять время. \nЧтобы начать обучение закройте текущее окно и дождитесь пока не появится окно с результатом'
        )
        start_label.pack(pady=20)
        return train_window

    def create_train_window(self, f1, length, step):
        train_window = tk.Toplevel(self)
        train_window.title('Режим обучения')
        train_window.geometry('600x200+200+200')

        final_score, final_len = fine_tune(min_f1=f1, start_max_len=length, step=step)

        final_label = tk.Label(
            train_window,
            text=f'F1 - {final_score}; Мин.длина - {final_len}'
        )
        final_label.pack(pady=20)

        return train_window

    @staticmethod
    def __get_params(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        text = text.strip()
        params = text.split('\n')
        f1, length, step = [param.split('==')[1] for param in params]

        f1 = f1.replace(',', '.')
        f1 = float(f1)
        length = int(length)
        step = int(step)

        return f1, length, step

    def mode_classify(self):
        filetypes = (("Текстовый файл", "*.txt"),
                     ("Документ Word", "*.docx"),
                     ("Любой", "*"))
        filename = self.choose_files(filetypes)
        if filename:
            prediction = get_prediction(filename)
            result_window = self.create_prediction_window(prediction)
            result_window.geometry('500x200+200+200')

            result_window.focus_set()
            result_window.grab_set()
            result_window.wait_window()

    def create_prediction_window(self, prediction):
        result_window = tk.Toplevel(self)

        label = tk.Label(
            result_window,
            text=f'Для данного файла предсказанный класс - "{prediction}"'
        )
        label.pack(pady=20)
        return result_window

    @staticmethod
    def choose_files(filetypes):
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        return filename

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    window  = MenuWindow()
    window.run()
