# #!/usr/bin/env python
# # -*- encoding: utf-8 -*-
# '''
# @File    :   main.py
# @Contact :   252392785@qq.com
# @License :   (C)Copyright 2022-2029
#
# @Modify Time      @Author    @Version    @Desciption
# ------------      -------    --------    -----------
# 2022/12/6 21:58   Evan       1.0         None
# '''
# import json
# import random
#
# # import lib
# import paddle
# from paddle.nn import Linear
# import paddle.nn.functional as F
# import numpy as np
# import gzip
#
# # 声明数据集位置
# data_file = 'data/mnist.json.gz'
# print('loading mnist dataset from {}......'.format(data_file))
#
# # load mnist dataset
# mnist_dataset = json.load(gzip.open(data_file))
# print('mnist dataset load done')
#
# # setting training_dataset, val_dataset, test_dataset
# train_dataset, val_dataset, test_dataset = mnist_dataset
#
# train_imgs, train_labels = train_dataset[0], train_dataset[1]
# # print('train data length: imgs:{}, labels:{}'.format(len(imgs), len(labels)))
#
# # imgs, labels = val_dataset[0], val_dataset[1]
# # print('val data length: {}, {}'.format(len(imgs), len(labels)))
#
# # imgs, labels = val = test_dataset[0], test_dataset[1]
# # print('test data length: {}, {}'.format(len(imgs), len(labels)))
#
# # create index for data
# index_list = list(range(len(train_imgs)))
# # init batch size
# batch_size = 100
# random.shuffle(index_list)
#
# def data_generator():
#     imgs_list = []
#     label_list = []
#
#     for i in index_list:
#         img = np.array(train_imgs[i]).astype('float32')
#         label = np.array(train_labels[i]).astype('float32')
#         imgs_list.append(img)
#         label_list.append(label)
#
#         if len(imgs_list) == batch_size:
#             yield np.array(imgs_list), np.array(label_list)
#             imgs_list = []
#             label_list = []
#
#     if len(imgs_list) > 0:
#         yield np.array(imgs_list), np.array(label_list)
#     return data_generator
#
#
# train_loader = data_generator
# # 以迭代的形式读取数据
# for batch_id, data in enumerate(train_loader()):
#     image_data, label_data = data
#     if batch_id == 0:
#         # 打印数据shape和类型
#         print("打印第一个batch数据的维度:")
#         print("图像维度: {}, 标签维度: {}".format(image_data.shape, label_data.shape))
#     break
import gzip
import json

import numpy as np
import paddle.io
from paddle.io import Dataset


class MnistDataset(Dataset):
    def __init__(self, mode):

        super().__init__()
        data = json.load(gzip.open('data/mnist.json.gz'))
        train_dataset, val_dataset, eval_dataset = data

        if mode == 'train':
            images, labels = train_dataset[0], train_dataset[1]

        elif mode == 'valid':
            images, labels = val_dataset[0], val_dataset[1]

        elif mode == 'eval':
            images, labels = eval_dataset[0], eval_dataset[1]

        else:
            raise Exception("The mode must be one of ['train', 'valid', 'eval']")

        # assert images and labels length must be same.
        assert len(images) ==len(labels), "length of train_imgs({}) should be the same as train_labels({})".format(len(images), len(labels))

        self.images = images
        self.labels = labels

    def __getitem__(self, idx):
        images = np.array(self.images[idx]).astype('float32')
        labels = np.array(self.labels[idx]).astype('float32')
        return images, labels

    def __len__(self):
        return len(self.images)

