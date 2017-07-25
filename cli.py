#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from time import time

from PyQt5.QtGui import QFont, QStaticText
from PyQt5.QtWidgets import QApplication

from main import Window
from network.network import Network
from school import School
from random import randint
import cv2
from PIL import Image, ImageDraw, ImageFont
import _pickle as cPickle
from os import path
app = QApplication(sys.argv)
App = Window()

img = Image.new('RGBA', (30, 30), (255, 255, 255, 255))
if path.exists('data.p'):
    network = cPickle.load(open('data.p', 'rb'))
else:
    network = Network()
school = School(network)
school.clearDataAfterClose = False

for x in range(0, 40):
    font = QFont('Ubuntu', 15)
    number = randint(0, 10)
    text = QStaticText(str(number))
    print('study '+str(number), network.neurons)
    imagePath = school.generateImage(text, font)
    image = Image.open(imagePath)
    input = network.read_image(image)

    network.study(input, number)

cPickle.dump(network, open('data.p', 'wb'))