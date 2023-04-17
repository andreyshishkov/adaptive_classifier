from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, BatchNormalization
import keras
from keras.wrappers.scikit_learn import KerasClassifier


def create_model():
    model = Sequential()
    model.add(Dense(50,activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Dense(50,activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(1,activation='sigmoid'))

    model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])

    return model


def get_wrapped_network():
    return KerasClassifier(build_fn=create_model, verbose=0)
