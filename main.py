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
        self.ui.lineEdit_2.setText('12')
        self.ui.pushButton.clicked.connect(self.generateImage)
        self.ui.pushButton_2.clicked.connect(self.generate_random_image)
        self.ui.pushButton_3.clicked.connect(self.update_images_table)
        self.ui.pushButton_4.clicked.connect(self.start_study)
        self.ui.pushButton_5.clicked.connect(self.save_network)
        self.ui.pushButton_6.clicked.connect(self.load_network)

        self.network = Network()
        self.school = School(self.network)

    def save_network(self):
        self.school.network.save_to_file()

    def load_network(self):
        self.school.network.load_from_file()

    def generate_random_image(self):
        current_font = self.ui.fontComboBox.currentFont()
        length = self.ui.fontComboBox.count()
        try:
            count = int(self.ui.lineEdit_2.text())
        except ValueError:
            count = 12
        for x in range(0, count):
            self.ui.fontComboBox.setCurrentIndex(randint(0, length))
            font = self.ui.fontComboBox.currentFont()
            self.school.generate_random_image(font)
        self.ui.fontComboBox.setFont(current_font)
        self.update_images_table()


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
        letterCell = self.ui.tableWidget.item(item.row(), 0)
        print('Letter: '+letterCell.text())
        f = self.ui.tableWidget.item(item.row(), 1)
        file_name = f.text()
        image_path = path.join(self.school.imagesDir, file_name)
        image_file = open(image_path, 'rb')
        image_content = image_file.read()
        qImage = QImage()
        qImage.loadFromData(image_content)
        network = self.school.network
        image_data = network.read_image(qImage)

        network_answer = network.get_answer(image_data)
        print('Network thinks that is '+network_answer[1]+' '+str(network_answer[0]))




    def generateImage(self):
        """
        :var QString letters
        """
        letters = self.ui.lineEdit.displayText()
        letters = list(letters)
        font = self.ui.fontComboBox.currentFont()
        for x in letters:
            self.school.generateImage(x, font)
        self.update_images_table()

    def start_study(self):
        table = self.ui.tableWidget
        for y in range(0, 100):
            for x in range(0, table.rowCount()):
                # letter = table.item(x, 0)
                image_name = table.item(x, 1).text()
                self.school.study(image_name)
                # print(letter.text())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = Window()
    App.show()
    sys.exit(app.exec_())
