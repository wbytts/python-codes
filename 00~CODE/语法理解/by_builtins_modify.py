import builtins

class list(builtins.list):

    def append(self, obj):
        builtins.list.append(self, obj)
        return self

