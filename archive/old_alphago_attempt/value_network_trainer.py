import pickle
import numpy as np

from keras.models import Sequential,load_model
from keras.layers import Dense, Flatten, Dropout
from keras.layers.advanced_activations import LeakyReLU
from keras.callbacks import EarlyStopping,ModelCheckpoint

from keras.layers.convolutional import Conv2D

with open('./data/train.pickle', 'rb') as train:
    train_x, train_Y = pickle.load(train)
with open('./data/test.pickle', 'rb') as train:
    test_x, test_Y = pickle.load(train)

def vectorize(y):
    ''' Converts a classification into the desired neural net output format '''
    a = np.zeros(3)
    a[y] = 1
    return a

# reformat input for convolutional neural net (input needs to be need to be (# examples, 6, 7))
train_x = np.array(train_x).reshape(len(train_x), 6, 7, 1)
train_Y = np.array([vectorize(y) for y in train_Y])

test_x = np.array(test_x).reshape(len(test_x), 6, 7, 1)
test_Y = np.array([vectorize(y) for y in test_Y])

nb_filters = 128

input_shape = (6, 7, 1)

model = Sequential([Conv2D(nb_filters, kernel_size=(4,4), padding='valid', input_shape = input_shape, data_format="channels_last"),
                   LeakyReLU(),
                   #Dropout(0.25),
                   Conv2D(nb_filters, kernel_size=(2,2), padding='valid', data_format="channels_last"),
                   LeakyReLU(),
                   #Dropout(0.25),
                   Flatten(),
                   Dense(256),
                   LeakyReLU(),
                   #Dropout(0.25),
                   Dense(64),
                   LeakyReLU(),
                   Dense(3, activation='softmax')])

model.compile('rmsprop','categorical_crossentropy', metrics=['accuracy'])

model_name = 'model.h5'

model.fit(train_x, train_Y, validation_split=0.1,
          callbacks=[EarlyStopping(patience=10),
                     ModelCheckpoint(model_name,verbose=1,save_best_only=True)],
          batch_size=64, epochs=200)

model = load_model(model_name)
# load previous model

print('test accuracy:', model.evaluate(test_x, test_Y, verbose=0)[1])
