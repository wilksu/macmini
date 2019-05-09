import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import gzip
from pylab import mpl
from PIL import Image

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
# print(tf.__version__)

def load_data(data_folder):
    files = [
        'train-labels-idx1-ubyte.gz','train-images-idx3-ubyte.gz', 
        't10k-labels-idx1-ubyte.gz','t10k-images-idx3-ubyte.gz'
    ]

    paths = []
    for fname in files:
        paths.append(os.path.join(data_folder,fname))
    # print(paths)

    with gzip.open(paths[0], 'rb') as lbpath:
        y_train = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(paths[1], 'rb') as imgpath:
        x_train = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(y_train), 28, 28)

    with gzip.open(paths[2], 'rb') as lbpath:
        y_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(paths[3], 'rb') as imgpath:
        x_test = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(y_test), 28, 28)

    return (x_train, y_train), (x_test, y_test)

# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

class_names = ['t恤/前','裤子','套衫','连衣裙','外套','凉鞋','衬衫','运动鞋','手袋','短靴']

(train_images, train_labels), (test_images, test_labels) = load_data('fashion')
train_images = train_images / 255.0
test_images = test_images / 255.0

def showsample():
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        # plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

def train():
    model=keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128,activation=tf.nn.relu),
        keras.layers.Dense(10,activation=tf.nn.softmax)
    ])
    model.compile(optimizer=tf.train.AdamOptimizer(),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=5)
    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver.save(sess, "Model/model.ckpt")
    img = Image.open('t1.jpg')
    img = img.resize((28, 28),Image.ANTIALIAS) #resize image with high-quality
    # r,g,b=img.split()
    im = np.asarray(img)
    print(im)
    predictions = model.predict(train_images[10])
    print(predictions)
    # test_loss, test_acc = model.evaluate(test_images, test_labels)
    # print('Test accuracy:', test_acc)

def resize():
    img = Image.open('t1.jpg')
    img = img.resize((28, 28),Image.ANTIALIAS) #resize image with high-quality
    r,g,b=img.split()
    im = np.asarray(r)
    print(im)

if __name__ == "__main__":
    # showsample()
    train()
    # resize()




