#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import QImage, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from time import time

from network.network import Network
from school import School
from ui.main_window import Ui_MainWindow


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generateImage)
        self.network = Network()
        self.school = School(self.network)

    def generateImage(self):
        """
        :var QString letters
        :return:
        """
        letters = self.ui.lineEdit.displayText()

        # :var QFont
        font = self.ui.fontComboBox.currentFont()
        font.setPointSize(15)
        for x in letters:
            self.school.generateImage(x, font)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = Window()
    App.show()
    sys.exit(app.exec_())
