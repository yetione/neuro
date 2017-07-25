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

    def create_network(self):
        for x in range(0, self.neuronsCount):
            self.neurons = Neuron(self, self.neuronWidth, self.neuronHeight, self.neuronMinimum)

    def read_image(self, image):
        pixel_map = []
        for r in range(0, self.neuronHeight):
            for c in range(0, self.neuronWidth):
                pixel_map[r][c] = image.pixel(r, c)

        return pixel_map
