import numpy as np
import paddle.io
from paddle.io import Dataset


class RandomDataset(Dataset):
    def __init__(self, num_samples):

        super().__init__()
        self.num_samples = num_samples

    def __getitem__(self, idx):
        image = np.random.random([784]).astype('float32')
        label = np.random.randint(0, 9, (1, )).astype('float32')
        return image, label

    def __len__(self):
        return self.num_samples


dataset = RandomDataset(100)
# for i in range(len(dataset)):
    # print(dataset[i])

loader = paddle.io.DataLoader(dataset, batch_size= 10, shuffle= True, drop_last=True, num_workers=2)
for i, data in enumerate(loader()):
    images, labels = data[0], data[1]
    print("batch_id: {}, 训练数据shape: {}, 标签数据shape: {}".format(i, images.shape, labels.shape))