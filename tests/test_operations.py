import unittest
from calc.matrix_operations import *
from calc.matrix import Matrix

#transpose
class TestTranspose(unittest.TestCase):
    def test_transpose_square_matrix(self):
        matrix = Matrix([[1, 2], [3, 4]])
        result = transpose(matrix)
        self.assertEqual(result.elements, [[1, 3], [2, 4]])

    def test_transpose_non_square_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        result = transpose(matrix)
        self.assertEqual(result.elements, [[1, 4], [2, 5], [3, 6]])
#det
class TestDeterminant(unittest.TestCase):
    def test_determinant_2x2_matrix(self):
        matrix = Matrix([[1, 2], [3, 4]])
        result = determinant(matrix)
        self.assertEqual(result.elements, [[-2]])

    def test_determinant_3x3_matrix(self):
        matrix = Matrix([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
        result = determinant(matrix)
        self.assertEqual(result.elements, [[1]])

    def test_determinant_non_square_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        result = determinant(matrix)
        self.assertEqual(result, -1) 
#inverse
class TestInverse(unittest.TestCase):
    def test_inverse_2x2_matrix(self):
        matrix = Matrix([[1, 2], [3, 4]])
        result = inverse(matrix)
        self.assertAlmostEqual(result.elements[0][0], -2.0)
        self.assertAlmostEqual(result.elements[0][1], 1.0)
        self.assertAlmostEqual(result.elements[1][0], 1.5)
        self.assertAlmostEqual(result.elements[1][1], -0.5)

    def test_inverse_singular_matrix(self):
        matrix = Matrix([[1, 2], [2, 4]])
        result = inverse(matrix)
        self.assertEqual(result, -1)

    def test_inverse_3x3_matrix(self):
        matrix = Matrix([[1, 0, 2], [0, 1, 0], [0, 0, 1]])
        result = inverse(matrix)
        self.assertEqual(result.elements, [[1, 0, -2], [0, 1, 0], [0, 0, 1]])
#ref
class TestRowEchelon(unittest.TestCase):
    def test_row_echelon_simple_matrix(self):
        matrix = Matrix([[1, 2], [3, 4]])
        result = row_echelon(matrix)
        self.assertEqual(result.elements, [[1, 2], [0, -2]])

    def test_row_echelon_with_zero_row(self):
        matrix = Matrix([[1, 2], [0, 0]])
        result = row_echelon(matrix)
        self.assertEqual(result.elements, [[1, 2], [0, 0]])
#rref
class TestReducedRowEchelon(unittest.TestCase):
    def test_rref_simple_matrix(self):
        matrix = Matrix([[1, 2], [3, 4]])
        result = reduced_row_echelon(matrix)
        self.assertEqual(result.elements, [[1, 0], [0, 1]])

    def test_rref_with_zero_row(self):
        matrix = Matrix([[1, 2], [0, 0]])
        result = reduced_row_echelon(matrix)
        self.assertEqual(result.elements, [[1, 2], [0, 0]])
#rank
class TestRank(unittest.TestCase):
    def test_rank_full_rank(self):
        matrix = Matrix([[1, 2], [3, 4]])
        result = rank(matrix)
        self.assertEqual(result.elements, [[2]])

    def test_rank_deficient_matrix(self):
        matrix = Matrix([[1, 2], [2, 4]])
        result = rank(matrix)
        self.assertEqual(result.elements, [[1]])
#lu
class TestLUDecomposition(unittest.TestCase):
    def test_lu_decomposition_simple_matrix(self):
        matrix = Matrix([[4, 3], [6, 3]])
        lower, upper = lu_decomposition(matrix)
        self.assertEqual(lower.elements, [[1, 0], [1.5, 1]])
        self.assertEqual(upper.elements, [[4, 3], [0, -1.5]])
#qr
class TestQRDecomposition(unittest.TestCase):
    def test_qr_decomposition_simple_matrix(self):
        matrix = Matrix([[1, 0], [0, 1]])
        Q, R = qr_decomposition(matrix)
        self.assertEqual(Q.elements, [[1, 0], [0, 1]])
        self.assertEqual(R.elements, [[1, 0], [0, 1]])
#ab
class TestSolveProblem(unittest.TestCase):
    def test_solve_ax_equals_b(self):
        matrix = Matrix([[1, 5], [5, 10]])
        b = [1, 5]
        result = solve_problem(matrix, b)
        self.assertAlmostEqual(result.elements[0][2], 1)
        self.assertAlmostEqual(result.elements[1][2], -0)

if __name__ == '__main__':
    unittest.main()