# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_main_window.ui'
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
        self.checkBox_our_lib = QtWidgets.QCheckBox(Dialog)
        self.checkBox_our_lib.setGeometry(QtCore.QRect(310, 186, 121, 21))
        self.checkBox_our_lib.setObjectName("checkBox_our_lib")
        self.checkBox_moms_lib = QtWidgets.QCheckBox(Dialog)
        self.checkBox_moms_lib.setGeometry(QtCore.QRect(310, 210, 121, 21))
        self.checkBox_moms_lib.setObjectName("checkBox_moms_lib")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(460, 160, 120, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_serial = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_serial.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_serial.setObjectName("radioButton_serial")
        self.radioButton_film = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_film.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton_film.setObjectName("radioButton_film")
        self.radioButton_anime = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_anime.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_anime.setObjectName("radioButton_anime")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(440, 442, 151, 31))
        self.pushButton_save.setObjectName("pushButton_save")
        self.checkBox_autosave = QtWidgets.QCheckBox(Dialog)
        self.checkBox_autosave.setGeometry(QtCore.QRect(480, 10, 101, 31))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Media Organizer"))
        self.checkBox_our_lib.setText(_translate("Dialog", "наша библиотека"))
        self.checkBox_moms_lib.setText(_translate("Dialog", "мамина библиотека"))
        self.groupBox_2.setTitle(_translate("Dialog", "Категория"))
        self.radioButton_serial.setText(_translate("Dialog", "Сериал"))
        self.radioButton_film.setText(_translate("Dialog", "Фильм"))
        self.radioButton_anime.setText(_translate("Dialog", "Анимэ"))
        self.pushButton_save.setText(_translate("Dialog", "Сохранить"))
        self.checkBox_autosave.setText(_translate("Dialog", "Автосохранение"))
        self.pushButton.setText(_translate("Dialog", "Переименовать"))
