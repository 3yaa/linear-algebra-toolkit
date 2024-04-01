class Matrix:
    def __init__(self, elements):
        if (isinstance(elements, int)) or (isinstance(elements, float)):
            self.elements = [[elements]]
            self.row = 1
            self.col = 1
        else:
            self.elements = elements
            self.row = len(elements)
            try:
                self.col = len(elements[0])
            except (TypeError, IndexError):
                self.col = 0
    
    def __add__(self, matrix_b):
        if (self.row != matrix_b.row) or (self.col != matrix_b.col):
            return -1

        result = [[self.elements[i][j] + matrix_b.elements[i][j] for j in range(self.col)] for i in range(self.row)]
        return Matrix(result)
    
    def __sub__(self, matrix_b):
        if (self.row != matrix_b.row) or (self.col != matrix_b.col):
            return -1
        
        result = [[self.elements[i][j] - matrix_b.elements[i][j] for j in range(self.col)] for i in range(self.row)]
        return Matrix(result)
    
    def __mul__(self, matrix_b):
        if self.col != matrix_b.row:
            return -1
        
        result = []
        for i in range(self.row):
            row = []
            for j in range(matrix_b.col):
                sum = 0
                for k in range(matrix_b.row):
                    sum += self.elements[i][k]*matrix_b.elements[k][j]
                row.append(sum)
            result.append(row)

        return Matrix(result)

    def scalar_subtraction(self, number):
        for i in range(self.row):
            for j in range(self.col):
                self.elements[i][j] += number;

    def scalar_addition(self, number):
        for i in range(self.row):
            for j in range(self.col):
                self.elements[i][j] -= number;

    def scalar_multiplication(self, number):
        for i in range(self.row):
            for j in range(self.col):
                self.elements[i][j] *= number;

    def scalar_division(self, number):
        for i in range(self.row):
            for j in range(self.col):
                self.elements[i][j] /= number;