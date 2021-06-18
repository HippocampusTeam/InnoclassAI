import math


def softsign(x):
    return x / (abs(x) + 1)


class Layer:
    def __init__(self, neurons_count, output_count):
        self.size = neurons_count
        self.next_size = output_count
        self.neurons = [0] * neurons_count
        self.weights = list()

        for neuron in range(neurons_count):
            self.weights.append([0] * output_count)

    def set_weights(self, weights):
        if len(weights) == self.size * self.next_size:
            counter = 0
            for neuron in range(self.size):
                for next_neuron in range(self.next_size):
                    self.weights[neuron][next_neuron] = weights[counter]
                    counter += 1
        else:
            return "Wrong layer size"

    def set_values(self, values):
        if len(values) == len(self.neurons):
            self.neurons = values
        else:
            return "Wrong layer size"


class NeuralNetwork:
    def __init__(self, size):
        self.network = list()
        for layer in range(len(size)):
            if layer != len(size) - 1:
                self.network.append(Layer(size[layer], size[layer + 1]))
            else:
                self.network.append(Layer(size[layer], 0))

    def calculate(self, input):
        self.network[0].set_values(input)
        for layer in range(1, len(self.network)):
            for current_neuron in range(self.network[layer].size):
                for previous_neuron in range(self.network[layer - 1].size):
                    self.network[layer].neurons[current_neuron] += self.network[layer - 1].weights[previous_neuron][
                                                                       current_neuron] * \
                                                                   self.network[layer - 1].neurons[current_neuron]
                self.network[layer].neurons[current_neuron] = softsign(self.network[layer].neurons[current_neuron])
        return self.network[-1].neurons

# network = NeuralNetwork([19, 3, 3])
# network.network[1].set_weights([2, 1, 3, 2, 1, 2, 3, 4, 5])
# network.calculate([6, 3, 4.6, 5.7, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
