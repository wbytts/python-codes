import pickle


def pickle_dump(obj, path):
    """
    序列化对象，保存为指定路径的文件
    :param obj: 要序列化的对象
    :param path: 文件路径
    :return:
    """
    f = open(path, 'wb')
    pickle.dump(obj, f)
    f.close()


def pickle_laod(path):
    """
    从指定路径的文件中加载对象
    :param path: 文件路径
    :return: 返回加载的对象
    """
    f = open(path, 'rb')
    obj = pickle.load(f)
    f.close()
    return obj
