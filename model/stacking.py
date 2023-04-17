from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.base import BaseEstimator
from mlxtend.classifier import StackingClassifier
from model.normalizer import Normalizer
from model.metaclassifier import get_wrapped_network
import pickle


class StackClassifier(BaseEstimator):

    def __init__(self, th=0.37):
        self._th = 0.37

        self._passive_aggressive = Pipeline([
            ('vect', HashingVectorizer()),
            ('cls', PassiveAggressiveClassifier())
        ])
        self._svc = Pipeline([
            ('vect', HashingVectorizer()),
            ('cls', SVC())
        ])
        self._knn = Pipeline(
            [
                ('vect', HashingVectorizer()),
                ('cls', KNeighborsClassifier(n_neighbors=7))
            ]
        )
        self._sgd = Pipeline(
            [
                ('vect', HashingVectorizer()),
                ('cls', SGDClassifier(loss='log'))
            ]
        )

        self._classifiers = [
            self._sgd,
            self._knn,
            self._svc,
            self._passive_aggressive
        ]

        self._metaclassifier = get_wrapped_network()

        self._stacking = StackingClassifier(
            classifiers=self._classifiers,
            meta_classifier=self._metaclassifier
        )

        # self._model = Pipeline([
        #     ('normalizer', Normalizer()),
        #     ('cls', self._stacking)
        # ])

    def fit(self, texts, targets):
        self._stacking.fit(texts, targets)
        return self

    def predict(self, texts):
        predictions = self._stacking.predict(texts)
        predictions = [pred[0] for pred in predictions]
        return predictions

    def save(self):
        with open('model_data/staking-model.pkl', 'wb') as file:
            pickle.dump(self._stacking, file)
