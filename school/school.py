#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path, mkdir, unlink

from PyQt5.QtGui import QImage, QPainter, QColor
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

        self.clearDataAfterClose = False
        self.files = []
        pass

    def __del__(self):
        if self.clearDataAfterClose:
            for f in self.files:
                absPath = self.dir + '/' + f
                print(absPath)
                unlink(absPath)

    def generateImage(self, letter, font):
        image = QImage(30, 30, QImage.Format_Alpha8)
        image.fill(QtCore.Qt.transparent)
        painter = QPainter(image)
        painter.setPen(QColor('black'))
        painter.setFont(font)
        painter.drawText(image.rect(), QtCore.Qt.AlignCenter, letter)
        painter.end()
        filename = letter+'.'+str(time()) + str(randint(0, 1000)) + '.png'
        image.save(path.join(self.imagesDir, filename))
        self.files.append(path.join(self.imagesDirName, filename))
        return path.join(self.imagesDir, filename)

    #def handle(self):

