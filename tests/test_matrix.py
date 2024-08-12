import unittest
from calc.matrix import Matrix 

#add
class TestMatrixAddition(unittest.TestCase):
    def test_matrix_addition(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[2, 0], [1, 3]])
        result = matrix_a + matrix_b
        self.assertEqual(result.elements, [[3, 2], [4, 7]])

    def test_matrix_addition_mismatched_size(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[1, 2]])
        result = matrix_a + matrix_b
        self.assertEqual(result, -1)
#sub
class TestMatrixSubtraction(unittest.TestCase):
    def test_matrix_subtraction(self):
        matrix_a = Matrix([[5, 3], [7, 1]])
        matrix_b = Matrix([[2, 0], [1, 3]])
        result = matrix_a - matrix_b
        self.assertEqual(result.elements, [[3, 3], [6, -2]])

    def test_matrix_subtraction_mismatched_size(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[1, 2]])
        result = matrix_a - matrix_b
        self.assertEqual(result, -1)
#mul
class TestMatrixMultiplication(unittest.TestCase):
    def test_matrix_multiplication(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[2, 0], [1, 2]])
        result = matrix_a * matrix_b
        self.assertEqual(result.elements, [[4, 4], [10, 8]])

    def test_matrix_multiplication_mismatched_size(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[1, 2]])
        result = matrix_a * matrix_b
        self.assertEqual(result, -1)
#scalar
class TestScalarOperations(unittest.TestCase):
    def test_scalar_subtraction(self):
        matrix = Matrix([[3, 4], [5, 6]])
        matrix.scalar_subtraction(2)
        self.assertEqual(matrix.elements, [[1, 2], [3, 4]])

    def test_scalar_addition(self):
        matrix = Matrix([[3, 4], [5, 6]])
        matrix.scalar_addition(2)
        self.assertEqual(matrix.elements, [[5, 6], [7, 8]])

    def test_scalar_multiplication(self):
        matrix = Matrix([[1, 2], [3, 4]])
        matrix.scalar_multiplication(3)
        self.assertEqual(matrix.elements, [[3, 6], [9, 12]])

    def test_scalar_division(self):
        matrix = Matrix([[2, 4], [6, 8]])
        matrix.scalar_division(2)
        self.assertEqual(matrix.elements, [[1, 2], [3, 4]])

if __name__ == '__main__':
    unittest.main()
