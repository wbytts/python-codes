from PyQt5.QtQuick import QQuickView
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtQml, QtQuick
import sys

app = QtWidgets.QApplication(sys.argv)
engine = QtQml.QQmlApplicationEngine(QUrl('Qml1.qml'))  # 显示window界面
sys.exit(app.exec_())
