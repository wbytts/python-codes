# coding=utf-8
from sklearn import preprocessing
import numpy as np
from datatool import evaluation
import pickle
from tqdm import tqdm
from sklearn.decomposition import PCA


def estimate_entropy_of_sensor(sensor):
    TotolEvent = np.size(sensor, 1)  # 所有的子特征
    totalServer = np.size(sensor, 0)  # 所有的服务总类
    Hz = 0
    for lines in sensor:
        m = 0
        p = 0
        global log_number
        log_number = 0
        h = lines.copy()
        h[h > 0] = 1
        m = np.sum(h)
        if m == 0:
            log_number = 0
        else:
            p = m / (totalServer * TotolEvent)
            log_number = np.log2(p) * p * (-1)
    Hz = Hz + log_number  # 香农熵计算
    return Hz / (totalServer * TotolEvent)


# combSUM
def combSUM(sensor):
    return [np.sum(value) for value in sensor]


def combMin(sensor):
    return [np.min(value) for value in sensor]


def combMax(sensor):
    return [np.max(value) for value in sensor]


def combEVERAGE(sensor):
    return [np.mean(value) for value in sensor]


# 欧氏距离计算
def distEclud(x, y):
    return np.sqrt(np.sum((x - y) ** 2))  # 计算欧氏距离


# 为给定数据集构建一个包含K个随机质心的集合
def randCent(dataSet, k):
    m, n = dataSet.shape
    centroids = np.zeros((k, n))
    for i in range(k):
        index = int(np.random.uniform(0, m))  #
        centroids[i, :] = dataSet[index, :]
    return centroids


# k均值聚类
def KMeans(dataSet, k):
    m = np.shape(dataSet)[0]  # 行的数目
    # 第一列存样本属于哪一簇
    # 第二列存样本的到簇的中心点的误差
    clusterAssment = np.mat(np.zeros((m, 2)))
    clusterChange = True
    # 第1步 初始化centroids
    centroids = randCent(dataSet, k)
    while clusterChange:
        clusterChange = False

        # 遍历所有的样本（行数）
        for i in range(m):
            minDist = 100000.0
            minIndex = -1

            # 遍历所有的质心
            # 第2步 找出最近的质心
            for j in range(k):
                # 计算该样本到质心的欧式距离
                distance = distEclud(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist = distance
                    minIndex = j
            # 第 3 步：更新每一行样本所属的簇
            if clusterAssment[i, 0] != minIndex:
                clusterChange = True
                clusterAssment[i, :] = minIndex, minDist ** 2
        # 第 4 步：更新质心
        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssment[:, 0].A == j)[0]]  # 获取簇类所有的点
            centroids[j, :] = np.mean(pointsInCluster, axis=0)  # 对矩阵的行求均值

    return centroids


# Mass
def Mass_function(comb_list, shannon_array):
    mass_function = []
    # 香浓熵归一化
    sum = np.sum(shannon_array)
    if sum == 0:
        shanon_normalist = np.full_like(shannon_array, 1.0 / 3.0)
    else:
        shanon_normalist = shannon_array / sum
    shannon_j = np.subtract(np.ones_like(shanon_normalist), shanon_normalist)
    mass = []  # mass函数
    for lines in comb_list:
        sum = 0
        sum = np.sum(lines)
        if sum == 0:
            massdata = np.full_like(lines, 1.0 / len(lines))
        else:
            massdata = lines / sum
        mass.append(massdata)
    for i in range(len(shannon_j)):
        mass[i] = [x * shannon_j[i] for x in mass[i]]
    mass = np.transpose(mass)
    mass_function = np.insert(mass, len(mass), shanon_normalist, 0)

    return mass_function


# DS证据理论
def combinare(d1, d2):
    d1 = np.array(d1)
    d2 = np.array(d2)
    K = np.sum(np.outer(d1[:-1], d2[:-1])) - np.dot(d1[:-1], d2[:-1])
    list1 = [((d1[i] * d2[-1] + d1[-1] * d2[i] + d1[i] * d2[i])) / (1.0 - K) for i in range(len(d1) - 1)]
    list1.append((d1[-1] * d2[-1]) / (1.0 - K))
    return list1  # DS融合结果


# 计算香浓熵，取出排名并进行对比,返回排序后的api排名位置列表
def show_data_sorted(masslistall):
    masslistall = np.transpose(masslistall)
    last = masslistall[0]
    for i in range(1, len(masslistall)):
        last = combinare(last, masslistall[i])  # 证据理论的结果
    allserver = [i for i in range(len(last) - 1)]
    rec = dict(zip(allserver, last))  # 字典存储所有的排名
    rec_sorted = sorted(rec.items(), key=lambda x: x[1], reverse=True)  # 按照字典里面值的元组进行降序排列
    sorted_list = []  # 最后排名结果api位置
    for lines in rec_sorted:
        sorted_list.append(lines[0])
    sorted_list = sorted_list[:20]  # 只取前20个
    return sorted_list


