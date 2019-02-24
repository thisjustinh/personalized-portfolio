# import KMeans
# import keras
import pandas as pd
# from keras.models import Sequential
# from keras.layers import Dense, Activation, LSTM
from sklearn.cluster import KMeans
import numpy as np

X = np.array
num_clusters = 5


def cluster(df):
    array = np.array(df.fillna(0))
    clustering = KMeans(n_clusters=20, verbose=1).fit(array)
    df = pd.DataFrame(array, index=df.index, columns=df.columns)

    df['cluster'] = clustering.labels_
    df.to_csv('cluster.csv')

    return df

    # model = Sequential()
    #
    # model.add(LSTM(32, return_sequences=True, input_shape=(8, 16)))
    # model.add(LSTM(32, return_sequences=True))
    # model.add(LSTM(32))
    #
    # model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['accuracy'])


# def get_stocks():
#     bestStocks = []
#
#     for i in range(num_clusters):
#
#         list = result.index[result['Cluster'] == i].tolist()
#
#         x_train = pd.DataFrame
#         for stock in list:
#             x_train.append(historical.loc[stock])
#
#         model.fit(x_train, target, batch_size=60, epochs=5, validation_data=())
#
#         current = x_train.loc[:, -60:-1]
#
#         future = model.predict(current)
#         k = future.idmax
#         bestStocks.append(k)
#     return bestStocks


if __name__ == '__main__':
    df = pd.DataFrame.from_csv('data.csv')

    cluster(df)





