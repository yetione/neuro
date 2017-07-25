#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import randint


class Neuron:
    height = 30
    width = 30
    minimum = 50
    def __init__(self, network, width=width, height=height, minimum=minimum):
        self.network = network
        self.width = width
        self.height = height
        self.minimum = minimum
        self.weight = []
        self.random_weight()


    def random_weight(self):
        for r in range(0, self.height):
            self.weight.append([])
            for c in range(0, self.width):
                self.weight[r].append(randint(0, 10))

    def transfer_hard(self, input):
        power = 0
        for r in range(0, self.height):
            for c in range(0, self.width):
                power += self.weight[r][c] * input[r][c]
        return 1 if power >= self.minimum else 0

    def transfer(self, input):
        power = 0
        for r in range(0, self.height):
            for c in range(0, self.width):
                power += self.weight[r][c] * input[r][c]
        return power

    def change_weight(self, input, dif):
        for r in range(0, self.height):
            for c in range(0, self.width):
                self.weight[r][c] += dif*input[r][c]