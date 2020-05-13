# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tmp\gui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 490)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        Dialog.setBaseSize(QtCore.QSize(0, 0))
        self.listWidget_library = QtWidgets.QListWidget(Dialog)
        self.listWidget_library.setGeometry(QtCore.QRect(10, 40, 256, 431))
        self.listWidget_library.setObjectName("listWidget_library")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(440, 442, 151, 31))
        self.pushButton_save.setObjectName("pushButton_save")
        self.checkBox_autosave = QtWidgets.QCheckBox(Dialog)
        self.checkBox_autosave.setGeometry(QtCore.QRect(490, 30, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_autosave.sizePolicy().hasHeightForWidth())
        self.checkBox_autosave.setSizePolicy(sizePolicy)
        self.checkBox_autosave.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_autosave.setSizeIncrement(QtCore.QSize(0, 0))
        self.checkBox_autosave.setBaseSize(QtCore.QSize(0, 0))
        self.checkBox_autosave.setIconSize(QtCore.QSize(25, 25))
        self.checkBox_autosave.setObjectName("checkBox_autosave")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 400, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(470, 160, 121, 151))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_cats_main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_cats_main.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_cats_main.setObjectName("verticalLayout_cats_main")
        self.groupBox_cats = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_cats.setObjectName("groupBox_cats")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_cats)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 101, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_cats = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_cats.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_cats.setObjectName("verticalLayout_cats")
        self.verticalLayout_cats_main.addWidget(self.groupBox_cats)
        self.pushButton_add_cat = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_add_cat.setObjectName("pushButton_add_cat")
        self.verticalLayout_cats_main.addWidget(self.pushButton_add_cat)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 160, 160, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_add_lib = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_add_lib.setObjectName("pushButton_add_lib")
        self.gridLayout.addWidget(self.pushButton_add_lib, 1, 0, 1, 1)
        self.groupBox_libs = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_libs.setObjectName("groupBox_libs")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_libs)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 121, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_libs = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_libs.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_libs.setObjectName("verticalLayout_libs")
        self.gridLayout.addWidget(self.groupBox_libs, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Media Organizer"))
        self.pushButton_save.setText(_translate("Dialog", "Сохранить"))
        self.checkBox_autosave.setText(_translate("Dialog", "Автосохранение"))
        self.pushButton.setText(_translate("Dialog", "Переименовать"))
        self.groupBox_cats.setTitle(_translate("Dialog", "Категории"))
        self.pushButton_add_cat.setText(_translate("Dialog", "Добавить\n"
"категорию"))
        self.pushButton_add_lib.setText(_translate("Dialog", "Добавить\n"
"библиотеку"))
        self.groupBox_libs.setTitle(_translate("Dialog", "Библиотеки"))
