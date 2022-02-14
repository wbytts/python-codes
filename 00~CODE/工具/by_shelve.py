class ShelveHelper:
    """
    封装 shelve 模块的相关操作
    默认把数据存储到 /shelves/demo 中
    """

    def __init__(self, path="f:/shelves/demo"):
        import shelve
        self.path = path
        self.shelve = shelve

    def __getitem__(self, item):
        with self.shelve.open(self.path) as f:
            return f[item]

    def __setitem__(self, key, value):
        with self.shelve.open(self.path) as f:
            f[key] = value
