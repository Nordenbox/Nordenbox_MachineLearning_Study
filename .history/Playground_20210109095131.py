from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels)= minist.load_data()
print(train_images.ndim)

