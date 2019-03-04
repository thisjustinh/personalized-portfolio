#import KMeans 
#import keras 
from keras.models import Sequential 
from keras.layers import Dense, Activation, LSTM 
from sklearn.cluster import AgglomerativeClustering
import numpy as np 

X = np.array; 

def cluster():

    clustering = AgglomerativeClustering().fit(X)
    clustering AgglomerativeClustering(affinity='cosine'; compute_full_tree='auto, connectivity=None, linkage='complete',memory=None, n_clusters=5, pooling_func='deprecated')

    final = pd.DataFrame(clustering.labels_)

    result = pd.concat(X,final,axis=1, join='outer')

model = Sequential()

model.add(LSTM(32, return_sequences=True, input_shape = (timesteps, data_dim)))
model.add(LSTM(32, return_sequences =True))
model.add(LSTM(32))

model.compile(loss = 'mean_squared_error', optimizer = 'rmsprop', metrics = ['accuracy'])

def getStocks():
    bestStocks = []

    for i in range(num_clusters):

        list = result.index[result['Cluster'] == i].tolist()

        x_train = pd.DataFrame
        for stock in list:
            x_train.append(historical.loc[stock])

        model.fit(x_train, target, batch_size= 60, epochs = 5, validation_data =())

        current = x_train.loc[:,0-60,:]

        future = model.predict(current)
        k = future.idmax
        bestStocks.append(k)
    return bestStocks

def getOptions(string stock):

    





