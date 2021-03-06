
'''
当在一个程序中使用变量名时，创建、查找、修改、删除变量名都是在所谓的命名空间中进行的
命名空间：变量名存放的地方
我们在讨论代码中查找变量名时，作用域这个术语指的就是命名空间
！也就是说，在源代码中，变量被赋值的位置，决定了这个变量名能被访问到的范围

python中一切与变量名有关的事件（包括作用域分类）都发生在赋值的时候
变量名在第一次赋值时才能存在，并且只有经过赋值后才能使用
python将一个变量名被赋值的地点关联为（绑定给）一个特定的命名空间
换句话说：在代码中给一个变量赋值的地方决定了这个变量将存在于哪个命名空间，也就是它的可见范围

函数为程序增加了一个额外的命名空间层来最小化相同变量名之间的潜在冲突
再默认的情况下，一个函数内赋值的所有变量都与该函数的命名空间相关联
这意味着：
    在def内赋予的变量名只能够被def内的代码使用
    在def内赋值的变量名与在def外赋值的变量名不冲突，即使同名也是两个不同的变量

如果一个变量在def内部赋值，它对于该函数而言是局部的
如果一个变量在一个外层的def中赋值，对于内存的函数来说，它是非局部的
如果一个变量在所有def外赋值，它对整个文件来说是全局的
我们将其称为 语义作用域
'''
