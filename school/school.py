#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path, mkdir, unlink, walk

from PyQt5.QtGui import QImage, QPainter, QColor, qRgb, QFont
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
        self.supported_symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-/*_|@#$%^&)({}[]!?.,'
        pass

    def __del__(self):
        if self.clearDataAfterClose:
            for f in self.files:
                absPath = self.dir + '/' + f
                print(absPath)
                unlink(absPath)

    def generate_random_image(self, font):
        letter = self.supported_symbols[randint(0, len(self.supported_symbols) - 1)]
        font = QFont(font)
        return self.generateImage(letter, font)

    def generateImage(self, letter, font):
        image = QImage(30, 30, QImage.Format_ARGB32_Premultiplied)
        image.fill(QColor(255, 255, 255, 255))
        painter = QPainter(image)
        painter.setPen(QColor(0, 0, 0, 255))
        painter.setFont(font)
        rect = image.rect()
        painter.drawText(rect, QtCore.Qt.AlignCenter, letter)
        painter.end()

        filename = letter + '.' + str(time()) + str(randint(0, 1000)) + '.png'
        p = path.join(self.imagesDir, filename)
        image.save(path.join(self.imagesDir, filename))
        # self.files.append(path.join(self.imagesDirName, filename))
        return path.join(self.imagesDir, filename)

    def study(self, image):
        image_path = path.join(self.imagesDir, image)
        letter = image.split('.')[0]
        if letter not in self.network.neurons:
            self.network.add_neuron(letter)
        image_file = open(image_path, 'rb')
        image_content = image_file.read()
        qImage = QImage()
        qImage.loadFromData(image_content)
        image_data = self.network.read_image(qImage)
        return self.network.study(image_data, letter)

        # print(letter)
        # print(image_path)

    @staticmethod
    def get_images():
        p = path.dirname(__file__) + '/images'
        files = []
        for (dirpath, dirnames, filenames) in walk(p):
            files += map(lambda f: dirpath + '/' + f, filenames)
        return files
