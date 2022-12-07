# It's a linear layer with 784 input features and 1 output feature.
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Network.py    
@Contact :   252392785@qq.com
@License :   (C)Copyright 2022-2029

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/12/7 21:25   Evan       1.0         None
'''
import paddle.nn
from loadData import *

# import lib

paddle.vision.set_image_backend('cv2')

# It's a linear model that takes in a 784-dimensional vector and outputs a 1-dimensional vector
class MNSIT(paddle.nn.Linear):
    def __init__(self):
        super(MNSIT, self).__init__(in_features=784, out_features=1)

        self.fc = paddle.nn.Linear(in_features=784, out_features=1)

def train(model):
    """
    *|MARCADOR_CURSOR|*

    :param model: The model to be trained
    """

    model = MNSIT()
    model.train()

    train_data =load_data(mode='train')
    opt = paddle.optimizer.SGD(learning_rate=0.001, parameters=model.parameters())
    # train num is 10
    epoch_num = 10
    for epoch_id in range(epoch_num):
        for batch_id, data in enumerate(train_data()):
            images, labels = data
            images = paddle.to_tensor(images)
            labels = paddle.to_tensor(labels)

            predict =model(images)

            loss = F.square_error_cost(predict, labels)
            avg_loss = paddle.mean(loss)

            if batch_id % 200 ==0:
                print("epoch: {}, batch: {}, loss is: {}".format(epoch_id, batch_id, avg_loss.numpy()))

            avg_loss.backward()
            opt.step()
            opt.clear_gradients()

    paddle.save(model.state_dict(), 'data/mnist.pdparams')


train_model = MNSIT()
train(train_model)
