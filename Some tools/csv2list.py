import pandas
import numpy as np


def main():
    train_csv = pandas.read_csv('./data-952/csv/train.csv', chunksize=1)
    temp_list = []  # 整个表格数据
    for item in train_csv:
        data = item.values.tolist()
        temp_list.append(data)
    train_list = []
    for i in range(len(temp_list)):
        if i % 2 == 0:
            train_list.append(temp_list[i])
    # print(len(train_list))
    # test = train_list[0][0][3]
    # temp = test.split('_')
    # target = 1 if test == 'cancer' else 0
    # print(target)
    # box = np.array([np.array(list(map(int, box.split(',')))) for box in train_list[0][0][4:]])
    # box = np.array([box for box in train_list[0][0][4:]], dtype=np.float32)
    # print(box)
    return train_list

    # [
    #     [['A_1004_1.LEFT_CC.png', 512, 1024, 'cancer', 333, 284, 374, 344]],
    #     [['A_1004_1.LEFT_MLO.png', 512, 1024, 'cancer', 260, 344, 298, 397]]
    # ]

    # list_name = []  # 拆分出文件名的前缀如：A_1004_1.LEFT_MLO
    # list_label = []
    # for i in range(len(train_csv_list)):
    #     predata = train_csv_list[i][0][0]
    #     list_label.append(train_csv_list[i][0][3])
    #     temp = predata.split('_')
    #     redata = temp[0] + '_' + temp[1] + '_' + temp[2]
    #     list_name.append(redata)
    # list_name_new = []  # 文件名去重
    # list_label_new = []  # 标签去重
    # for i in range(len(list_name)):
    #     if i % 2 == 0:
    #         list_name_new.append(list_name[i])
    #         list_label_new.append(list_label[i])
    # return list_name_new, list_label_new


if __name__ == '__main__':
    main()
# print(len(list_name_new))
# print(list_name_new)
# print(len(list_label_new))
# print(list_label_new)

# 图像读取模块
# self.images_pair_name=csvread  =['A_1007_1.right',...]
# self.labels = csvread[]
# self.imagedir = ./images/
# self.__getitem__(self,i): # i <len(self.images_pair_name)
#    inputname = self.images_pair_name[i]
#    label = self.labels[argindex(inputname)]
#    ccimg = imread(self.imagedir+inputname+'cc.png')
#   mloimg = imread(self.imagedir+inputname+'mlo.png')
#
#  return [ccimg,mloimg],label
