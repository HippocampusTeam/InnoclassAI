# Функция активации
def softsign(x):
    return x / (abs(x) + 1)


class Layer:

    # Создание объекта слоя
    def __init__(self, previous_count, neurons_count):
        self.size = neurons_count  # Количество нейронов в этом слое
        self.previous_size = previous_count  # Количество нейронов в следующем слое
        self.neurons = [0] * neurons_count  # Список значений нейронов этого слоя (изначально равны 0)
        self.biases = [0] * neurons_count  # TODO: Создайте список значений bias (изначально равны 0)
        self.weights = list()  # Список, в котором подряд

        # Устанавливаем значения весов, исходящих из каждого нейрона (изначально нулевые)
        for neuron in range(neurons_count):
            weights_of_neuron = [0] * previous_count  # Создаем список, в который нужно положить исходящие веса текущего нейрона (должны быть равны нулю)
            self.weights.append(weights_of_neuron)

    # Устанавливаем веса
    def set_weights(self, weights):
        counter = 0

        # Проходим через все веса текущего слоя
        for current_neuron in range(self.size):
            # Проходим через все веса предыдущего слоя
            for previous_neuron in range(self.previous_size):
                self.weights[current_neuron][previous_neuron] = weights[counter]  # TODO: Установите значениее веса на соответствующее по счету
                counter += 1

        return self.weights

    def calculate(self, previous_layer):
        for current_neuron in range(self.size):
            for previous_neuron in range(self.previous_size):
                self.neurons[current_neuron] += self.weights[current_neuron][previous_neuron] * \
                                                previous_layer.neurons[previous_neuron]
            self.neurons[current_neuron] = softsign(self.neurons[current_neuron] + self.biases[current_neuron])

    # Устанавливаем bias'ы
    def set_biases(self, biases):
        self.biases = biases

    # Устанавливаем значения нейронов
    def set_values(self, values):
        self.neurons = values


class NeuralNetwork:

    # Создаем объект нейронной сети
    def __init__(self, size):
        self.network = list()

        self.network.append(Layer(0, size[0]))  # Добавляем последний слой, у которого нет выходных весов
        # Добавляем все слои (кроме последнего) в нейронную сеть
        for layer in range(1, len(size)):
            self.network.append(Layer(size[layer - 1], size[
                layer]))  # При создании слоя передаем количество нейронов в этом слое и в следующем

    # Вычисляем вывод нейронной сети
    def calculate(self, input):
        self.network[0].set_values(input)  # Задаем значения входного слоя

        for layer in range(1, len(self.network)):
            self.network[layer].set_values([0] * self.network[layer].size)
            self.network[layer].calculate(self.network[layer - 1])
        return self.network[-1].neurons
