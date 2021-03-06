#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import randint, random
from math import exp, log, tanh


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
                self.weight[r].append(random()/100.0)

    def transfer_hard(self, input):
        power = 0
        for r in range(0, self.height):
            for c in range(0, self.width):
                power += self.weight[r][c] * input[r][c]
        return 1 if power >= self.minimum else 0

    def sum(self, input):
        result = 0
        for x in range(0, self.height):
            for y in range(0, self.width):
                result += self.weight[x][y] * input[x][y]
        return result

    def transfer(self, input):
        """
        :param input: array
        :return: float
        """
        power = self.sum(input)
        power = power / 100.0
        return self.sigmod(power)
        # return self.sigmod(power)
        # return power/1000.0

    def sigmod(self, power):
        """
        :param power: float
        :return: float
        """
        return 1.0 / (1.0 + exp(-1.0 * power))

    def htan(self, power):
        return tanh(power/1.0)

    def change_weight(self, input, dif):
        for r in range(0, self.height):
            for c in range(0, self.width):
                self.weight[r][c] += dif
                #if self.weight[r][c] < 0:
                #    self.weight[r][c] = 0
        return True
