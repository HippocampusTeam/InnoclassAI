# Функция активации
def softsign(x):
    return x / (abs(x) + 1)

# Класс нашей нейронной сети
class NeuralNetwork:
    def __init__(self, size):  # Создааем объект класса NeuralNetwork, передавая ему список размеров каждого слоя
        self.neurons = list()  # Список слоев нейронов (каждый слой - это список значений нейронов)
        self.biases = list()  # Список слоев bias'ов нейронов (каждый слой - это список значений bias'ов нейронов)
        for layer_size in size:  # Проходимся по списку размеров слоев
            self.neurons.append([0] * layer_size)  # Создаем новый слой нейронов данного размера
            self.biases.append('''TODO: Создайте список значений bias (изначально равны 0) для этого слоя''')

        # weights[layer][previous_neuron][current_neuron] - вес между нейроном под номером current в слое layer
        # и нейроном ПРЕДЫДУЩЕГО слоя под номером prev
        self.weights = list()  # Создаем список весов
        self.weights.append(list())  # Добавляем список весов нулевого (входного) слоя. Он пустой, тк этот слой первый

        for layer in range(1, len(self.neurons)):  # Проходимся по всем остальным слоям
            self.weights.append(list())  # Добавляем список этого слоя
            for previous_neuron in range(len(self.neurons[layer - 1])):  # Проходимся по всем нейронам ПРЕДЫДУЩЕГО слоя
                self.weights[layer].append(list())  # Добавляем список текущего нейрона предыдущего слоя в список слоя
                for current_neuron in range(len(self.neurons[layer])):  # Проходимся по всем нейронам ТЕКУЩЕГО слоя
                    self.weights[layer]['''TODO: Напишите нужный индекс'''].append(0)
                    # Добавляем вес между нейроном под номером current в слое layer
                    # и нейроном ПРЕДЫДУЩЕГО слоя под номером prev. Изначально равен 0

    # Устанавливаем веса
    def set_weights(self, layer, new_weights):
        counter = 0

        # Проходим через все веса предыдущего слоя
        for previous_neuron in range(len(self.neurons[layer - 1])):
            # Проходим через все веса текущего слоя
            for current_neuron in range(len(self.neurons[layer])):
                self.weights[layer][previous_neuron][current_neuron] = '''TODO: Установите значениее веса на соответствующее по счету'''
                counter += 1

        return self.weights[layer]

    # Устанавливаем bias'ы
    def set_biases(self, layer, biases):
        self.biases[layer] = biases

    # Вычисляем вывод (ответ) нейронной сети
    def calculate(self, input):
        self.neurons[0] = input  # Устанавливаем (входные) значения нулевого слоя
        for layer in range(1, len(self.neurons)):  # Проходимся по всем слоям, кроме нулевого
            for current_neuron in range(len(self.neurons[layer])):  # Проходимся по всем нейронам ТЕКУЩЕГО слоя
                for previous_neuron in range(len(self.neurons[layer - 1])):  # Проходимся по всем нейронам ПРЕДЫДУЩЕГО слоя
                    self.neurons[layer][current_neuron] += '''TODO: Рассчитайте значение текщего нейрона, исходя из нейронов предыдущего слоя'''
                neuron_value = '''TODO: Вычислите сумму значения и bias текущего нейрона'''
                self.neurons[layer][current_neuron] = softsign(neuron_value)  # Вычисляем значение нейрона, перепад его в функцию активации

        return self.neurons[-1]  # Возвращаем значение нейронов последного слоя
