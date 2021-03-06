
'''
用简单的术语来讲：每一个以 .py 结尾的python源代码文件都是一个模块
    其他文件可以通过导入一个模块读取这个模块定义的内容---导入本质上来讲就是载入另一个文件，并给予读取那个我呢间内容的权限
    一个模块的内容通过其属性从而被外部世界使用

模块是python程序中最大的程序结构

导入操作运行文件中的代码，这个文件作为最后一步正在加载，正是如此，导入文件是另一种运行文件的方法

每当导入一个模块的时候，python都会从头到尾的执行模块文件中的每一条代码！
可以直接运行的模块文件，往往也叫做脚本（一个顶层程序文件的非官方，非正式的说法，俗语，粗话）
所以：导入，同时也是一种启动程序的方法

在默认的情况下，每次会话中，只有第一次导入时会运行模块中的代码（后面的导入不会反映出模块的修改）。
为什么？ ！导入是一个开销很大的操作！。所以，不用的东西界就别导入了

模块，也可以理解成   “变量名的包”  “变量名组成的一个集合（命名空间）”
属性：绑定在特定对象上的变量名

导入者得到了模块文件中顶层所定义的所有变量名的访问权限


python程序往往由多个模块文件构成，通过import语句连接在一起，每个模块文件是一个变量包（命名空间）
每个模块都是一个自包含的命名空间
一个模块不能看到其它文件中定义的变量名，除非它显式地导入了那个文件

模块文件在代码中起到了 “最小化命名冲突” 的作用，因为每个文件都是一个独立完备的命名空间
'''
