import numpy as np
import pandas as pd
from os.path import isfile
from progressbar import ProgressBar
import pickle

def preprocess():
    pbar = ProgressBar()

    with open('./data/connect-4.data') as f:
        data = [line.split(',') for line in f.readlines()]

    dataset = pd.DataFrame(data=data)

    dataset.iloc[:,-1] = [element.strip('\n') for element in dataset.iloc[:,-1]]

    dataset = dataset.replace(['b','x','o'],[0,1,-1])
    dataset = dataset.replace(['win','loss','draw'],[2,0,1])
    # x is the first player. The outcome is for the first player

    num_examples = len(dataset)

    def generator(row):
        for element in row:
            yield element

    x = []
    Y = []

    for row_num in pbar(range(len(dataset))):
        board = np.empty(shape=(6, 7), dtype=int)
        row_generator = generator(dataset.iloc[row_num,:-1])
        for c in range(7):
            for r in reversed(range(6)):
                board[r,c] = next(row_generator)
        x.append(board)
        Y.append(dataset.iloc[row_num,-1])

    x_train = x[:int(num_examples*0.9)]
    Y_train = Y[:int(num_examples*0.9)]

    x_test = x[int(num_examples*0.9):]
    Y_test = Y[int(num_examples*0.9):]

    with open('./data/train.pickle', 'wb') as output:
        pickle.dump((x_train, Y_train), output, protocol=pickle.HIGHEST_PROTOCOL)
    with open('./data/test.pickle', 'wb') as output:
        pickle.dump((x_test, Y_test), output, protocol=pickle.HIGHEST_PROTOCOL)

    print('Data preprocessing complete. Pickle files created.')

if not isfile('./data/train.pickle') or not isfile('./data/test.pickle'):
    preprocess()
else:
    print('Data already preprocessed.')
