#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

from PyQt5.QtGui import qRgb, QColor

from network.neuron import Neuron
import _pickle as cPickle
from os import path


class Network(object):

    default_symbols = '0123456789'

    default_save_file = 'data.p'

    def __init__(self, memory_file=default_save_file):
        self.dir = path.dirname(__file__)
        self.default_options = ['neurons', 'neuronWidth', 'neuronHeight', 'neuronMinimum']
        self.neurons = {}
        self.neuronWidth = 30
        self.neuronHeight = 30
        self.neuronMinimum = 10000

        self.memory_file = memory_file
        self.load()

    def read_image(self, image):
        pixel_map = []
        for r in range(0, self.neuronHeight):
            pixel_map.append([])
            for c in range(0, self.neuronWidth):
                pixel_data = image.pixel(r, c)
                pixel_data = pixel_data - int('0xff000000', 16)
                # pixel_color = QColor(pixel_data)
                # print(pixel_color.red(), pixel_color.green(), pixel_color.blue(), pixel_color.alpha())
                # pixel_map[r].append(pixel_data[0] + pixel_data[1] + pixel_data[2])
                pixel_map[r].append(pixel_data)
        return pixel_map

    def handle_hard(self, input):
        output = []
        neurons = self.neurons.items()  # type: List[Neuron]
        for neuron in neurons:
            print(neuron)
            output.append(neuron.transfer_hard(input))
        return output

    def handle(self, input):
        output = []
        neurons = self.neurons.items()  # type: List[Neuron]
        for neuron in neurons:
            output.append(neuron.transfer(input))
        return output

    def study1(self, input, correctAnswer):
        self.neurons[correctAnswer] = 1
        correctOutput = []


        output = self.handle_hard(input)
        while not self.compare_array(correctOutput, output):
            for x in range(0, len(self.neurons)):
                dif = correctOutput[x] - output[x]
                self.neurons[x].change_weight(input, dif)
            output = self.handle_hard(input)

    def study(self, image_data, correct_answer):
        answer = self.get_answer(image_data)
        self.neurons[answer[1]].change_weight(image_data, -0.002 if answer[1] != correct_answer else 0.005)
        return True
        for letter in self.neurons:
            neuron = self.neurons[letter]
            if correct_answer == letter:
                e = ''
            try:
                neuron_result = neuron.transfer(image_data)
            except OverflowError:
                print(letter, correct_answer)
            if neuron_result == 1 and letter != correct_answer:
                neuron.change_weight(image_data, -0.0002)
            if neuron_result != 1 and letter == correct_answer:
                neuron.change_weight(image_data, 0.0005)
            #print(neuron.weight)
            # print(neuron)

    def get_answer(self, image_data):
        result = []
        letters = []
        for letter in self.neurons:
            neuron = self.neurons[letter]
            letters.append(letter)
            result.append(abs(neuron.transfer(image_data)))
        max_item = max(result)
        result_letter = letters[result.index(max_item)]
        return max_item, result_letter

    def add_neuron(self, symbol, neuron=None):
        if neuron is None:
            neuron = Neuron(self, self.neuronWidth, self.neuronHeight, self.neuronMinimum)
        self.neurons[symbol] = neuron

    def compare_array(self, a, b):
        if len(a) != len(b):
            return False
        for x in range(0, len(a)):
            if a[x] != b[x]:
                return False
        return True

    def save(self):
        self.save_to_file()

    def load(self):
        if path.exists(self.memory_file):
            self.load_from_file()
        else:
            #self.set_options(self.default_options)
            symbols = list(self.default_symbols)
            for symbol in symbols:
                self.add_neuron(symbol)

    def load_from_file(self):
        data = cPickle.load(open(self.memory_file, 'rb'))
        self.set_options(data)

    def set_options(self, options):
        print(options)
        for key in self.default_options:
            self.__dict__[key] = options[key] if key in options else self.__dict__[key]

    def save_to_file(self):
        data = {}
        for key in self.default_options:
            data[key] = self.__dict__[key]
        cPickle.dump(data, open(self.memory_file, 'wb'))

