# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\copperdai\Desktop\Inventory_swim_store_PhungDaiDong\colorSIDE\choosecolor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_chooseColor(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(216, 232)
        Dialog.setMinimumSize(QtCore.QSize(216, 232))
        Dialog.setMaximumSize(QtCore.QSize(216, 232))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Logo-EAUT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 185, 166))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_brown = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_brown.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_brown.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_brown.setFont(font)
        self.pushButton_brown.setStyleSheet("QPushButton:!pressed{\n"
"        border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(165, 42, 42);\n"
"    color: rgb(165, 42, 42);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/done.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_brown.setIcon(icon1)
        self.pushButton_brown.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_brown.setObjectName("pushButton_brown")
        self.gridLayout.addWidget(self.pushButton_brown, 1, 4, 1, 1)
        self.pushButton_teal = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_teal.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_teal.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_teal.setFont(font)
        self.pushButton_teal.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(0, 128, 128);\n"
"color: rgb(0, 128, 128);\n"
"}")
        self.pushButton_teal.setIcon(icon1)
        self.pushButton_teal.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_teal.setObjectName("pushButton_teal")
        self.gridLayout.addWidget(self.pushButton_teal, 2, 4, 1, 1)
        self.pushButton_cyan = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_cyan.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_cyan.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_cyan.setFont(font)
        self.pushButton_cyan.setStyleSheet("QPushButton:!pressed{\n"
"    color: rgb(0, 255, 255);\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(0, 255, 255);\n"
"}")
        self.pushButton_cyan.setIcon(icon1)
        self.pushButton_cyan.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_cyan.setObjectName("pushButton_cyan")
        self.gridLayout.addWidget(self.pushButton_cyan, 1, 3, 1, 1)
        self.pushButton_purple = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_purple.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_purple.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_purple.setFont(font)
        self.pushButton_purple.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(128, 0, 128);\n"
"color: rgb(128, 0, 128);\n"
"}")
        self.pushButton_purple.setIcon(icon1)
        self.pushButton_purple.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_purple.setObjectName("pushButton_purple")
        self.gridLayout.addWidget(self.pushButton_purple, 2, 3, 1, 1)
        self.pushButton_green = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_green.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_green.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_green.setFont(font)
        self.pushButton_green.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"}")
        self.pushButton_green.setIcon(icon1)
        self.pushButton_green.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_green.setObjectName("pushButton_green")
        self.gridLayout.addWidget(self.pushButton_green, 0, 1, 1, 1)
        self.pushButton_silver = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_silver.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_silver.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_silver.setFont(font)
        self.pushButton_silver.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(192, 192, 192);\n"
"color: rgb(192, 192, 192);\n"
"}")
        self.pushButton_silver.setIcon(icon1)
        self.pushButton_silver.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_silver.setObjectName("pushButton_silver")
        self.gridLayout.addWidget(self.pushButton_silver, 3, 3, 1, 1)
        self.pushButton_black = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_black.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_black.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_black.setFont(font)
        self.pushButton_black.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_black.setIcon(icon1)
        self.pushButton_black.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_black.setObjectName("pushButton_black")
        self.gridLayout.addWidget(self.pushButton_black, 0, 3, 1, 1)
        self.pushButton_orange = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_orange.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_orange.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_orange.setFont(font)
        self.pushButton_orange.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(255, 165, 0);\n"
"    color: rgb(255, 165, 0);\n"
"}")
        self.pushButton_orange.setIcon(icon1)
        self.pushButton_orange.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_orange.setObjectName("pushButton_orange")
        self.gridLayout.addWidget(self.pushButton_orange, 3, 0, 1, 1)
        self.pushButton_pink = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_pink.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_pink.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_pink.setFont(font)
        self.pushButton_pink.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    color: rgb(255, 192, 203);\n"
