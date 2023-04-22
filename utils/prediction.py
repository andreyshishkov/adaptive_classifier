import pickle
import docx


def get_prediction(path):
    with open('model_data/staking-model.pkl', 'rb') as file:
        model = pickle.load(file)
    if path.split('.')[1] == 'txt':
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
    if path.split('.')[1] == 'docx':
        text = get_text_from_docx(path)

    prediction = model.predict([text])
    prediction = prediction[0][0]
    return prediction


def get_text_from_docx(path):
    doc = docx.Document(path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)
