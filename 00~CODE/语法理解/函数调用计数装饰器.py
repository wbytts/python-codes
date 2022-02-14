class tracer:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('函数 %s 被调用了 %s 次' % (self.func.__name__, self.calls))
        return self.func(*args, **kwargs)


@tracer
def show():
    print('Hello World')



show()
show()
show()
show()
show()
show()
