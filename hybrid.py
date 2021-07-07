# Функция активации
def softsign(x):
    return x / (abs(x) + 1)


class NeuralNetwork:
    def __init__(self, size):  # Создааем объект класса NeuralNetwork, передавая ему список размеров каждого слоя
        self.layers = list()  # Список слоев нейронов (каждый слой - это список значений нейронов)
        self.biases = list()  # Список bias'ов нейронов (структура такая же, как и у layers)
        for layer_size in size:  # Проходимся по списку размеров слоев
            self.layers.append([0] * layer_size)  # Создаем новый слой данного размера
            self.biases.append([0] * layer_size)  # Создаем список bias'ов для этого слоя

        self.weights = list()  # Создаем список весов
        self.weights.append(list())  #
        for layer in range(1, len(self.layers)):
            self.weights.append(list())
            for neuron in range(len(self.layers[layer])):
                self.weights[layer].append(list())
                for previous_neuron in range(len(self.layers[layer - 1])):
                    self.weights[layer][neuron].append(0)

    # Устанавливаем веса
    def set_weights(self, layer, weights):
        counter = 0

        # Проходим через все веса предыдущего слоя
        for previous_neuron in range(len(self.layers[layer - 1])):
            # Проходим через все веса текущего слоя
            for current_neuron in range(len(self.layers[layer])):
                self.weights[layer][current_neuron][previous_neuron] = weights[counter]
                # Устанавливаем значение веса на соответствующее по счету
                counter += 1

        return self.weights

    # Устанавливаем bias'ы
    def set_biases(self, layer, biases):
        self.biases[layer] = biases

    def calculate(self, input):
        self.layers[0] = input
        for layer in range(1, len(self.layers)):
            for neuron in range(len(self.layers[layer])):
                for previous in range(len(self.layers[layer - 1])):
                    self.layers[layer][neuron] += self.weights[layer][neuron][previous] * self.layers[layer - 1][previous]
                self.layers[layer][neuron] = softsign(self.layers[layer][neuron] + self.biases[layer][neuron])

