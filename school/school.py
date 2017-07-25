#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path, mkdir, unlink

from PyQt5.QtGui import QImage, QPainter, QColor, qRgb
from PyQt5 import QtCore
from time import time
from random import randint


class School:
    def __init__(self, network):
        """
        :param network:
        """
        self.network = network
        self.dir = path.dirname(__file__)
        self.imagesDirName = 'images'
        self.imagesDir = path.join(self.dir, self.imagesDirName)
        if not path.exists(self.imagesDir):
            mkdir(self.imagesDir, 0o755)

        self.clearDataAfterClose = True
        self.files = []
        pass

    def __del__(self):
        if self.clearDataAfterClose:
            for f in self.files:
                absPath = self.dir + '/' + f
                print(absPath)
                unlink(absPath)

    def generateImage(self, letter, font):
        image = QImage(30, 30, QImage.Format_ARGB32_Premultiplied)

        image.fill(QColor(255, 255, 255, 255))
        painter = QPainter(image)
        painter.setPen(QColor(0, 0, 0, 255))
        painter.setFont(font)
        rect = image.rect()
        painter.drawText(rect, QtCore.Qt.AlignCenter, letter.text())
        painter.end()

        filename = letter.text()+'.'+str(time()) + str(randint(0, 1000)) + '.png'
        image.save(path.join(self.imagesDir, filename))
        self.files.append(path.join(self.imagesDirName, filename))
        return path.join(self.imagesDir, filename)


    #def handle(self):

