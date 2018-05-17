#!/usr/bin/env python3

#Representation of a Nueron node for Neural Networks

import random as rand
import sys

class neuron:
    """
    Representation of a neuron node.
    """
    def __init__(self, inputs = (), activationFunction = 0):
        """
       :param inputs:
        A tuple of other neuron objects that are in the layer previouse to this node
        :param activationFunction:
        int ∈ [0, 1], 0 = step function 1 = sigmoid
        """
        if not isinstance(inputs, tuple):
            raise TypeError('node inputs must be in a tuple')
        if not 0 <= activationFunction <= 1:
            raise TypeError(f'Activation function perameter must 0 (step function) or 1 (sigmoid function). Input was {activationFunction}')

        self._actvFunc = activationFunction
        self._bias = rand.randint
        self._inputs = dict()
        for i in inputs:
            self._inputs[rand.randint] = i

    def input_stream(self):
        return self._inputs


def stepActvFunc(inputs, bias):
    for input in inputs:
        inputSum = inputSum + (input.value * input.key)



def main():
    print('OK')
    x = sys.path
    print(x)

if __name__ == '__main__': main()







