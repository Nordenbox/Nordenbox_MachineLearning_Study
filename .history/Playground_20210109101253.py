from keras.datasets import mnist
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

(train_images, train_labels), (test_images, test_labels)= mnist.load_data()
print(train_images.ndim)

