import gzip
import json
import random

import numpy as np
import paddle.io


# import lib
class MnistDataset(paddle.io.Dataset):


    def __init__(self, mode):
        """
        > The function takes in a mode, which can be either 'train', 'valid', or 'eval', and returns a dataset of images and
        labels

        :param mode: 'train', 'valid', 'eval'
        """

        super().__init__()

        datafile = 'data/mnist.json.gz'
        data = json.load(gzip.open(datafile))

        train_set, val_set, eval_set = data

        if mode == 'train':
            images, labels = train_set[0], train_set[1]
        elif mode == 'valid':
            images, labels = val_set[0], val_set[1]
        elif mode == 'eval':
            images, labels = eval_set[0], eval_set[1]
        else:
            raise Exception("mode can only be one of ['train', 'valid', 'eval']")

        img_lenth = len(images)
        assert len(images) == len(labels), \
            "length of train_imgs({}) should be the same as train_labels({})".format(len(images), len(labels))

        self.images = images
        self.labels = labels

    def __getitem__(self, idx):
        """
        This function returns the image and label of the index specified by the argument idx

        Args:
          idx: the index of the image in the dataset

        Returns:
          The image and label are being returned.
        """

        image = np.array(self.images[idx]).astype('float32')
        label = np.array(self.labels[idx]).astype('float32')

        return image, label

    def __len__(self):
        """
        The __len__ function returns the length of the images list

        Returns:
          The length of the images list.
        """
        return len(self.images)
