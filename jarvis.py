# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1089, 868)
        self.Friday = QtWidgets.QLabel(Form)
        self.Friday.setGeometry(QtCore.QRect(0, 0, 1091, 871))
        self.Friday.setText("")
        self.Friday.setPixmap(QtGui.QPixmap("C:/Users/HP/Downloads/7LP8.gif"))
        self.Friday.setObjectName("Friday")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 321, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/HP/Downloads/download.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(770, 800, 81, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("font: 75 14pt \"Microsoft YaHei\";background: green")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(870, 800, 81, 31))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("font: 75 14pt \"Microsoft YaHei\"; background: red")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(490, 30, 241, 51))
        self.textBrowser.setStyleSheet("background: transparent")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(790, 30, 241, 51))
        self.textBrowser_2.setStyleSheet("background: transparent")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Run"))
        self.pushButton_2.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    #this is a comment for github checking 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
