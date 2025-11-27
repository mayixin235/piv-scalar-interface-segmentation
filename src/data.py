from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
import os
import glob
import cv2


class dataProcess(object):

    def __init__(self, out_rows, out_cols, data_path="C:/Users/oguri/Desktop/cases/case/train/image raw",
                 label_path="C:/Users/oguri/Desktop/cases/case/train/mask raw",
                 val_path="C:/Users/oguri/Desktop/cases/case/validation/image raw",
                 val_label_path="C:/Users/oguri/Desktop/cases/case/validation/mask raw",
                 test_path= "C:/Users/oguri/Desktop/cases/case/test/image raw",
                 #"C:/Users/hp/Desktop/diss/matlab/data/case14/test/image raw",
                 test_label_path="C:/Users/oguri/Desktop/cases/case/test/mask raw",
                 npy_path="C:/Users/oguri/Desktop/cases/case", img_type="png"):

        self.out_rows = out_rows
        self.out_cols = out_cols
        self.data_path = data_path
        self.label_path = label_path
        self.val_path = val_path
        self.val_label_path = val_label_path
        self.test_path = test_path
        self.test_label_path = test_label_path
        self.npy_path = npy_path
        self.img_type = img_type
        self.mean = False

    def create_train_data(self):
        i = 0
        print('-' * 30)
        print('Creating training images...')
        print('-' * 30)
        imgs = glob.glob(self.data_path + "/*." + self.img_type)
        print(len(imgs))
        imgdatas = np.ndarray((len(imgs), self.out_rows, self.out_cols, 3), dtype=np.uint8)
        imglabels = np.ndarray((len(imgs), self.out_rows, self.out_cols, 1), dtype=np.uint8)
        for imgname in imgs:
            midname = imgname[imgname.rindex("image raw") + 10:]
            img = load_img(self.data_path + "/" + midname)
            label = load_img(self.label_path + "/" + midname, grayscale=True)
            img = img_to_array(img)
            label = img_to_array(label)
            imgdatas[i] = img
            imglabels[i] = label
            if i % 100 == 0:
                print('Done: {0}/{1} images'.format(i, len(imgs)))
            i += 1
        print('loading done')
        np.save(self.npy_path + '/imgs_train.npy', imgdatas)
        np.save(self.npy_path + '/imgs_mask_train.npy', imglabels)
        print('Saving to .npy files done.')

    def create_val_data(self):
        i = 0
        print('-' * 30)
        print('Creating validation images...')
        print('-' * 30)
        imgs = glob.glob(self.val_path + "/*." + self.img_type)
        print(len(imgs))
        imgdatas = np.ndarray((len(imgs), self.out_rows, self.out_cols, 3), dtype=np.uint8)
        imglabels = np.ndarray((len(imgs), self.out_rows, self.out_cols, 1), dtype=np.uint8)
        for imgname in imgs:
            midname = imgname[imgname.rindex("image raw") + 10:]
            img = load_img(self.val_path + "/" + midname)
            label = load_img(self.val_label_path + "/" + midname, grayscale=True)
            img = img_to_array(img)
            label = img_to_array(label)
            imgdatas[i] = img
            imglabels[i] = label
            if i % 100 == 0:
                print('Done: {0}/{1} images'.format(i, len(imgs)))
            i += 1
        print('loading done')
        np.save(self.npy_path + '/imgs_val.npy', imgdatas)
        np.save(self.npy_path + '/imgs_mask_val.npy', imglabels)
        print('Saving to .npy files done.')

    def create_test_data(self):
        i = 0
        print('-' * 30)
        print('Creating test images...')
        print('-' * 30)
        imgs = glob.glob(self.test_path + "/*." + self.img_type)
        print(len(imgs))
        imgdatas = np.ndarray((len(imgs), self.out_rows, self.out_cols, 3), dtype=np.uint8)
        imglabels = np.ndarray((len(imgs), self.out_rows, self.out_cols, 1), dtype=np.uint8)
        for imgname in imgs:
            midname = imgname[imgname.rindex("image raw") + 10:]
            img = load_img(self.test_path + "/" + midname)
            label = load_img(self.test_label_path + "/" + midname, grayscale=True)
            img = img_to_array(img)
            label = img_to_array(label)
            imgdatas[i] = img
            imglabels[i] = label
            if i % 100 == 0:
                print('Done: {0}/{1} images'.format(i, len(imgs)))
            i += 1
        print('loading done')
        np.save(self.npy_path + '/imgs_test.npy', imgdatas)
        np.save(self.npy_path + '/imgs_mask_test.npy', imglabels)
        print('Saving to imgs_test.npy and imgs_test_mask.npy files done.')

    def load_train_data(self):
        print('-' * 30)
        print('load train images...')
        print('-' * 30)
        imgs_train = np.load(self.npy_path + "/imgs_train.npy")
        imgs_mask_train = np.load(self.npy_path + "/imgs_mask_train.npy")
        imgs_train = imgs_train.astype('float32')
        imgs_mask_train = imgs_mask_train.astype('float32')
        imgs_train /= 255
        mean = imgs_train.mean(axis=0)
        self.mean = mean
        imgs_train -= mean
        imgs_mask_train /= 255
        # mean = imgs_train.mean(axis=0)
        # np.divide(imgs_train, 255, out=imgs_train, casting="unsafe")
        # self.mean = mean
        # imgs_train -= mean
        imgs_mask_train[imgs_mask_train > 0.5] = 1
        imgs_mask_train[imgs_mask_train <= 0.5] = 0
        return imgs_train, imgs_mask_train

    def load_val_data(self):
        print('-' * 30)
        print('load train images...')
        print('-' * 30)
        imgs_val = np.load(self.npy_path + "/imgs_val.npy")
        imgs_mask_val = np.load(self.npy_path + "/imgs_mask_val.npy")
        imgs_val = imgs_val.astype('float32')
        imgs_mask_val = imgs_mask_val.astype('float32')
        imgs_val /= 255
        mean = imgs_val.mean(axis=0)
        self.mean = mean
        imgs_val -= mean
        imgs_mask_val /= 255
        # mean = imgs_val.mean(axis=0)
        # np.divide(imgs_val, 255, out=imgs_val, casting="unsafe")
        # self.mean = mean
        # imgs_val -= mean
        imgs_mask_val[imgs_mask_val > 0.5] = 1
        imgs_mask_val[imgs_mask_val <= 0.5] = 0
        return imgs_val, imgs_mask_val

    def get_mean(self):
        print("get mean image....")
        imgs_train = np.load(self.npy_path + "/imgs_train.npy")
        imgs_train /= 255
        # np.divide(imgs_train, 255, out=imgs_train, casting="unsafe")
        mean = imgs_train.mean(axis=0)
        self.mean = mean
        print("done mean image....")
        return mean

    def load_test_data(self):
        print('-' * 30)
        print('load test images...')
        print('-' * 30)
        imgs_test = np.load(self.npy_path + "/imgs_test.npy")
        imgs_mask_test = np.load(self.npy_path + "/imgs_mask_test.npy")
        imgs_test = imgs_test.astype('float32')
        imgs_mask_test = imgs_mask_test.astype('float32')
        imgs_test /= 255
        mean = self.mean
        # np.divide(imgs_test, 255, out=imgs_test, casting="unsafe")
        # mean = self.mean
        if self.mean.all() == False:
            mean = self.get_mean()
        # if not self.mean.all():
        #    mean = self.get_mean()
        imgs_test -= mean
        imgs_mask_test[imgs_mask_test > 0.5] = 1
        imgs_mask_test[imgs_mask_test <= 0.5] = 0
        return imgs_test, imgs_mask_test


if __name__ == "__main__":
    mydata = dataProcess(256, 256)
    mydata.create_train_data()
    mydata.create_val_data()
    mydata.create_test_data()
    imgs_train, imgs_mask_train = mydata.load_train_data()
    imgs_val, imgs_mask_val = mydata.load_val_data()
    imgs_test, imgs_mask_test = mydata.load_test_data()
    print(imgs_train.shape, imgs_mask_train.shape, imgs_val.shape, imgs_mask_val.shape, imgs_test.shape,
          imgs_mask_test.shape)
