#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path

from network.neuron import Neuron


class Network:
    def __init__(self):
        self.dir = path.dirname(__file__)
        self.neuronsCount = 10
        self.neuronWidth = 30
        self.neuronHeight = 30
        self.neuronMinimum = 50
        self.neurons = []
        self.create_network()

    def create_network(self):
        for x in range(0, self.neuronsCount):
            self.neurons.append(Neuron(self, self.neuronWidth, self.neuronHeight, self.neuronMinimum))

    def read_image(self, image):
        pixel_map = []
        for r in range(0, self.neuronHeight):
            pixel_map.append([])
            for c in range(0, self.neuronWidth):
                pixel_data = image.getpixel((r, c))
                #pixel_map[r].append(pixel_data[0] + pixel_data[1] + pixel_data[2])
                pixel_map[r].append(pixel_data)

        return pixel_map

    def handle_hard(self, input):
        output = []
        for x in range(0, self.neuronsCount):
            print(self.neurons[x])
            output.append(self.neurons[x].transfer_hard(input))
        return output

    def handle(self, input):
        output = []
        for x in range(0, self.neuronsCount):
            output.append(self.neurons[x].transfer(input))
        return output

    def study(self, input, correctAnswer):
        self.neurons[correctAnswer] = 1
        correctOutput = []

        output = self.handle_hard(input)
        while not self.compare_array(correctOutput, output):
            for x in range(0, len(self.neurons)):
                dif = correctOutput[x] - output[x]
                self.neurons[x].change_weight(input, dif)
            output = self.handle_hard(input)


    def compare_array(self, a, b):
        if len(a) != len(b):
            return False
        for x in range(0, len(a)):
            if a[x] != b[x]:
                return False
        return True

