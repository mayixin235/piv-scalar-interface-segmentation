import tensorflow.keras.callbacks
from keras.preprocessing.image import array_to_img
import pydot
from PIL import ImageFont
from tensorflow.keras.utils import plot_model
from keras.layers import Input
from keras.optimizers import *
from keras.callbacks import ModelCheckpoint, History
from tensorflow.keras.callbacks import ModelCheckpoint
import data
from tensorflow.keras.layers import Input
import visualkeras
from keras_sequential_ascii import keras2ascii
from openpyxl import Workbook
import pandas as pd


class myUnet(object):

    def __init__(self, img_rows=256, img_cols=256):
        self.img_rows = img_rows
        self.img_cols = img_cols

    def load_data(self):  # method to load data
        mydata = data.dataProcess(self.img_rows, self.img_cols)
        imgs_train, imgs_mask_train = mydata.load_train_data()
        imgs_val, imgs_mask_val = mydata.load_val_data()
        imgs_test, imgs_mask_test= mydata.load_test_data()
        return imgs_train, imgs_mask_train, imgs_val, imgs_mask_val, imgs_test, imgs_mask_test

    def get_unet(self):  # method to define the neural network
        inputs = Input((self.img_rows, self.img_cols, 3))

        conv1 = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same', kernel_initializer='he_normal')(inputs)
        print("conv1 shape:", conv1.shape)
        conv1 = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv1)
        print("conv1 shape:", conv1.shape)
        pool1 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv1)
        print("pool1 shape:", pool1.shape)

        conv2 = tf.keras.layers.Conv2D(128, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool1)
        print("conv2 shape:", conv2.shape)
        conv2 = tf.keras.layers.Conv2D(128, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv2)
        print("conv2 shape:", conv2.shape)
        pool2 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv2)
        print("pool2 shape:", pool2.shape)

        conv3 = tf.keras.layers.Conv2D(256, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool2)
        print("conv3 shape:", conv3.shape)
        conv3 = tf.keras.layers.Conv2D(256, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv3)
        print("conv3 shape:", conv3.shape)
        drop3 = tf.keras.layers.Dropout(0.5)(conv3)
        pool3 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop3)
        print("pool3 shape:", pool3.shape)

        conv4 = tf.keras.layers.Conv2D(512, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool3)
        conv4 = tf.keras.layers.Conv2D(512, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv4)
        drop4 = tf.keras.layers.Dropout(0.5)(conv4)
        pool4 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop4)

        conv5 = tf.keras.layers.Conv2D(1024, 3, activation='relu', padding='same', kernel_initializer='he_normal')(
            pool4)
        conv5 = tf.keras.layers.Conv2D(1024, 3, activation='relu', padding='same', kernel_initializer='he_normal')(
            conv5)
        drop5 = tf.keras.layers.Dropout(0.5)(conv5)

        up6 = tf.keras.layers.Conv2D(512, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            tf.keras.layers.UpSampling2D(size=(2, 2))(drop5))
        merge6 = tf.keras.layers.concatenate([drop4, up6], axis=3)
        conv6 = tf.keras.layers.Conv2D(512, 3, activation='relu', padding='same', kernel_initializer='he_normal')(
            merge6)
        conv6 = tf.keras.layers.Conv2D(512, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv6)

        up7 = tf.keras.layers.Conv2D(256, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            tf.keras.layers.UpSampling2D(size=(2, 2))(conv6))
        merge7 = tf.keras.layers.concatenate([conv3, up7], axis=3)
        conv7 = tf.keras.layers.Conv2D(256, 3, activation='relu', padding='same', kernel_initializer='he_normal')(
            merge7)
        conv7 = tf.keras.layers.Conv2D(256, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv7)

        up8 = tf.keras.layers.Conv2D(128, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            tf.keras.layers.UpSampling2D(size=(2, 2))(conv7))
        merge8 = tf.keras.layers.concatenate([conv2, up8], axis=3)
        conv8 = tf.keras.layers.Conv2D(128, 3, activation='relu', padding='same', kernel_initializer='he_normal')(
            merge8)
        conv8 = tf.keras.layers.Conv2D(128, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv8)

        up9 = tf.keras.layers.Conv2D(64, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            tf.keras.layers.UpSampling2D(size=(2, 2))(conv8))
        merge9 = tf.keras.layers.concatenate([conv1, up9], axis=3)
        conv9 = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge9)
        conv9 = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
        conv9 = tf.keras.layers.Conv2D(2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
        conv10 = tf.keras.layers.Conv2D(1, 1, activation='sigmoid')(conv9)

        model = tf.keras.Model(inputs=inputs, outputs=conv10)

        # select hyperparameters: optimiser, learning rate and loss function
        model.compile(optimizer=tf.keras.optimizers.Adam(lr=1e-4), loss='binary_crossentropy', metrics=['accuracy'])

        return model

    def train(self):  # method to train the neural network
        print("loading data")
        imgs_train, imgs_mask_train, imgs_val, imgs_mask_val, imgs_test, imgs_mask_test = self.load_data()
        print("loading data done")
        model = self.get_unet()
        print("got unet")

        # load weights from the previous case if there is, if not comment this line
        model.load_weights("C:/Users//Desktop/diss/python/case10/weights-improvement-94.hdf5")  # WEIGHT PATH
        #print("loaded model weights from case10")

        checkpoint_path = "weights-improvement-{epoch:02d}.hdf5"

        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            checkpoint_path, verbose=1, save_weights_only=True,
            # Save weights, every epoch.
            save_freq='epoch')

        model.save_weights(checkpoint_path.format(epoch=0))
        print('Fitting model...')
        history = History()
        history = model.fit(imgs_train, imgs_mask_train, validation_data=(imgs_val, imgs_mask_val), batch_size=1,
                            epochs=100,
                            verbose=1, shuffle=True,
                            callbacks=[cp_callback])
        print(history.history.keys())
        df = pd.DataFrame(history.history)  # save epoch info into an excel sheet
        df.to_excel('dict11.xlsx')

    def test(self):  # method to test the neural network
        print("loading data")
       # imgs_test = self.load_data()
        imgs_test = np.load("C:/Users/oguri/Desktop/cases/case1/imgs_test.npy")
        print("loading data done")
        model = self.get_unet()
        model.load_weights("C:/Users/oguri/Desktop/unet-keras-master/model_data/best_epoch_weights.h5")  # load best weights
        print("got unet")

        print('predict test data')
        imgs_mask_predict = model.predict(imgs_test, batch_size=1, verbose=1)
        np.save("C:/Users/oguri/Desktop/cases/case1/test/imgs_mask_predict.npy", imgs_mask_predict)
        print(imgs_mask_predict.shape)

    def save_image(self):  # method to turn npy info into actual images and save them
        data = np.load("C:/Users/oguri/Desktop/cases/case1/test/imgs_mask_predict.npy")
        print(np.shape(data))
        print(type(data))

        array = np.split(data, 20)  # adjust depending on the number of testing images
        print(len(array))

        for i in range(0, 20):
            # creating image object of array

            a = array[i]
            print(a)

            print(a.shape)

            b = np.reshape(a, (256, 256, 1))

            print(b.shape)

            data = array_to_img(b)

            data = data.convert("1")
            print(data.size)
            print(data.mode)

            # saving the final output as a PNG file
            data.save("C:/Users/oguri/Desktop/cases/case1/test/results/%d.png" % i)

    def plot(self):
        model = self.get_unet()
        plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=False, rankdir='TB',
                   expand_nested=False, dpi=96)
        print(model.summary())
        font = ImageFont.truetype("arial.ttf", 45, encoding="unic")
        visualkeras.layered_view(model, legend=True, to_file='output.png', font=font).show()
        visualkeras.layered_view(model)


if __name__ == '__main__':
    case = myUnet()
    #case.plot()
    mydata = data.dataProcess(256, 256)
    #mydata.create_train_data()
    #mydata.create_test_data()
    #mydata.create_val_data()
    #case.train()
    case.test()
    #case.save_image()
