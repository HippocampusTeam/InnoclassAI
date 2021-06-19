import unittest
from main import NeuralNetwork


# Test cases to test NN's methods
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.network = NeuralNetwork([5, 3, 3])

    def test_set_weights(self):
        self.network.network[1].set_weights([2, 1, 3, 2, 1, 2, 3, 4, 5, 3, -2, 5])
        self.assertEqual(self.network.calculate([6, 3, 4.6, 5.7, 0]), 11, msg='Bobo')


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
