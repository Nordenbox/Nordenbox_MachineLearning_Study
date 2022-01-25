from keras import models
from keras import layers
network = models.Sequential()
network.add(layers.Dense(512,activation='lelu',input_shape=(28*28)))
network.add(layers.Dense(10,activation='softmax'))
print(type(network))