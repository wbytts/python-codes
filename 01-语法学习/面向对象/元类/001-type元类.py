
# python里万物皆对象
# 所以类是对象，不妨叫 类对象
# 对象是由类构造的，类对象是对象，所以类对象也是由类构造的（体现在代码中是有一个 __class__ 属性）
# 那么 类对象的类，是什么呢？
# ！元类

# type是默认的元类，如下类型对象的 __class__ 都是 type
print(int.__class__)
print(str.__class__)
print(list.__class__)

# 可以使用 type 元类来实例化一个类对象
# 第一个参数：类名称
# 第二个参数：继承父类
# 第三个参数：属性字典
def run(self):
    print(f"{self.name}跑了")

Dog = type("Dog", (), {"name": "旺财", "age": 18, "run": run})
d = Dog()
d.run()

print(type(type.__class__))


