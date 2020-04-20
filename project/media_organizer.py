import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets

from gui_main_window import Ui_Dialog as Design
from database import MediaDB


def get_film_info(func):
    def check_film_info(func_arg1, func_arg12, checkBox_our_lib):
        print()
        films = func_arg12.get_films()
        film_info = func_arg12.get_film_info(films[func_arg1])
        func(func_arg1, func_arg12, checkBox_our_lib)
        print(film_info)
        if film_info[0][1] is True:
            checkBox_our_lib.setChecked(True)
        else:
            checkBox_our_lib.setChecked(False)
    return check_film_info


@get_film_info
def clicked_event(film, database, checkBox_our_lib):
    films = database.get_films()
    if film:
        print(films[film])


class MediaOrganizer(QtWidgets.QMainWindow, Design):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.database = MediaDB()
        self.fill_library()
        self.listWidget_library.itemClicked.connect(self.library_item_clicked_event)

        # self.checkBox_our_lib.setChecked(True)

    def fill_library(self):
        films = self.database.get_films()
        self.listWidget_library.addItems(films.keys())

    def library_item_clicked_event(self):
        film = self.listWidget_library.currentItem().text()

        clicked_event(film, self.database, self.checkBox_our_lib)

    def accept(self):
        print('OK')

    def reject(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MediaOrganizer()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
