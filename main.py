import copy
import random
import math


class NeuralNetwork():
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def __init__(self, size):
        self.network = list()
        for i in size:
            self.network.append([0] * i)

        self.weights = dict()  # 0;1-1;0
        for layer1 in range(len(self.network)):
            for neuron1 in range(len(self.network[layer1])):
                for layer2 in range(layer1 + 1, len(self.network)):
                    for neuron2 in range(len(self.network[layer2])):
                        first = str(layer1) + ';' + str(neuron1)
                        second = str(layer2) + ';' + str(neuron2)
                        self.weights[first + '-' + second] = random.uniform(-5, 5)
    

    def calculate(self):
        for layer in range(1, len(self.network)):
            for neuron in range(len(self.network[layer])):
                for previous in range(len(self.network[layer - 1])):
                    first = str(layer - 1) + ';' + str(previous)
                    second = str(layer) + ';' + str(neuron)
                    self.network[layer][neuron] += self.weights[first + '-' + second] * self.network[layer - 1][neuron]
                self.network[layer][neuron] = self.sigmoid(self.network[layer][neuron])
        return self.network

    def mutate(self, percentage_mutation_rate):
        new_weights = copy.deepcopy(self.weights)
        for weight in random.sample(self.weights.keys(), int(len(self.weights.keys()) * percentage_mutation_rate)):
            new_weights = self.weights[weight] = random.uniform(-5, 5)
        return new_weights

# self.network, self.weights = create([6, 3, 4.6, 5.7, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
# self.network = calculate(self.network, self.weights)
# self.weights = mutate(self.weights, 0.25)
