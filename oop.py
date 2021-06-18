import random


class Layer:
    def __init__(self, neurons_count, output_count):
        self.size = neurons_count
        self.next_size = output_count
        self.neurons = [0] * neurons_count
        self.weights = list()

        for neuron in range(neurons_count):
            self.weights.append(list())
            for next_neuron in range(output_count):
                self.weights[neuron].append(random.uniform(-5, 5))

    def set_weights(self, weights):
        if len(weights) == self.size * self.next_size:
            counter = 0
            for neuron in range(self.size):
                for next_neuron in range(self.next_size):
                    self.weights[neuron] = weights[counter]
                    counter += 1
        else:
            return "Wrong layer size"

    def resize(self, new_size):
        new_size -= self.size