"    background-color: rgb(255, 192, 203);\n"
"}")
        self.pushButton_pink.setIcon(icon1)
        self.pushButton_pink.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_pink.setObjectName("pushButton_pink")
        self.gridLayout.addWidget(self.pushButton_pink, 3, 1, 1, 1)
        self.pushButton_white = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_white.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_white.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_white.setFont(font)
        self.pushButton_white.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_white.setIcon(icon1)
        self.pushButton_white.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_white.setObjectName("pushButton_white")
        self.gridLayout.addWidget(self.pushButton_white, 0, 4, 1, 1)
        self.pushButton_bronze = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_bronze.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_bronze.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_bronze.setFont(font)
        self.pushButton_bronze.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(205, 127, 50);\n"
"color: rgb(205, 127, 50);\n"
"}")
        self.pushButton_bronze.setIcon(icon1)
        self.pushButton_bronze.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_bronze.setObjectName("pushButton_bronze")
        self.gridLayout.addWidget(self.pushButton_bronze, 3, 4, 1, 1)
        self.pushButton_maroon = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_maroon.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_maroon.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_maroon.setFont(font)
        self.pushButton_maroon.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    color: rgb(128, 0, 0);\n"
"    background-color:rgb(128, 0, 0);\n"
"}")
        self.pushButton_maroon.setIcon(icon1)
        self.pushButton_maroon.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_maroon.setObjectName("pushButton_maroon")
        self.gridLayout.addWidget(self.pushButton_maroon, 2, 1, 1, 1)
        self.pushButton_red = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_red.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_red.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_red.setFont(font)
        self.pushButton_red.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"    border:1px solid rgb(255, 255, 0);\n"
"    color: rgb(255, 0, 0);\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.pushButton_red.setIcon(icon1)
        self.pushButton_red.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_red.setObjectName("pushButton_red")
        self.gridLayout.addWidget(self.pushButton_red, 0, 0, 1, 1)
        self.pushButton_navy = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_navy.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_navy.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_navy.setFont(font)
        self.pushButton_navy.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(0, 0, 128);\n"
"    color: rgb(0, 0, 128);\n"
"}")
        self.pushButton_navy.setIcon(icon1)
        self.pushButton_navy.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_navy.setObjectName("pushButton_navy")
        self.gridLayout.addWidget(self.pushButton_navy, 2, 2, 1, 1)
        self.pushButton_magenta = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_magenta.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_magenta.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_magenta.setFont(font)
        self.pushButton_magenta.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(255, 0, 255);\n"
"    color:rgb(255, 0, 255);\n"
"}")
        self.pushButton_magenta.setIcon(icon1)
        self.pushButton_magenta.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_magenta.setObjectName("pushButton_magenta")
        self.gridLayout.addWidget(self.pushButton_magenta, 1, 2, 1, 1)
        self.pushButton_gray = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_gray.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_gray.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_gray.setFont(font)
        self.pushButton_gray.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(128, 128, 128);\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.pushButton_gray.setIcon(icon1)
        self.pushButton_gray.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_gray.setObjectName("pushButton_gray")
        self.gridLayout.addWidget(self.pushButton_gray, 1, 0, 1, 1)
        self.pushButton_gold = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_gold.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_gold.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_gold.setFont(font)
        self.pushButton_gold.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(255, 215, 0);\n"
"color: rgb(255, 215, 0);\n"
"}")
        self.pushButton_gold.setIcon(icon1)
        self.pushButton_gold.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_gold.setObjectName("pushButton_gold")
        self.gridLayout.addWidget(self.pushButton_gold, 3, 2, 1, 1)
        self.pushButton_olive = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_olive.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_olive.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_olive.setFont(font)
        self.pushButton_olive.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(128, 128, 0);\n"
