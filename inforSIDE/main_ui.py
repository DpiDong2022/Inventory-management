# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\copperdai\Desktop\INVENTORY_project\inforSIDE\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_inputInforItem(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(203, 136)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 0, 91, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.boxQuantity = QtWidgets.QSpinBox(self.layoutWidget)
        self.boxQuantity.setMinimum(1)
        self.boxQuantity.setMaximum(1000000)
        self.boxQuantity.setObjectName("boxQuantity")
        self.verticalLayout_2.addWidget(self.boxQuantity)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 84, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.boxPrice = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.boxPrice.setMinimum(0.1)
        self.boxPrice.setMaximum(3000.0)
        self.boxPrice.setSingleStep(0.1)
        self.boxPrice.setObjectName("boxPrice")
        self.verticalLayout.addWidget(self.boxPrice)
        self.verticalLayout_3.addWidget(self.frame)
        self.buttoSelectIamge = QtWidgets.QPushButton(Dialog)
        self.buttoSelectIamge.setStyleSheet("QPushButton:!pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"border: 2px solid rgb(200, 200, 200);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(153, 153, 153);\n"
"    border-radius:4px;\n"
"    border: 2px solid Blue\n"
"}")
        self.buttoSelectIamge.setObjectName("buttoSelectIamge")
        self.verticalLayout_3.addWidget(self.buttoSelectIamge)
        self.buttonOK = QtWidgets.QPushButton(Dialog)
        self.buttonOK.setEnabled(False)
        self.buttonOK.setObjectName("buttonOK")
        self.verticalLayout_3.addWidget(self.buttonOK)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "price, quantity, hold"))
        self.label_2.setText(_translate("Dialog", "Quantity"))
        self.label.setText(_translate("Dialog", "Price"))
        self.buttoSelectIamge.setText(_translate("Dialog", "Select image"))
        self.buttonOK.setText(_translate("Dialog", "OK"))
