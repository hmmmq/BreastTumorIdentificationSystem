# 划分训练集和验证集，总共1200，200张测试集，800张做训练，200张做验证
import os
import random


def main():
    random.seed(0)  # 设置随机种子，保证随机结果可复现

    files_path = "./VOCdevkit/ultra_detection/Annotations" #数据集的标签文件所在路径
    assert os.path.exists(files_path), "path: '{}' does not exist.".format(files_path)  #报错提醒

    val_rate = 0.2 # 验证集所占的比例

    files_name = sorted([file.split(".")[0] for file in os.listdir(files_path)]) # list存储所有文件名，以点为分隔符，【0】就是分隔符前面的内容。

    files_num = len(files_name) # 文件的数量
    val_index = random.sample(range(0, files_num), k=int(files_num*val_rate)) # 随机的范围是在0-1000，k是从1000里随机挑验证集
    train_files = []
    val_files = []
    for index, file_name in enumerate(files_name):
        if index in val_index: # 在
            val_files.append(file_name)
        else: # 不在
            train_files.append(file_name)

    try:
        train_f = open("train.txt", "x")
        eval_f = open("val.txt", "x")
        train_f.write("\n".join(train_files))
        eval_f.write("\n".join(val_files))
    except FileExistsError as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
