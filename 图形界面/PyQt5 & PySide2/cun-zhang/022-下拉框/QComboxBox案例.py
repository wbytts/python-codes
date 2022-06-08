from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox下拉框案例 - PyQt5中文网")
        self.resize(600, 500)
        self.city_dic = {
            '江苏省': {
                '南京': '025',
                '徐州市': '0516',
                '淮安市': '0517',
                '盐城市': '0515',
                '扬州市': '0514',
                '苏州市': '0512',
            },
            '浙江省': {
                '杭州市': '0571',
                '宁波市': '0574',
                '金华市': '0579',
                '舟山市': '0580',
                '温州市': '0577',
                '台州市': '0576',
            },
            '安徽省': {
                '合肥市': '0551',
                '滁州市': '0550',
                '宿州市': '0557',
                '巢湖市': '0565',
                '黄山市': '0559',
                '宣州市': '0563',
            },
            '河北省': {
                '石家庄市': '0311',
                '邯郸市': '0310',
                '保定市': '0312',
                '唐山市': '0315',
                '沧州市': '0317 ',
                '衡水市': '0318',
                '邢台市': '0319',
            },
        }
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        self.qcb1 = QComboBox(self)
        self.qcb1.move(100, 150)
        self.qcb1.resize(100, 40)

        self.qcb2 = QComboBox(self)
        self.qcb2.move(240, 150)
        self.qcb2.resize(100, 40)

        # 1.获取省一级，这里要先链接信号，然后添加数据，数据从无到有也能触发信号
        # self.qcb1.addItems(self.city_dic.keys())
        self.qcb1.currentIndexChanged[str].connect(self.qcb1_changed)
        self.qcb1.addItems(self.city_dic.keys())

        # 2.获得当前选中省的名称
        self.qcb1_changed(self.qcb1.currentText())

        # 4.城市区号获取方法
        self.qcb2.currentIndexChanged[int].connect(self.qcb2_changed)
        self.qcb2_changed(self.qcb2.currentIndex())

    def qcb1_changed(self, name):
        # print(name)
        # 3.根据省的名称到字典中查找下级城市名称
        citys = self.city_dic[name]
        # print(citys)
        # 从字典中获取下级城市名称到下一个下拉框中
        '''
        # self.qcb2.addItems(citys.keys())  # 这只会追加城市，所以要清空之前的数据,在重新添加条目
        self.qcb2.clear()
        # self.qcb2.addItems(citys.keys())
        '''
        self.qcb2.blockSignals(True)
        self.qcb2.clear()  # 这里会出现None结果，参考97行代码
        self.qcb2.blockSignals(False)

        for key, val in citys.items():  # 通过增加val数据来获取
            self.qcb2.addItem(key, val)
            # print(citys.items())

    def qcb2_changed(self, num):  # 这里传入条目的索引值
        # print(num) # 这里值为-1，会打印None
        print(self.qcb2.itemData(num))
        # 这里注意itemData()的用法


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
