import requests
from PyQt5 import QtWidgets

from gui_add_new import Ui_Dialog_add_new as Design
from logs.log_config import logger


class AddNew(QtWidgets.QMainWindow, Design):
    def __init__(self, parent, type_to_add):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.parent = parent
        self.type_to_add = type_to_add

        if self.type_to_add == 'libraries':
            self.setWindowTitle("Добавить библиотеку")
        elif self.type_to_add == 'categories':
            self.setWindowTitle("Добавить категорию")

    def accept(self):
        name = self.lineEdit_name.text()
        name_ru = self.lineEdit_name_ru.text()

        if self.type_to_add == 'libraries' and name and name_ru:
            r = requests.post('http://127.0.0.1:5000/api/v1/libraries',
                              {'name': name, 'name_ru': name_ru})

            if r.status_code == 200:
                self.parent.refresh_layout(self.type_to_add)
            else:
                logger.error(r)

        elif self.type_to_add == 'categories' and name and name_ru:
            r = requests.post('http://127.0.0.1:5000/api/v1/categories',
                              {'name': name, 'name_ru': name_ru})

            if r.status_code == 200:
                self.parent.refresh_layout(self.type_to_add)
            else:
                logger.error(r)

        self.close()

    def reject(self):
        self.close()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AddNew('libraries')  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