def perform_recommendation(mashup_list, api_list, sensor2, sensor3, sensor4, test_dict, top_n, log, comb):
    lenght = 0
    API_test = []
    for i in tqdm(range(1, len(mashup_list) + 1), desc='Recommendation of API...'):  # 抽取出一类mashup进行推荐

        sensor2_list = sensor2[lenght:i * len(api_list) - 1]
        sensor3_list = sensor3[lenght:i * len(api_list) - 1]
        sensor4_list = sensor4[lenght:i * len(api_list) - 1]

        entropy_list = []
        entropy_list.append(estimate_entropy_of_sensor(sensor2_list))
        entropy_list.append(estimate_entropy_of_sensor(sensor3_list))
        entropy_list.append(estimate_entropy_of_sensor(sensor4_list))

        min_max_scaler = preprocessing.MinMaxScaler()
        sensor2_list = min_max_scaler.fit_transform(sensor2_list)
        min_max_scaler = preprocessing.MinMaxScaler()
        sensor3_list = min_max_scaler.fit_transform(sensor3_list)
        min_max_scaler = preprocessing.MinMaxScaler()
        sensor4_list = min_max_scaler.fit_transform(sensor4_list)

        comb_list = []
        if comb == 'combEVERAGE':
            comb_list.append(combEVERAGE(sensor2_list))
            comb_list.append(combEVERAGE(sensor3_list))
            comb_list.append(combEVERAGE(sensor4_list))
        if comb == 'combSUM':
            comb_list.append(combSUM(sensor2_list))
            comb_list.append(combSUM(sensor3_list))
            comb_list.append(combSUM(sensor4_list))
        if comb == 'combMin':
            comb_list.append(combMin(sensor2_list))
            comb_list.append(combMin(sensor3_list))
            comb_list.append(combMin(sensor4_list))
        if comb == 'combMax':
            comb_list.append(combMax(sensor2_list))
            comb_list.append(combMax(sensor3_list))
            comb_list.append(combMax(sensor4_list))
        if comb == 'PCA':
            comb_list.append(
                (min_max_scaler.fit_transform(PCA(n_components=1).fit_transform(sensor2_list))).reshape(-1))
            comb_list.append(
                (min_max_scaler.fit_transform(PCA(n_components=1).fit_transform(sensor3_list))).reshape(-1))
            comb_list.append(
                (min_max_scaler.fit_transform(PCA(n_components=1).fit_transform(sensor4_list))).reshape(-1))
        mass = Mass_function(comb_list, entropy_list)
        api = show_data_sorted(mass)  # 返回api排名列表
        API_URI_List = [api_list[i] for i in api]
        API_test.append(API_URI_List)

        lenght = i * len(api_list)

    rec = dict(zip(mashup_list, API_test))
    # 提取排序后的api和数据
    sorted_data = data(test_dict, rec)
    # 测试文件
    test_data = data(test_dict, test_dict)

    for n in top_n:
        #        test=take_n_data(test_data,n)
        rec = take_n_data(sorted_data, n)
        NDCG, Precision, Recall, Ham_dist = evaluation(rec, test_data, n)
        nn = np.mean(NDCG)  # 求均值
        rr = np.mean(Recall)
        pp = np.mean(Precision)
        hh = np.mean(Ham_dist)
        print("%s:Mean Top-%d Recall: %f Precision: %f NDCG: %f Ham_dist: %F" % (comb, n, rr, pp, nn, hh))
        log.write("%s: Mean Top-%d Recall: %f Precision: %f NDCG: %f Ham_dist: %F\n" % (comb, n, rr, pp, nn, hh))
        log.flush()
    print('succesful!')


# 根据mashup挑出api重新组成字典
def data(all_mashup, all_data):
    the_sorted_data = []
    for mashup in all_mashup:
        the_sorted_data.append(all_data[mashup])
    the_sorted_data = dict(zip(all_mashup, the_sorted_data))
    return the_sorted_data


# 取前N个api
def take_n_data(n_data, n):
    tops_list = []
    keys = list(n_data.keys())
    for i in range(len(keys)):
        m_i = n_data[keys[i]][:n]
        tops_list.append(m_i)
    top_list = dict(zip(keys, tops_list))
    return top_list


def main():
    sensor2 = pickle.load(open('out_features\sim_cf_sensor.pickle', 'rb'))  # 加载pickle文件
    sensor3 = pickle.load(open('out_features\sim_sensor.pickle', 'rb'))
    sensor4 = pickle.load(open('out_features\\text_sensor.pickle', 'rb'))
    mashup_all = open('mashup_2013.txt', 'r', encoding='utf-8')  # open files
    api_all = open('api_2013.txt', 'r', encoding='utf-8')
    test_dict_list = open("dataset\mashup_used_api.txt", 'r')
    test_dict = eval(test_dict_list.read())
    log = open('out_features\Finally_data.log', 'a')
    log.write("############################################### \n")
    log.flush()
    # evaluations
    perform_recommendation([str.strip() for str in mashup_all],
                           [str.strip() for str in api_all], sensor2, sensor3, sensor4, test_dict,
                           [1, 5, 10, 15, 20], log, 'combEVERAGE')
    # close files
    mashup_all.close()
    api_all.close()
    test_dict_list.close()
    log.close()


if __name__ == '__main__':
    main()
