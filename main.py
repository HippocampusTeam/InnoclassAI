import copy
import random
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def create(input):
    network = [input,
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0]]
    weights = dict()  # 0;1-1;0
    for layer1 in range(len(network)):
        for neuron1 in range(len(network[layer1])):
            for layer2 in range(layer1 + 1, len(network)):
                for neuron2 in range(len(network[layer2])):
                    first = str(layer1) + ';' + str(neuron1)
                    second = str(layer2) + ';' + str(neuron2)
                    weights[first + '-' + second] = random.uniform(-5, 5)
    return network, weights


def calculate(network, weights):
    for layer in range(1, len(network)):
        for neuron in range(len(network[layer])):
            for previous in range(len(network[layer - 1])):
                first = str(layer - 1) + ';' + str(previous)
                second = str(layer) + ';' + str(neuron)
                network[layer][neuron] += weights[first + '-' + second] * network[layer - 1][neuron]
            network[layer][neuron] = sigmoid(network[layer][neuron])
    return network


def mutate(weights, percentage_mutation_rate):
    new_weights = copy.deepcopy(weights)
    for weight in random.sample(weights.keys(), int(len(weights.keys()) * percentage_mutation_rate)):
        new_weights = weights[weight] = random.uniform(-5, 5)
    return new_weights


# network, weights = create([6, 3, 4.6, 5.7, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
# network = calculate(network, weights)
# weights = mutate(weights, 0.25)
