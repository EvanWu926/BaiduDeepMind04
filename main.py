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

# from LoadDataAync import *
#
# train_dataset = MnistDataset('train')
#
# if __name__ == '__main__':
#     data_loader = paddle.io.DataLoader(train_dataset, batch_size=100, shuffle=True, drop_last=True, num_workers=4)
#
#     for i, data in enumerate(data_loader()):
#         images, labels = data
#         print(i, images.shape, labels.shape)
#         if i >= 2:
#             break

from datetime import datetime, timedelta


def isHoliday(start_date, day):
    # 输入开始日期
    start_date = input("请输入开始日期(格式为yyyy-MM-dd):")
    # 将开始日期转换为datetime类型
    start_date = datetime.strptime(start_date, "%Y-%m-%d")

    # 输入持续天数
    days = int(input("持续天数:"))

    # 计算包含的法定节假日天数
    holiday_days = 0
    for i in range(days):
        date = start_date + timedelta(days=i)
        # 如果年份小于等于2022年，并且当天是法定节假日，则统计包含的法定节假日天数
        if date.year <= 2022 and is_holiday(date):
            holiday_days += 1

    # 输出包含的法定节假日天数
    print("包含的法定节假日天数:", holiday_days)


# 判断某个日期是否为法定节假日
def is_holiday(date):
        # 这里只是简单判断是否为周末，实际应该根据具体情况判断
    return date.weekday() in (5, 6)


# 产假天数
maternity_leave = 98
# 生育假天数
pregnancy_leave = 60

# 输入产假开始日期
start_date = input("请输入产假开始日期(格式为yyyy-MM-dd):")
# 将产假开始日期转换为datetime类型
start_date = datetime.strptime(start_date, "%Y-%m-%d")

# 输入是否难产
difficult_delivery = input("是否难产(是/否):")
# 输入胞胎数量
twins_number = input("胞胎数量:")

# 如果难产，增加产假15天
if difficult_delivery =="是":
  maternity_leave += 15

# 根据胞胎数量增加产假天数
maternity_leave += 15 * int(twins_number)

# 计算产假结束日期
end_date = start_date + timedelta(days=maternity_leave)
# 计算生育假结束日期
pregnancy_end_date = start_date + timedelta(days=maternity_leave + pregnancy_leave)

# 如果生育假结束日期遇到法定节假日，将生育假结束日期顺延
while isHoliday(pregnancy_end_date):
  pregnancy_end_date

