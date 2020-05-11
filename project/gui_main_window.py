# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project\gui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 490)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(430, 440, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listWidget_library = QtWidgets.QListWidget(Dialog)
        self.listWidget_library.setGeometry(QtCore.QRect(10, 40, 256, 431))
        self.listWidget_library.setObjectName("listWidget_library")
        self.checkBox_our_lib = QtWidgets.QCheckBox(Dialog)
        self.checkBox_our_lib.setGeometry(QtCore.QRect(310, 190, 70, 17))
        self.checkBox_our_lib.setObjectName("checkBox_our_lib")
        self.checkBox_moms_lib = QtWidgets.QCheckBox(Dialog)
        self.checkBox_moms_lib.setGeometry(QtCore.QRect(310, 210, 70, 17))
        self.checkBox_moms_lib.setObjectName("checkBox_moms_lib")
        self.checkBox_serial = QtWidgets.QCheckBox(Dialog)
        self.checkBox_serial.setGeometry(QtCore.QRect(410, 190, 70, 17))
        self.checkBox_serial.setObjectName("checkBox_serial")
        self.checkBox_film = QtWidgets.QCheckBox(Dialog)
        self.checkBox_film.setGeometry(QtCore.QRect(410, 210, 70, 17))
        self.checkBox_film.setObjectName("checkBox_film")
        self.checkBox_anime = QtWidgets.QCheckBox(Dialog)
        self.checkBox_anime.setGeometry(QtCore.QRect(410, 230, 70, 17))
        self.checkBox_anime.setObjectName("checkBox_anime")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox_our_lib.setText(_translate("Dialog", "CheckBox"))
        self.checkBox_moms_lib.setText(_translate("Dialog", "CheckBox"))
        self.checkBox_serial.setText(_translate("Dialog", "Сериал"))
        self.checkBox_film.setText(_translate("Dialog", "Фильм"))
        self.checkBox_anime.setText(_translate("Dialog", "Анимэ"))
