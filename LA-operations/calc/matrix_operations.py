from matrix import Matrix

#!returns a Matrix object
def transpose(matrix):
    result = []
    for j in range(matrix.col):
        row = []
        for i in range(matrix.row):
            row.append(matrix.elements[i][j])
        result.append(row)
    
    return Matrix(result)

#!returns a int 
def determinant(matrix):
    #check if matrix is square or not
    if matrix.row != matrix.col:
        return -1
    #base cases
    if matrix.row == 1:
        return matrix.elements[0][0]
    elif matrix.row == 2:
        return (matrix.elements[0][0]*matrix.elements[1][1]) - (matrix.elements[1][0]*matrix.elements[0][1])
    #calculation of the determinant
    det = 0
    sign = 1
    for j in range(matrix.col):
        element_a = matrix.elements[0][j]
        minor = inner(matrix, 0, j)
        det += sign * element_a * determinant(minor)
        sign *= -1
    
    return det

#!returns a Matrix object
def inverse(matrix):
    #matrix has be square && > 1x1
    if (matrix.row != matrix.col) and (matrix.row > 1) :
        return -1
    
    det = determinant(matrix)

    #if matrix is singular
    if det == 0:
        return -1
    
    det = 1/det
    element = 0
    #sign = 1
    result = []
    for i in range(matrix.row):
        row = []
        for j in range(matrix.col):
            minor = inner(matrix, i, j)
            sign = (-1)**((i+1)+(j+1))
            element = sign*determinant(minor)
            row.append(element)
        result.append(row)
    
    result = Matrix(result)
    result = transpose(result)
    result.scalar_multiplication(det)

    return result

#!returns a Matrix object
#finds the inner_matrix of each section
def inner(full_matrix, row_x, col_x):
    result = []
    for i in range(full_matrix.row):
        row = []
        if i == row_x:
            continue
        for j in range(full_matrix.col):
            if j == col_x:
                continue
            row.append(full_matrix.elements[i][j])
        result.append(row)
    
    return Matrix(result)

#!modifies a aruj matrix 
def check_move_zero(matrix):
    zero_rows = []
    zero_cols = []
    #checks which row/col has zeros
    for i in range(matrix.row):
        row_zero = True
        for j in range(matrix.col):
            if matrix.elements[i][j] != 0:
                row_zero = False
                break
        if row_zero:
            zero_row.append(i)
    
    for j in range(matrix.col):
        col_zero = True
        for i in range(matrix.row):
            if matrix.elements[i][j] != 0:
                col_zero = False
                break
        if col_zero:
            zero_col.append(j)

    #swaps the zero row/col to the end
    num_zero_row = len(zero_rows)
    if num_zero_row > 0:
        for i in range(num_zero_row):
            temp = matrix.elements[zero_rows[i]]
            matrix.elements[zero_rows[i]] = matrix.elements[matrix.row-1-i]
            matrix.elements[matrix.row-1-i] = temp
    num_zero_col = len(zero_cols)
    if num_zero_col > 0:
        for i in range(num_zero_col):
            for j in range(matrix.row):
                temp = matrix.elements[j][zero_cols[i]]
                matrix.elements[j][zero_cols[i]] = matrix.elements[j][matrix.col - 1 - i]
                matrix.elements[j][matrix.col - 1 - i] = temp
    zero_row_start_pos = matrix.row-num_zero_row
    zero_col_start_pos = matrix.col-num_zero_col
    
    #returns what row/col the zero row/col starts
    return zero_row_start_pos, zero_col_start_pos 

#!modifies 
def row_echelon(matrix):
    zero_row, zero_col = check_move_zero(matrix)
    
    #check if the [0][0] = 0
    row_s = 0
    if matrix.elements[0][0] == 0:
        row_s = 0.5
        for i in range(matrix.row):
            if matrix.elements[i][0] != 0:
                row_s = i
                break
        #swap rows when [0][0] is 0
        if row_s != 0.5:
            for j in range(matrix.col):
                temp = matrix.elements[0][j]
                matrix.elements[0][j] = matrix.elements[row_s][j]
                matrix.elements[row_s][j] = temp
    #if it's not a square matrix
    max_dim = zero_row
    if (zero_row > zero_col):
        max_dim = max(zero_row, zero_col)
    else:
        max_dim = min(zero_row, zero_col)
    #makes lower triangle all 0
    lower = []
    for i in range(max_dim):
        for j in range(i+1, max_dim):
            #next element / pivot
            temp = abs(matrix.elements[j][i])/abs(matrix.elements[i][i])
            lower.append(temp)
            #if of the same sign -> subtract else add to get 0
            if ((matrix.elements[i][i] > 0) and (matrix.elements[j][i] > 0)) or ((matrix.elements[i][i] < 0) and (matrix.elements[j][i] < 0)):
                for k in range(zero_col):
                    matrix.elements[j][k] -= temp * matrix.elements[i][k]
            else: 
                for k in range(zero_col):
                    matrix.elements[j][k] += temp * matrix.elements[i][k]

    return zero_row, zero_col, lower

#!modifies | returns int
def reduced_row_echelon(matrix):
    row_echelon(matrix)
    rank = 1

    for i in range(1, matrix.row):
        pivot = False
        pivot_j = 1
        #figures out the pivot
        for j in range(matrix.col):
            if matrix.elements[i][j] != 0:
                pivot = True
                pivot_j = j
                rank += 1
                break
        if pivot:
            pivot = False
            #makes pivot = 1
            pivot_value = matrix.elements[i][pivot_j]
            for j in range(pivot_j, matrix.col):
                matrix.elements[i][j] /= pivot_value
                if matrix.elements[i][pivot_j] < 0:
                    matrix.elements[i][j] *= -1

            #removes elements from above the pivot 
            for k in range(i, 0, -1):
                temp_pivot_holder = matrix.elements[k-1][pivot_j]
                for m in range(pivot_j, matrix.col):
                    temp = matrix.elements[i][m]*temp_pivot_holder
                    if ((temp > 0) and (matrix.elements[k-1][m] > 0)) or ((temp < 0) and (matrix.elements[k-1][m] < 0)):
                        matrix.elements[k-1][m] -= temp
                    elif ((matrix.elements[k-1][m] == 0) or (temp == 0)) and ((temp < 0) or (temp < 0)):
                        matrix.elements[k-1][m] -= temp
                    else:
                        matrix.elements[k-1][m] += temp

    return rank

#!modifies | returns int 
def rank(matrix):
    rank = reduced_row_echelon(matrix)
    return rank

"""
def eigenvalues(matrix):
    pass

def eigenvector():
    pass
"""

def lu_demonpisition(matrix):
    _, _, lower = row_echelon(matrix)
    lower.reverse()

    result = []
    for i in range(matrix.row):
        row = []
        for j in range(matrix.col):
            if i == j:
                row.append(1)
            elif i > j:
                row.append(lower.pop())
            else:
                row.append(0)
        result.append(row)
    
    return Matrix(result)


def main():

    x = Matrix([
        [1, 2],
        [0, -5]
    ])

    b = [4, 1]

    solve_problem(x, b)

    print_matrix(x.elements)


#Ax = b
def solve_problem(matrix, b):
    for i in range(matrix.row):
        matrix.elements[i].append(b[i])

    matrix.col = matrix.col+1

    print_matrix(matrix.elements)
    print()
    reduced_row_echelon(matrix)


#can use matrix mult
#have to limit the dimensions
def dot_product(matrix_a, matrix_b):
    result = matrix_a*matrix_b

    return result

#can use matrix mult
def cross_product():
    pass

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' | ') 
        print()

if __name__ == "__main__":
    main()