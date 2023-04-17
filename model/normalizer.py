from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer


class Normalizer(BaseEstimator, TransformerMixin):

    def __init__(self):
        self._punct =  '!"#$%&()*\+,-\./:;<=>?@\[\]^_`{|}~„“«»†*\—/\-‘’'
        self._stop_words = stopwords.words('russian')
        self._morph = MorphAnalyzer()

    def fit(self, *args):
        return self

    def transform(self, texts):
        for text in texts:
            yield self.normalize(text)

    def normalize(self, text):
        text = text.replace('\xa0', ' ')
        text = text.replace('\n', ' ')
        tokens = word_tokenize(text)
        tokens = [word.strip(self._punct) for word in tokens]
        tokens = [word.lower() for word in tokens if word != '']
        tokens = [word for word in tokens if word not in self._stop_words]
        tokens = [self._morph.parse(word)[0].normal_form for word in tokens]

        preprocessed_text = ' '.join(tokens)
        return preprocessed_text


