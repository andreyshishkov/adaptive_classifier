import pandas as pd
from model.stacking import StackClassifier
from finetune_model.reduce_texts import reduce_texts
from finetune_model.scoring import check_score


def fine_tune(min_f1, start_max_len, step=5):
    data = pd.read_csv('training_dataset/training_dataset.csv')
    texts = data['text'].values
    targets = data['class'].values

    stacking = StackClassifier()
    text_len = start_max_len
    prev_score = None
    while True:
        X = reduce_texts(texts, text_len)
        score = check_score(model=stacking, texts=X, targets=targets)

        if prev_score is None:
            prev_score = score

        if score >= min_f1:
            print(f'Metrics for  step: f1-score - {score}, text-length - {text_len}')
            text_len -= step
            prev_score = score
            continue
        else:
            final_len = text_len + step
            print(f'Final: {prev_score}, {final_len}')
            X = reduce_texts(texts, final_len)
            stacking.fit(X, targets)
            stacking.save()

            return prev_score, final_len
