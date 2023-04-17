from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score
import numpy as np


def check_score(model, texts, targets):
    texts = np.array(texts)
    targets = np.array(targets)
    skf = StratifiedKFold(n_splits=7)
    scores = []
    for train_index, val_index in skf.split(texts, targets):
        X_train, X_val = texts[train_index], texts[val_index]
        y_train, y_val = targets[train_index], targets[val_index]

        model.fit(X_train, y_train)

        preds = model.predict(X_val)
        scores.append(
            f1_score(y_val, preds)
        )
    print(f'Cur. f1-score: {np.mean(scores)}')
    return np.mean(scores)
