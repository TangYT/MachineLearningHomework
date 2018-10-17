import random

result_set = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}

data_file = open('./IRIS/iris.data')
data_set = data_file.readlines()
data_file.close()

# 设定学习速度
learning_rate = 0.01
# 统计准确率
accuracy = 0.
# 用5折法求算法平均性能
for i in range(5):
    # w1,w2,w3分别为3个类别对应的分类器
    w = [[0. for k in range(5)] for j in range(3)]

    # 分割验证集
    test_data = []
    train_data = []
    for j, data in enumerate(data_set):
        if j % 5 == i:
            test_data.append(data)
        else:
            train_data.append(data)

    for j in range(10000):
        # 取出训练数据
        data = random.choice(train_data)
        a = data.strip().split(',')

        if a == ['']:
            break

        # 用3个分类器计算样本的分类结果
        f = [0.] * 3
        for t in range(3):
            for k in range(4):
                f[t] = f[t] + w[t][k] * float(a[k])
            f[t] = f[t] + w[t][4]

        # 如果分类器w[t]错误，修改w[t]
        for t in range(3):
            if f[t] >= 0 and not result_set[a[4]] == t:
                for k in range(4):
                    w[t][k] = w[t][k] - learning_rate * float(a[k])
                w[t][4] = w[t][4] - learning_rate
            elif f[t] <= 0 and result_set[a[4]] == t:
                for k in range(4):
                    w[t][k] = w[t][k] + learning_rate * float(a[k])
                w[t][4] = w[t][4] + learning_rate

    sum_num = 0
    correct_num = 0
    for data in test_data:
        # 取出训练数据
        sum_num = sum_num + 1
        a = data.strip().split(',')

        if a == ['']:
            break

        # 用3个分类器计算样本的分类结果
        f = [0.] * 3
        for t in range(3):
            for k in range(4):
                f[t] = f[t] + w[t][k] * float(a[k])
            f[t] = f[t] + w[t][4]

        # 判断分类结果
        if f[0] / (f[0] + f[1] + f[2]) > f[1] / (f[0] + f[1] + f[2]):
            if f[0] / (f[0] + f[1] + f[2]) > f[2] / (f[0] + f[1] + f[2]):
                classify = 0
            else:
                classify = 2
        else:
            if f[1] / (f[0] + f[1] + f[2]) > f[2] / (f[0] + f[1] + f[2]):
                classify = 1
            else:
                classify = 2
        if classify == result_set[a[4]]:
            correct_num = correct_num + 1
    accuracy = accuracy + correct_num / sum_num
print(accuracy / 5)
