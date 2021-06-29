# Функция активации
def softsign(x):
    return x / (abs(x) + 1)


class Layer:

    # Создание объекта слоя
    def __init__(self, previous_count, neurons_count):
        self.size = neurons_count  # Количество нейронов в этом слое
        self.previous_size = previous_count  # Количество нейронов в следующем слое
        self.neurons = [0] * neurons_count  # Список значений нейронов этого слоя (изначально равны 0)
        self.biases = '''TODO: Создайте список значений bias (изначально равны 0)'''
        self.weights = list()  # Список, в котором хранятся списки весов между мейронами предыдущего и этого слоя (например, self.weights[previous_neuron][current_neuron] - вес, соединяющий какой-то нейрон из предыдущего слоя и какой-то нейрон из текущего)

        # Устанавливаем значения весов, исходящих из каждого нейрона (изначально нулевые)
        for neuron in range(previous_count):
            weights_of_neuron = list()  # Создаем список, в который нужно положить исходящие веса текущего нейрона (должны быть равны нулю)
            '''TODO: Заполните список weights_of_neuron'''
            self.weights.append(weights_of_neuron)  # Добавляем список весов текущего найрона к списку весов всего слоя

    # Устанавливаем веса
    def set_weights(self, weights):
        counter = 0

        # Проходим через все веса текущего слоя
        for previous_neuron in range(self.previous_size):
            # Проходим через все веса предыдущего слоя
            for current_neuron in range(self.size):
                self.weights[previous_neuron][current_neuron] = '''TODO: Установите значениее веса на соответствующее по счету'''
                counter += 1

        return self.weights

    def calculate(self, previous_layer):
        for current_neuron in range(self.size):
            for previous_neuron in range(self.previous_size):
                self.neurons[current_neuron] += '''TODO: Рассчитайте значение текщего нейрона, исхоля из нейронов предыдущего слоя'''
            neuron_value = '''TODO: Вычислите сумму значения и bias текущего нейрона'''
            self.neurons[current_neuron] = softsign(neuron_value)

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

        self.network.append(Layer(0, size[0]))  # Добавляем первый слой. При его создании пкркдаем количество нейронов в предыдущем слое (которого нет) и кроичество нейронов в текущем слое

        # Добавляем все остальные слои в нейронную сеть
        for layer in range(1, len(size)):
            self.network.append('''TODO: Создайте новый слой, передав количество нейронов в этом слое и в следующем''')

    # Вычисляем вывод нейронной сети
    def calculate(self, input):
        self.network[0].set_values(input)  # Задаем значения входного слоя

        # Проходимся по всем слоям сети, кроме первого (входного)
        for layer in range(1, len(self.network)):
            self.network[layer].set_values([0] * self.network[layer].size)  # Устанавливаем изначальное значение всех нейронов текущего слоя на 0
            '''TODO: вызываем метод calculate ТЕКУЩЕГО СЛОЯ, передав ему предыдущий слой'''
        return self.network[-1].neurons  # Возвращаем значения нейронов последнего слоя (вывод нейронной сети)
