import gzip
import random

import paddle
import paddle.nn.functional as F
import numpy as np

def load_data(mode = 'train' | None):
    """
    It loads the dataset from the file `data/mnist.json.gz` and returns the images and labels for the specified mode

    :param mode: 'train', 'valid', 'eval', defaults to train (optional)
    """

    dataset_path = 'data/mnist.json.gz'
    print('dataset start loading from {}....'.format(dataset_path))
    dataset = gzip.open(dataset_path)
    print('dataset loading success!')

    train_dataset, val_dataset, eval_dataset = dataset

    if mode == 'train':
        imgs, labels = train_dataset[0], train_dataset[1]
    elif mode == 'valid':
        imgs, labels = val_dataset[0], val_dataset[1]
    elif mode == 'eval':
        imgs, labels = eval_dataset[0], eval_dataset[1]
    else:
        raise Exception("mode can only be one of ['train', 'valid', 'eval']")

    print('dataset length: {}'.format(len(imgs)))

    # confirm data is right
    assert len(imgs) == len(labels),\
        "length of train_imgs({}) should be the same as train_labels({})".format(len(imgs), len(labels))
    # get the length from dataset
    imgs_length = len(imgs)

    index_list = list(range(imgs_length))
    batch_size =100

    # define data generator
    def data_generator():
        # shuffle the data when mode == 'train'
        if  mode == 'train':
            random.shuffle(index_list)





