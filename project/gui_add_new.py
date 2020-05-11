# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tmp\gui_add_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_add_new(object):
    def setupUi(self, Dialog_add_new):
        Dialog_add_new.setObjectName("Dialog_add_new")
        Dialog_add_new.resize(408, 128)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_add_new)
        self.buttonBox.setGeometry(QtCore.QRect(214, 90, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_name_ru = QtWidgets.QLineEdit(Dialog_add_new)
        self.lineEdit_name_ru.setGeometry(QtCore.QRect(154, 60, 211, 21))
        self.lineEdit_name_ru.setObjectName("lineEdit_name_ru")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog_add_new)
        self.lineEdit_name.setGeometry(QtCore.QRect(154, 20, 211, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtWidgets.QLabel(Dialog_add_new)
        self.label_name.setGeometry(QtCore.QRect(30, 20, 131, 21))
        self.label_name.setObjectName("label_name")
        self.label_name_ru = QtWidgets.QLabel(Dialog_add_new)
        self.label_name_ru.setGeometry(QtCore.QRect(30, 60, 111, 21))
        self.label_name_ru.setObjectName("label_name_ru")

        self.retranslateUi(Dialog_add_new)
        self.buttonBox.accepted.connect(Dialog_add_new.accept)
        self.buttonBox.rejected.connect(Dialog_add_new.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_add_new)

    def retranslateUi(self, Dialog_add_new):
        _translate = QtCore.QCoreApplication.translate
        Dialog_add_new.setWindowTitle(_translate("Dialog_add_new", "Добавить"))
        self.label_name.setText(_translate("Dialog_add_new", "Название на английском"))
        self.label_name_ru.setText(_translate("Dialog_add_new", "Название на русском"))
