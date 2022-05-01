# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frameless.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormFrameless(object):
    def setupUi(self, FormFrameless):
        FormFrameless.setObjectName("FormFrameless")
        FormFrameless.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormFrameless)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetTitleBar = QtWidgets.QWidget(FormFrameless)
        font = QtGui.QFont()
        font.setFamily("Symbola")
        self.widgetTitleBar.setFont(font)
        self.widgetTitleBar.setObjectName("widgetTitleBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetTitleBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonMinimum = QtWidgets.QPushButton(self.widgetTitleBar)
        self.buttonMinimum.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonMinimum.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("webdings")
        self.buttonMinimum.setFont(font)
        self.buttonMinimum.setObjectName("buttonMinimum")
        self.horizontalLayout.addWidget(self.buttonMinimum)
        self.buttonMaximum = QtWidgets.QPushButton(self.widgetTitleBar)
        self.buttonMaximum.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonMaximum.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("webdings")
        self.buttonMaximum.setFont(font)
        self.buttonMaximum.setObjectName("buttonMaximum")
        self.horizontalLayout.addWidget(self.buttonMaximum)
        self.buttonNormal = QtWidgets.QPushButton(self.widgetTitleBar)
        self.buttonNormal.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonNormal.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("webdings")
        self.buttonNormal.setFont(font)
        self.buttonNormal.setObjectName("buttonNormal")
        self.horizontalLayout.addWidget(self.buttonNormal)
        self.buttonClose = QtWidgets.QPushButton(self.widgetTitleBar)
        self.buttonClose.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonClose.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("webdings")
        self.buttonClose.setFont(font)
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout.addWidget(self.buttonClose)
        self.verticalLayout.addWidget(self.widgetTitleBar)
        self.textEdit = QtWidgets.QTextEdit(FormFrameless)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(FormFrameless)
        QtCore.QMetaObject.connectSlotsByName(FormFrameless)

    def retranslateUi(self, FormFrameless):
        _translate = QtCore.QCoreApplication.translate
        FormFrameless.setWindowTitle(_translate("FormFrameless", "Form"))
        self.buttonMinimum.setToolTip(_translate("FormFrameless", "Minimum"))
        self.buttonMinimum.setText(_translate("FormFrameless", "0"))
        self.buttonMaximum.setToolTip(_translate("FormFrameless", "Maximum"))
        self.buttonMaximum.setText(_translate("FormFrameless", "1"))
        self.buttonNormal.setToolTip(_translate("FormFrameless", "Normal"))
        self.buttonNormal.setText(_translate("FormFrameless", "2"))
        self.buttonClose.setToolTip(_translate("FormFrameless", "Close"))
        self.buttonClose.setText(_translate("FormFrameless", "r"))
        self.textEdit.setHtml(_translate("FormFrameless", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">frameless window with move and resize</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormFrameless = QtWidgets.QWidget()
    ui = Ui_FormFrameless()
    ui.setupUi(FormFrameless)
    FormFrameless.show()
    sys.exit(app.exec_())
