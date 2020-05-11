import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets

from gui_main_window import Ui_Dialog as Design
from database import MediaDB


class MediaOrganizer(QtWidgets.QMainWindow, Design):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.database = MediaDB()
        self.videos = self.database.get_videos()

        self.fill_library()

        self.video_index = None
        print(self.video_index)

        self.listWidget_library.itemClicked.connect(self.library_item_clicked_event)
        self.checkBox_autosave.stateChanged.connect(self.set_auto_save)
        self.pushButton_save.clicked.connect(self.change_video_info)

    def fill_library(self):
        self.listWidget_library.addItems(self.videos.values())

    def library_item_clicked_event(self):
        self.video_index = self.listWidget_library.currentRow()
        video_info = self.database.get_video_info(list(self.videos)[self.video_index])
        if video_info[1] is True:
            self.checkBox_our_lib.setChecked(True)
        else:
            self.checkBox_our_lib.setChecked(False)

        if video_info[2] is True:
            self.checkBox_moms_lib.setChecked(True)
        else:
            self.checkBox_moms_lib.setChecked(False)

        if video_info[3] == 1:
            self.radioButton_serial.setChecked(True)
        elif video_info[3] == 2:
            self.radioButton_film.setChecked(True)
        elif video_info[3] == 3:
            self.radioButton_anime.setChecked(True)

        print(video_info)

    def set_auto_save(self):
        if self.checkBox_autosave.isChecked():
            self.pushButton_save.setHidden(True)
        else:
            self.pushButton_save.setHidden(False)

    def change_video_info(self):
        # database.change_row('1820', name='ljlh111h', our_lib='false')
        if self.checkBox_our_lib.isChecked():
            our_lib = 'true'
        else:
            our_lib = 'false'
            
        if self.checkBox_moms_lib.isChecked():
            moms_lib = 'true'
        else:
            moms_lib = 'false'

        if self.radioButton_serial.isChecked():
            categories_id = 1
        elif self.radioButton_film.isChecked():
            categories_id = 2
        elif self.radioButton_anime.isChecked():
            categories_id = 3
            
        self.database.change_row(
            list(self.videos)[self.video_index],
            our_lib=our_lib,
            moms_lib=moms_lib,
            categories_id=categories_id
        )

    def rename_video(self):
        # TODO добавить проверку имени на наличие дубликатов
        pass
        
        print(list(self.videos)[self.video_index])


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MediaOrganizer()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
