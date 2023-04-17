import tkinter as tk
import tkinter.filedialog as fd
import pickle
import docx


class ClassifyWindow(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)
        self.title('Режим предсказания модели')
        self.geometry('600x400+200+200')

        with open('model_data/staking-model.pkl', 'rb') as file:
            self._model = pickle.load(file)

        self.create_button()

    def create_button(self):
        btn_file = tk.Button(self, text="Выбрать файл",
                             command=self.choose_files)
        btn_file.pack(padx=60, pady=10)

    def choose_files(self):
        filetypes = (("Текстовый файл", "*.txt"),
                     ("Документ Word", "*.docx"),
                     ("Изображение", "*.jpg *.gif *.png"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            prediction = self.get_prediction(filename)
            label = tk.Label(
                self,
                text=f'Для данного файла предсказанный класс - "{prediction}"'
            )
            label.pack(pady=20)

    def get_prediction(self, path):
        if path.split('.')[1] == 'txt':
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
        if path.split('.')[1] == 'docx':
            text = self.get_text_from_docx(path)

        prediction = self._model.predict([text])
        prediction = prediction[0][0]
        return prediction


    @staticmethod
    def get_text_from_docx(path):
        doc = docx.Document(path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)

    def grab_focus(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()


