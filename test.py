import unittest
from main import NeuralNetwork

calculate_msg = 'Что-то не так с вычислением вывода нейронной сети (функция calculate). Убедитесь, что: веса последнего слоя выставляются правильно, вы используете функцию активации, вы правильно вычисляете значения ВСЕХ нейронов, вы не забываете умножать на веса и не перепутали индексы нейронов'


# Test cases to test NN's methods
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.network = NeuralNetwork([5, 3, 3])

    def test_set_weights1(self):
        output = ([[2, 1, 3], [2, 1, 2], [3, 4, 5]])
        self.assertEqual(self.network.network[2].set_weights([2, 1, 3, 2, 1, 2, 3, 4, 5]), output,
                         msg='Что-то не так с установкой весов во третьем слое. Проверьте функцию set_weights')

    def test_set_weights2(self):
        output = ([[0.546, -4, 355678875865], [4, 678, 5], [345.76867, 6, 7], [8, -325.6, 6456.7], [4, 7, 87]])
        self.assertEqual(self.network.network[1].set_weights(
            [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4, 7, 87]),
            output, msg='Что-то не так с установкой весов во втором слое. Проверьте функцию set_weights')

    def test_calculate0(self):
        output = self.network.calculate([6, -3, 4.6, -5.7, 0])
        self.assertEqual(output, [0, 0, 0],
                         msg='Что-то не так с вычислением вывода нейронной сети (функция calculate). Убедитесь, '
                             'что все веса изначально равны 0')

    def test_calculate1(self):
        self.network.network[2].set_weights([2, 1, 3, 2, 1, 2, 3, 4, 5])
        self.network.network[1].set_biases([3, -2, 5])
        eps = 1e-3
        output = self.network.calculate([6, 3, 4.6, 5.7, 0])
        self.assertLessEqual(abs(output[0] - 0.727), eps, msg=calculate_msg)
        self.assertLessEqual(abs(output[1] - 0.773), eps, msg=calculate_msg)
        self.assertLessEqual(abs(output[2] - 0.835), eps, msg=calculate_msg)

    def test_calculate2(self):
        self.network.network[1].set_weights(
            [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4, 7, 87, 56, 34, 67., 34., 908])
        self.network.network[2].set_weights([2, 1, 3, 2, 1, 2, 3, 4, 5, 3, -2, 5])
        eps = 1e-3
        output = self.network.calculate([6, 3, 4.6, 5.7, 0])
        self.assertLessEqual(abs(output[0] - 0.874), eps, msg=calculate_msg)
        self.assertLessEqual(abs(output[1] - 0.857), eps, msg=calculate_msg)
        self.assertLessEqual(abs(output[2] - 0.908), eps, msg=calculate_msg)

    def test_calculate3(self):
        self.network.network[1].set_weights(
            [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4, 7, 87])
        self.network.network[0].set_biases([56, 34, 67., 34., 908])
        self.network.network[2].set_weights([8, 9.96, -3, 0.062, -0.7, 82, 63, -4, -58])
        self.network.network[1].set_biases([0.3, -2, 51])
        eps = 1e-3
        output = self.network.calculate([6, 3, 4.6, 5.7, 0])
        self.assertLessEqual(abs(output[0] - 0.986), eps, msg=calculate_msg)
        self.assertLessEqual(abs(output[1] - 0.840), eps, msg=calculate_msg)
        self.assertLessEqual(abs(output[2] - 0.953), eps, msg=calculate_msg)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
