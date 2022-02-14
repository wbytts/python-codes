from imp import reload

# 重新导入一个模块
# reload(xxx)

'''
reload函数自身载入并运行了文件当前脚本的代码，如果已经存在另一个窗口中修改并保存了它，那将范引出修改变化！
reload一个模块，必须在这个模块成功导入之后才能使用
reload的返回值：<module名 from 模块的路径> 加载的模块

！from导入的名字不会被reload更新
reload是不可传递的，重载一个模块不会重载该模块所导入的任何模块，只会重载当前模块
'''
