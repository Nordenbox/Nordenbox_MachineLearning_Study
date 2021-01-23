import matplotlib.pyplot as plt
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels)= mnist.load_data()
print(train_images.ndim)
print(train_labels.ndim)
print(train_images.shape)
print(train_images.dtype)


my_slice = train_images[10,14:,14:]

plt.imshow(my_slice,cmap= plt.cm.binary)
plt.show()