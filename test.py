import unittest
from main import NeuralNetwork


# Test cases to test NN's methods
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.network = NeuralNetwork([5, 3, 3])

    def test_set_weights1(self):
        output = ([[2, 1, 3], [2, 1, 2], [3, 4, 5]], [3, -2, 5])
        self.assertEqual(self.network.network[1].set_weights([2, 1, 3, 2, 1, 2, 3, 4, 5, 3, -2, 5]), output, msg='Bobo')

    def test_set_weights2(self):
        output = ([[0.546, -4, 355678875865], [4, 678, 5], [345.76867, 6, 7], [8, -325.6, 6456.7], [4, 7, 87]],
                  [56, 34, 67.0, 34.0, 908])
        self.assertEqual(self.network.network[0].set_weights(
            [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4, 7, 87, 56, 34, 67., 34., 908]),
            output)

    def test_calculate0(self):
        output = self.network.calculate([6, -3, 4.6, -5.7, 0])
        self.assertEqual(output, [0, 0, 0])

    def test_calculate1(self):
        self.network.network[1].set_weights([2, 1, 3, 2, 1, 2, 3, 4, 5, 3, -2, 5])
        eps = 1e-3
        output = self.network.calculate([6, 3, 4.6, 5.7, 0])
        self.assertLessEqual(abs(output[0] - 0.727), eps)
        self.assertLessEqual(abs(output[1] - 0.773), eps)
        self.assertLessEqual(abs(output[2] - 0.835), eps)

    def test_calculate2(self):
        self.network.network[0].set_weights(
            [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4, 7, 87, 56, 34, 67., 34., 908])
        self.network.network[1].set_weights([2, 1, 3, 2, 1, 2, 3, 4, 5, 3, -2, 5])
        eps = 1e-3
        output = self.network.calculate([6, 3, 4.6, 5.7, 0])
        self.assertLessEqual(abs(output[0] - 0.874), eps)
        self.assertLessEqual(abs(output[1] - 0.857), eps)
        self.assertLessEqual(abs(output[2] - 0.908), eps)

    def test_calculate3(self):
        self.network.network[0].set_weights(
            [0.546, -4, 355678875865, 4, 678, 5, 345.76867, 6, 7, 8, -325.6, 6456.7, 4, 7, 87, 56, 34, 67., 34., 908])
        self.network.network[1].set_weights([8, 9.96, -3, 0.062, -0.7, 82, 63, -4, -58, 0.3, -2, 51])
        eps = 1e-3
        output = self.network.calculate([6, 3, 4.6, 5.7, 0])
        self.assertLessEqual(abs(output[0] - 0.986), eps)
        self.assertLessEqual(abs(output[1] - 0.840), eps)
        self.assertLessEqual(abs(output[2] - 0.953), eps)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
