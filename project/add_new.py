from PyQt5 import QtCore, QtGui, QtWidgets
from gui_add_new import Ui_Dialog_add_new as Design


class AddNew(QtWidgets.QMainWindow, Design):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

    def accept(self):
        pass

    def reject(self):
        pass
