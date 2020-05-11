import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from gui_add_new import Ui_Dialog_add_new as Design
# from media_organizer import MediaOrganizer


class AddNew(QtWidgets.QMainWindow, Design):
    def __init__(self, type_to_add):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.type_to_add = type_to_add

    def accept(self):
        name = self.lineEdit_name.text()
        name_ru = self.lineEdit_name_ru.text()

        if self.type_to_add == 'libraries':
            r = requests.post('http://127.0.0.1:5000/api/v1/libraries',
                              {'name': name, 'name_ru': name_ru})
            # MediaOrganizer.libraries()
        elif self.type_to_add == 'categories':
            r = requests.post('http://127.0.0.1:5000/api/v1/categories',
                              {'name': name, 'name_ru': name_ru})

    def reject(self):
        self.close()