"    color:rgb(128, 128, 0);\n"
"}")
        self.pushButton_olive.setIcon(icon1)
        self.pushButton_olive.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_olive.setObjectName("pushButton_olive")
        self.gridLayout.addWidget(self.pushButton_olive, 2, 0, 1, 1)
        self.pushButton_blue = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_blue.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_blue.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_blue.setFont(font)
        self.pushButton_blue.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(0, 0, 255);\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_blue.setIcon(icon1)
        self.pushButton_blue.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_blue.setObjectName("pushButton_blue")
        self.gridLayout.addWidget(self.pushButton_blue, 0, 2, 1, 1)
        self.pushButton_yellow = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_yellow.setMinimumSize(QtCore.QSize(31, 28))
        self.pushButton_yellow.setMaximumSize(QtCore.QSize(31, 27))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_yellow.setFont(font)
        self.pushButton_yellow.setStyleSheet("QPushButton:!pressed{\n"
"    border-radius:5px;\n"
"border:1px solid rgb(255, 255, 0);\n"
"    background-color: rgb(255, 255, 0);color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.pushButton_yellow.setIcon(icon1)
        self.pushButton_yellow.setIconSize(QtCore.QSize(2, 2))
        self.pushButton_yellow.setObjectName("pushButton_yellow")
        self.gridLayout.addWidget(self.pushButton_yellow, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choose color"))
        self.pushButton_brown.setToolTip(_translate("Dialog", "brown"))
        self.pushButton_brown.setText(_translate("Dialog", "brown"))
        self.pushButton_teal.setToolTip(_translate("Dialog", "teal"))
        self.pushButton_teal.setText(_translate("Dialog", "teal"))
        self.pushButton_cyan.setToolTip(_translate("Dialog", "cyan"))
        self.pushButton_cyan.setText(_translate("Dialog", "cyan"))
        self.pushButton_purple.setToolTip(_translate("Dialog", "purple"))
        self.pushButton_purple.setText(_translate("Dialog", "purple"))
        self.pushButton_green.setToolTip(_translate("Dialog", "green"))
        self.pushButton_green.setText(_translate("Dialog", "green"))
        self.pushButton_silver.setToolTip(_translate("Dialog", "silver"))
        self.pushButton_silver.setText(_translate("Dialog", "silver"))
        self.pushButton_black.setToolTip(_translate("Dialog", "black"))
        self.pushButton_black.setText(_translate("Dialog", "black"))
        self.pushButton_orange.setToolTip(_translate("Dialog", "orange"))
        self.pushButton_orange.setText(_translate("Dialog", "orange"))
        self.pushButton_pink.setToolTip(_translate("Dialog", "pink"))
        self.pushButton_pink.setText(_translate("Dialog", "pink"))
        self.pushButton_white.setToolTip(_translate("Dialog", "white"))
        self.pushButton_white.setText(_translate("Dialog", "white"))
        self.pushButton_bronze.setToolTip(_translate("Dialog", "bronze"))
        self.pushButton_bronze.setText(_translate("Dialog", "bronze"))
        self.pushButton_maroon.setToolTip(_translate("Dialog", "maroon"))
        self.pushButton_maroon.setText(_translate("Dialog", "maroon"))
        self.pushButton_red.setToolTip(_translate("Dialog", "red"))
        self.pushButton_red.setText(_translate("Dialog", "red"))
        self.pushButton_navy.setToolTip(_translate("Dialog", "navy"))
        self.pushButton_navy.setText(_translate("Dialog", "navy"))
        self.pushButton_magenta.setToolTip(_translate("Dialog", "magenta"))
        self.pushButton_magenta.setText(_translate("Dialog", "magenta"))
        self.pushButton_gray.setToolTip(_translate("Dialog", "gray"))
        self.pushButton_gray.setText(_translate("Dialog", "gray"))
        self.pushButton_gold.setToolTip(_translate("Dialog", "gold"))
        self.pushButton_gold.setText(_translate("Dialog", "gold"))
        self.pushButton_olive.setToolTip(_translate("Dialog", "olive"))
        self.pushButton_olive.setText(_translate("Dialog", "olive"))
        self.pushButton_blue.setToolTip(_translate("Dialog", "blue"))
        self.pushButton_blue.setText(_translate("Dialog", "blue"))
        self.pushButton_yellow.setToolTip(_translate("Dialog", "yellow"))
        self.pushButton_yellow.setText(_translate("Dialog", "yellow"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton.setShortcut(_translate("Dialog", "Return"))
import Icons_rc
