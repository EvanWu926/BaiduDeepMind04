#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py    
@Contact :   252392785@qq.com
@License :   (C)Copyright 2022-2029

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/12/6 21:58   Evan       1.0         None
'''
import json

# import lib
import paddle
from paddle.nn import Linear
import paddle.nn.functional as F
import numpy
import gzip

# 声明数据集位置
data_file = 'data/mnist.json.gz'
print('loading mnist dataset from {}......'.format(data_file))

# load mnist dataset
mnist_dataset = json.load(gzip.open(data_file))
print('mnist dataset load done')

# setting training_dataset, val_dataset, test_dataset
train_dataset, val_dataset, test_dataset = mnist_dataset

imgs, labels = train_dataset[0], train_dataset[1]
print(train_dataset.shape)

