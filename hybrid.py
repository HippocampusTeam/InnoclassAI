# Функция активации
def softsign(x):
    return x / (abs(x) + 1)


class NeuralNetwork:
    def __init__(self, size):
        self.network = list()
        self.biases = list()
        for layer_size in size:
            self.network.append([0] * layer_size)
            self.biases.append([0] * layer_size)

        self.weights = list()
        self.weights.append(list())
        for layer in range(1, len(self.network)):
            self.weights.append(list())
            for neuron in range(len(self.network[layer])):
                self.weights[layer].append(list())
                for previous in range(len(self.network[layer - 1])):
                    self.weights[layer][neuron].append(0)

    def set_weights(self, layer, weights):
        counter = 0

        # Проходим через все веса предыдущего слоя
        for previous_neuron in range(len(self.network[layer - 1])):
            # Проходим через все веса текущего слоя
            for current_neuron in range(len(self.network[layer])):
                self.weights[layer][current_neuron][previous_neuron] = weights[counter]  # Устанавливаем значение веса на соответствующее по счету
                counter += 1

        return self.weights

    # Устанавливаем bias'ы
    def set_biases(self, layer, biases):
        self.biases[layer] = biases

    def calculate(self, input):
        self.network[0] = input
        for layer in range(1, len(self.network)):
            for neuron in range(len(self.network[layer])):
                for previous in range(len(self.network[layer - 1])):
                    self.network[layer][neuron] += self.weights[layer][neuron][previous] * self.network[layer - 1][previous]
                self.network[layer][neuron] = softsign(self.network[layer][neuron] + self.biases[layer][neuron])

