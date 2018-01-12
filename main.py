#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import QImage, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFontComboBox, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore
from time import time
from os import walk, path
from ntpath import basename

from network.network import Network
from school import School
from ui.main_window import Ui_MainWindow

from random import randint


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.generateImage)
        self.ui.pushButton_2.clicked.connect(self.generate_random_image)
        self.ui.pushButton_3.clicked.connect(self.update_images_table)

        self.network = Network()
        self.school = School(self.network)

    def generate_random_image(self):
        current_font = self.ui.fontComboBox.currentFont()
        length = self.ui.fontComboBox.count()
        count = 12
        for x in range(0, count):
            self.ui.fontComboBox.setCurrentIndex(randint(0, length))
            font = self.ui.fontComboBox.currentFont()
            self.school.generate_random_image(font)
        self.ui.fontComboBox.setFont(current_font)


    def update_images_table(self):
        table = self.ui.tableWidget
        files = self.school.get_images()
        print(files)
        table.setColumnCount(3)
        table.setRowCount(len(files))
        table.setHorizontalHeaderLabels(['Letter', 'File', 'Result'])
        #table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        #table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        #table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        for i, f in enumerate(files):
            name = basename(f)
            print([name.split('.')[0], name, ''])
            table.setItem(i, 0, QTableWidgetItem(name.split('.')[0]))
            table.setItem(i, 1, QTableWidgetItem(name))
            table.setItem(i, 2, QTableWidgetItem(''))
            item = table.itemAt(i, 0)
        table.resizeColumnsToContents()
        table.itemDoubleClicked.connect(self.letter_double_click)
        pass

    def letter_double_click(self, item):
        print('doubleclick')
        print(item)

    def generateImage(self):
        """
        :var QString letters
        :return:
        """
        letters = self.ui.lineEdit.displayText()

        # :var QFont
        self.generate_random_images(12)
        pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = Window()
    App.show()
    sys.exit(app.exec_())
