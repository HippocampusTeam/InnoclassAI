# Функция активации
def softsign(x):
    return x / (abs(x) + 1)


class NeuralNetwork:
    def __init__(self, size):  # Создааем объект класса NeuralNetwork, передавая ему список размеров каждого слоя
        self.neurons = list()  # Список слоев нейронов (каждый слой - это список значений нейронов)
        self.biases = list()  # Список bias'ов нейронов (структура такая же, как и у neurons)
        for layer_size in size:  # Проходимся по списку размеров слоев
            self.neurons.append([0] * layer_size)  # Создаем новый слой данного размера
            self.biases.append([0] * layer_size)  # Создаем список bias'ов для этого слоя

        self.weights = list()  # Создаем список весов
        self.weights.append(list())
        for layer in range(1, len(self.neurons)):
            self.weights.append(list())
            for previous_neuron in range(len(self.neurons[layer - 1])):
                self.weights[layer].append(list())
                for current_neuron in range(len(self.neurons[layer])):
                    self.weights[layer][previous_neuron].append(0)

    # Устанавливаем веса
    def set_weights(self, layer, weights):
        counter = 0

        # Проходим через все веса предыдущего слоя
        for previous_neuron in range(len(self.neurons[layer - 1])):
            # Проходим через все веса текущего слоя
            for current_neuron in range(len(self.neurons[layer])):
                self.weights[layer][previous_neuron][current_neuron] = weights[counter]
                # Устанавливаем значение веса на соответствующее по счету
                counter += 1

        return self.weights[layer]

    # Устанавливаем bias'ы
    def set_biases(self, layer, biases):
        self.biases[layer] = biases

    def calculate(self, input):
        self.neurons[0] = input
        for layer in range(1, len(self.neurons)):
            for neuron in range(len(self.neurons[layer])):
                self.neurons[layer][neuron] = 0
                for previous in range(len(self.neurons[layer - 1])):
                    self.neurons[layer][neuron] += self.weights[layer][previous][neuron] * self.neurons[layer - 1][previous]
                self.neurons[layer][neuron] = softsign(self.neurons[layer][neuron] + self.biases[layer][neuron])

        return self.neurons[-1]

