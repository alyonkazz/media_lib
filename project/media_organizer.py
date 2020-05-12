import json
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import requests
import transliterate
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets

from add_new import AddNew
from gui_add_new import Ui_Dialog_add_new
from gui_main_window import Ui_Dialog as Design


class MediaOrganizer(QtWidgets.QMainWindow, Design):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.videos = self.api_get_request()

        self.fill_library()

        self.video_index = None

        # self.listWidget_library.itemClicked.connect(self.library_item_clicked_event)
        self.checkBox_autosave.stateChanged.connect(self.set_auto_save)
        # self.pushButton_save.clicked.connect(self.save_video_info_changes)
        self.pushButton.clicked.connect(self.rename_video)

        # self.button = QtGui.QPushButton('', self)
        # self.button.clicked.connect(self.handleButton)

        # self.pushButton.setIcon(QIcon('static/add.png'))

        self.menu()
        self.libraries()
        self.categories()

    def menu(self):

        exit_action = QAction(QIcon('static/exit24.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        settings_action = QAction(QIcon('static/setting.png'), 'Настройки', self)
        settings_action.setShortcut('Ctrl+N')
        settings_action.setStatusTip('Настройки приложения')
        settings_action.triggered.connect(self.menu_settings)

        # self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(settings_action)
        file_menu.addAction(exit_action)

        # toolbar = self.addToolBar('Exit')
        # toolbar.addAction(exitAction)

    def menu_settings(self):
        pass

    def libraries(self):
        libraries_r = requests.get('http://127.0.0.1:5000/api/v1/libraries')
        libraries_json = libraries_r.json()
        checkBox_height_basic = 156
        checkBox_height_step = 24

        if libraries_json:
            for library in [libraries_json['all_libraries'][i]['name_ru']
                            for i in range(len(libraries_json['all_libraries']))]:
                checkBox_height_basic = checkBox_height_basic + checkBox_height_step

                checkBox = QtWidgets.QCheckBox(library, self)
                checkBox.setGeometry(QtCore.QRect(310, checkBox_height_basic, 121, 21))
                # checkBox.setObjectName("checkBox_moms_lib")

        btn_add_new_library = QtWidgets.QPushButton("Добавить\nбиблиотеку", self)
        btn_add_new_library.setGeometry(QtCore.QRect(310, checkBox_height_basic + checkBox_height_step, 121, 42))
        # TODO добавить расстояние между иконкой и текстом
        btn_add_new_library.setIcon(QIcon('static/add.png'))
        btn_add_new_library.clicked.connect(self.add_new_library)

    def categories(self):
        categories_r = requests.get('http://127.0.0.1:5000/api/v1/categories')
        categories_json = categories_r.json()
        checkBox_height_basic = 20
        checkBox_height_step = 20

        if categories_json:
            for category in [categories_json['all_categories'][i]['name_ru']
                             for i in range(len(categories_json['all_categories']))]:
                checkBox_height_basic = checkBox_height_basic + checkBox_height_step

                radioButton = QtWidgets.QRadioButton(category, self.groupBox_2)
                radioButton.setGeometry(QtCore.QRect(10, checkBox_height_basic, 82, 17))
                # radioButton.setObjectName("radioButton_serial")

        btn_add_new_category = QtWidgets.QPushButton("Добавить\nкатегорию", self)
        btn_add_new_category.setGeometry(QtCore.QRect(460, checkBox_height_basic + checkBox_height_step, 121, 42))
        # TODO добавить расстояние между иконкой и текстом
        btn_add_new_category.setIcon(QIcon('static/add.png'))
        btn_add_new_category.clicked.connect(self.add_new_category)

    def add_new_library(self):
        self.win_add = AddNew('libraries')
        self.win_add.show()

    def add_new_category(self):
        self.win_add = AddNew('categories')
        self.win_add.show()

    def api_get_request(self, *args, **kwargs):
        if kwargs.items():
            for k, v in kwargs.items():
                r = requests.get('http://127.0.0.1:5000/api/v1/media', {k: v})
                return r.json()
        else:
            r = requests.get('http://127.0.0.1:5000/api/v1/media')
            return r.json()

    def api_put_request(self, video_id, changes_dict):
        changes_str = json.dumps(changes_dict)
        r = requests.put('http://127.0.0.1:5000/api/v1/media', {'video_id': video_id, 'changes_dict': changes_str})

    def fill_library(self):
        self.listWidget_library.addItems(self.videos.values())

    # def library_item_clicked_event(self):
    #     self.video_index = self.listWidget_library.currentRow()
    #     video_info = self.api_get_request(video_id=list(self.videos)[self.video_index])
    #     if video_info[1] is True:
    #         self.checkBox_our_lib.setChecked(True)
    #     else:
    #         self.checkBox_our_lib.setChecked(False)
    #
    #     if video_info[2] is True:
    #         self.checkBox_moms_lib.setChecked(True)
    #     else:
    #         self.checkBox_moms_lib.setChecked(False)
    #
    #     if video_info[3] == 1:
    #         self.radioButton_serial.setChecked(True)
    #     elif video_info[3] == 2:
    #         self.radioButton_film.setChecked(True)
    #     elif video_info[3] == 3:
    #         self.radioButton_anime.setChecked(True)

    def set_auto_save(self):
        if self.checkBox_autosave.isChecked():
            self.pushButton_save.setHidden(True)
        else:
            self.pushButton_save.setHidden(False)

    # def save_video_info_changes(self):
    #     if self.checkBox_our_lib.isChecked():
    #         our_lib = 'true'
    #     else:
    #         our_lib = 'false'
    #
    #     if self.checkBox_moms_lib.isChecked():
    #         moms_lib = 'true'
    #     else:
    #         moms_lib = 'false'
    #
    #     if self.radioButton_serial.isChecked():
    #         categories_id = 1
    #     elif self.radioButton_film.isChecked():
    #         categories_id = 2
    #     elif self.radioButton_anime.isChecked():
    #         categories_id = 3
    #
    #     changes_dict = {
    #         'our_lib': our_lib,
    #         'moms_lib': moms_lib,
    #         'categories_id': categories_id
    #     }
    #     self.api_put_request(list(self.videos)[self.video_index], changes_dict)

    def rename_video(self):
        # TODO добавить проверку имени на наличие дубликатов
        changes_dict = {
            'name': '777',
            'our_lib': 'false',
            'moms_lib': 'false',
            'categories_id': '2'
        }
        self.api_put_request(list(self.videos)[self.video_index], changes_dict)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MediaOrganizer()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
