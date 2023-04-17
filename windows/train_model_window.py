import tkinter as tk
from finetune_model.fine_tune import fine_tune
import time


class TrainModelWindow(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)
        self.title('Режим адаптивного обучения модели')
        self.geometry('600x400+200+200')

        self._step = self._f1 = self._start_len = None
        self._warn_label = None
        self._result_label = None

        self.create_f1_entry()
        self.create_start_len_entry()
        self.create_step_entry()
        self.create_button()

    def create_f1_entry(self):
        field = tk.Frame(self)
        label = tk.Label(
            field,
            text='Введите пороговое значение F1 меры:',
            width=40
        )
        label.grid(row=0, column=0)
        self._f1 = tk.Entry(
            field,
            width=40
        )
        self._f1.grid(row=1, column=0)

        field.pack(pady=20)

    def create_start_len_entry(self):
        field = tk.Frame(self)
        label = tk.Label(
            field,
            text='Введите начальное значение,\nограничивающее количество токенов в примерах:',
        )
        label.grid(row=0, column=0)
        self._start_len = tk.Entry(
            field,
            width=40
        )
        self._start_len.grid(row=1, column=0)

        field.pack(pady=20)

    def create_step_entry(self):
        field = tk.Frame(self)
        label = tk.Label(
            field,
            text='Введите значение шага адаптации:',
            width=40
        )
        label.grid(row=0, column=0)
        self._step = tk.Entry(
            field,
            width=40
        )
        self._step.grid(row=1, column=0)

        field.pack(pady=20)

    def create_button(self):
        button = tk.Button(
            self,
            text='Обучить модель',
            command=self.train_model
        )
        button.pack(pady=25)

    def train_model(self):
        if self._warn_label is not None:
            self._warn_label.destroy()
            self._warn_label = None

        if self._result_label is not None:
            self._result_label.destroy()
            self._result_label = None

        f1 = float(self._f1.get().replace(',', '.'))
        step = int(self._step.get())
        start_len = int(self._start_len.get())

        self._warn_label = tk.Label(
            self,
            text='Пожалуйста подождите, начался процесс обучения модели, это может занять время...'
        )
        self._warn_label.pack(pady=5)
        time.sleep(2)

        final_score, final_min_len = fine_tune(f1, start_len, step)
        final_score = round(final_score, 4)
        # final_score = 0.95
        # final_min_len = 60

        self._result_label = tk.Label(
            self,
            text=f'Результат обучения: F1 - {final_score}; оптимальн.макс ддина - {final_min_len}'
        )
        self._result_label.pack(pady=10)

    def grab_focus(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()
