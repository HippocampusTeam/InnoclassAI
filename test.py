from task import NeuralNetwork
from sys import exc_info
from traceback import extract_tb

calculate_msg = 'Что-то не так с вычислением вывода нейронной сети (функция calculate). Убедитесь, что: веса ' \
                'последнего слоя выставляются правильно, вы используете функцию активации, вы правильно вычисляете ' \
                'значения ВСЕХ нейронов, вы не забываете умножать на веса и не перепутали индексы нейронов. '
eps = 1e-3


# Test cases to test NN's methods
def test_set_weights1():
    try:
        network = NeuralNetwork([5, 3, 3])
        output = ([[2, 1, 3], [2, 1, 2], [3, 4, 5]])
        assert network.set_weights(2, [2, 1, 3, 2, 1, 2, 3, 4, 5]) == output
    except Exception as e:
        print('Тест #1: Что-то не так с установкой весов во третьем слое. Проверьте функцию set_weights.')
        if not (e.__class__ is AssertionError):
            print('Причина:', e.args[0], 'в строке номер', str(extract_tb(exc_info()[2])[1][1]) + '.\n')
    else:
        print('Тест #1 пройден!\n')


def test_set_weights2():
    output = ([[0.546, -4, 355678875865], [4, 678, 5], [345.76867, 6, 7], [8, -325.6, 6456.7], [4, 7, 87]])
    try:
        network = NeuralNetwork([5, 3, 3])
        assert network.set_weights(1,
                                   [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4,
                                    7, 87]) == output
    except Exception as e:
        print('Тест #2: Что-то не так с установкой весов во третьем слое. Проверьте функцию set_weights.')
        if not (e.__class__ is AssertionError):
            print('Причина:', e.args[0], 'в строке номер', str(extract_tb(exc_info()[2])[1][1]) + '.\n')
    else:
        print('Тест #2 пройден!\n')


def test_calculate0():
    try:
        network = NeuralNetwork([5, 3, 3])
        output = network.calculate([6, -3, 4.6, -5.7, 0])
        assert output == [0, 0, 0]
    except Exception as e:
        print('Тест #3: Что-то не так с вычислением вывода нейронной сети (функция calculate). Убедитесь, '
              'что все веса изначально равны 0.')
        if not (e.__class__ is AssertionError):
            print('Причина:', e.args[0], 'в строке номер', str(extract_tb(exc_info()[2])[1][1]) + '.\n')
    else:
        print('Тест #3 пройден!\n')


def test_calculate1():
    try:
        network = NeuralNetwork([5, 3, 3])
        network.set_weights(2, [2, 1, 3, 2, 1, 2, 3, 4, 5])
        network.set_biases(1, [3, -2, 5])
        output = network.calculate([6, 3, 4.6, 5.7, 0])
        assert abs(output[0] - 0.727) <= eps
        assert abs(output[1] - 0.773) <= eps
        assert abs(output[2] - 0.835) <= eps
    except Exception as e:
        print('Тест #4:', calculate_msg)
        if not (e.__class__ is AssertionError):
            print('Причина:', e.args[0], 'в строке номер', str(extract_tb(exc_info()[2])[1][1]) + '.\n')
    else:
        print('Тест #4 пройден!\n')


def test_calculate2():
    try:
        network = NeuralNetwork([5, 3, 3])
        network.set_weights(1,
                            [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4, 7, 87,
                             56, 34, 67., 34., 908])
        network.set_weights(2, [2, 1, 3, 2, 1, 2, 3, 4, 5, 3, -2, 5])
        output = network.calculate([6, 3, 4.6, 5.7, 0])
        assert abs(output[0] - 0.874) <= eps
        assert abs(output[1] - 0.857) <= eps
        assert abs(output[2] - 0.908) <= eps
    except Exception as e:
        print('Тест #5:', calculate_msg)
        if not (e.__class__ is AssertionError):
            print('Причина:', e.args[0], 'в строке номер', str(extract_tb(exc_info()[2])[1][1]) + '.\n')
    else:
        print('Тест #5 пройден!\n')


def test_calculate3():
    try:
        network = NeuralNetwork([5, 3, 3])
        network.set_weights(1,
                            [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4, 7, 87])
        network.set_biases(0, [56, 34, 67., 34., 908])
        network.set_weights(2, [8, 9.96, -3, 0.062, -0.7, 82, 63, -4, -58])
        network.set_biases(1, [0.3, -2, 51])
        output = network.calculate([6, 3, 4.6, 5.7, 0])
        assert abs(output[0] - 0.986) <= eps
        assert abs(output[1] - 0.840) <= eps
        assert abs(output[2] - 0.953) <= eps
    except Exception as e:
        print('Тест #6:', calculate_msg)
        if not (e.__class__ is AssertionError):
            print('Причина:', e.args[0], 'в строке номер', str(extract_tb(exc_info()[2])[1][1]) + '.\n')
    else:
        print('Тест #6 пройден!\n')


# Executing the tests in the above test case class
if __name__ == "__main__":
    test_set_weights1()
    test_set_weights2()
    test_calculate0()
    test_calculate1()
    test_calculate2()
    test_calculate3()
