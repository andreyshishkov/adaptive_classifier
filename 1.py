from model.stacking import StackClassifier
import pandas as pd
import pickle

df = pd.read_csv('training_dataset/training_dataset.csv')
X = df['text']
y = df['class']
print(y.value_counts())

model = StackClassifier()
model.fit(X.values, y.values)
model.save()
# with open('model_data/staking-model.pkl', 'rb') as file:
#     model = pickle.load(file)
pred = model.predict([X.values[0]])
# pred = [i[0] for i in pred]
print(pred)