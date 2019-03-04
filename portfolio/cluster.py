# import KMeans
# import keras
import pandas as pd
# from keras.models import Sequential
# from keras.layers import Dense, Activation, LSTM, Conv2D,RNN
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
# model.add(LSTM(32, return_sequences=True, input_shape=(60, 5)))
# model.add(LSTM(512, return_sequences=True))
# model.add(LSTM(64))
# model.add(Dense(5))
#
# model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['accuracy'])
#
# def get_stocks(df_c, df_h):
#     bestStocks = []
#     print(df_c)
#     for i in range(num_clusters):
#         my_list = df_c.index[df_c['cluster'] == i].tolist()
#         tickers = []
#         for i in my_list:
#              tickers.append(df_c.loc[i, 'Unnamed: 0'])
#         #import pdb; pdb.set_trace()
#         print(tickers)
#         ##print(df_c.index[list[0]])
#         x_train = pd.DataFrame()
#         y_train = pd.DataFrame()
#         for stock in my_list:
#             x_train[stock] = df_h
#             y_train = pd.append(df_h.iloc[stock, :])
#
#         print(x_train)
#         x_train = np.array(x_train)
#         x_train = x_train.reshape(1,60,5)
#
#         y_train = np.array(y_train)
#         y_train.reshape(1,60,5)
#
#         print(x_train)
#         print(y_train)
#         model.fit(x_train, y_train, batch_size=60, epochs=5, validation_data=())
#
#         current = x_train.loc[:, -60:-1]
#
#         future = model.predict(current)
#         k = future.idmax
#         bestStocks.append(k)
#     return bestStocks


def recommendations(risk, capital, time, df1, df2):
    kmeans = pd.read_csv('C:/Users/sidiy/workspace/portfolio_api/portfolio/static/cluster.csv')
    hist = pd.read_csv('C:/Users/sidiy/workspace/portfolio_api/portfolio/static/historical.csv')

    if capital > '10000':
        n = kmeans.loc[kmeans['P/E'].idxmax(), 'cluster']
        my_list = kmeans.index[kmeans['cluster'] == n].tolist()
        tickers = []
        for i in my_list:
            t = kmeans.loc[i, 'Unnamed: 0']
            tickers.append({'symbol': t,
                            'price': hist[t].iloc[-1]})
        return tickers
    elif risk > '3':
        n = kmeans.loc[kmeans['Beta'].idxmax(), 'cluster']
        my_list = kmeans.index[kmeans['cluster'] == n].tolist()
        tickers = []
        for i in my_list:
            t = kmeans.loc[i, 'Unnamed: 0']
            tickers.append({'symbol': t,
                            'price': hist[t].iloc[-1]})
        return tickers
    elif time > '5':
        n = kmeans.loc[kmeans['Div Yield'].idxmax(), 'cluster']
        my_list = kmeans.index[kmeans['cluster'] == n].tolist()
        tickers = []
        for i in my_list:
            t = kmeans.loc[i, 'Unnamed: 0']
            tickers.append({'symbol': t,
                            'price': hist[t].iloc[-1]})
        return tickers
    else:
        n = kmeans.loc[kmeans['EPS'].idxmax(), 'cluster']
        my_list = kmeans.index[kmeans['cluster'] == n].tolist()
        tickers = []
        for i in my_list:
            t = kmeans.loc[i, 'Unnamed: 0']
            tickers.append({'symbol': t,
                            'price': hist[t].iloc[-1]})
        return tickers
