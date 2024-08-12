from .matrix import Matrix
import copy 

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
        result = (matrix.elements[0][0])
        return Matrix(result)
    elif matrix.row == 2:
        result = (matrix.elements[0][0]*matrix.elements[1][1]) - (matrix.elements[1][0]*matrix.elements[0][1])
        return Matrix(result)
    #calculation of the determinant
    det = 0
    sign = 1
    for j in range(matrix.col):
        element_a = matrix.elements[0][j]
        minor = inner(matrix, 0, j)
        result = determinant(minor)
        det += sign * element_a * result.elements[0][0]
        sign *= -1

    return Matrix(det)

#!returns a Matrix object
def inverse(matrix):
    #matrix has be square && > 1x1
    if (matrix.row != matrix.col) and (matrix.row > 1) :
        return -1
    
    det = determinant(matrix)

    #if matrix is singular
    if det.elements[0][0] == 0:
        return -1
    
    det.elements[0][0] = 1/det.elements[0][0]
    element = 0
    #sign = 1
    result = []
    for i in range(matrix.row):
        row = []
        for j in range(matrix.col):
            minor = inner(matrix, i, j)
            sign = (-1)**((i+1)+(j+1))
            temp = determinant(minor)
            element = sign*temp.elements[0][0]
            row.append(element)
        result.append(row)
    
    result = Matrix(result)
    result = transpose(result)
    result.scalar_multiplication(det.elements[0][0])

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
def check_move_zero(input_matrix):
    matrix = copy.deepcopy(input_matrix)
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
            zero_rows.append(i)
    
    for j in range(matrix.col):
        col_zero = True
        for i in range(matrix.row):
            if matrix.elements[i][j] != 0:
                col_zero = False
                break
        if col_zero:
            zero_cols.append(j)

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
    return matrix, zero_row_start_pos, zero_col_start_pos

#!modifies 
def row_echelon(input_matrix, lower_values=[]):
    matrix, zero_row, zero_col = check_move_zero(input_matrix)
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
    if matrix.elements[0][0] == 0:
        return matrix
    #if it's not a square matrix
    max_dim = zero_row
    if (zero_row > zero_col):
        max_dim = max(zero_row, zero_col)
    else:
        max_dim = min(zero_row, zero_col)
    #makes lower triangle all 0
    for i in range(max_dim):
        for j in range(i+1, max_dim):
            #next element / pivot
            temp = abs(matrix.elements[j][i])/abs(matrix.elements[i][i])
            lower_values.append(temp)
            #if of the same sign -> subtract else add to get 0
            if ((matrix.elements[i][i] > 0) and (matrix.elements[j][i] > 0)) or ((matrix.elements[i][i] < 0) and (matrix.elements[j][i] < 0)):
                for k in range(zero_col):
                    matrix.elements[j][k] -= temp * matrix.elements[i][k]
            else: 
                for k in range(zero_col):
                    matrix.elements[j][k] += temp * matrix.elements[i][k]
    #lower returns lower triangle 
    return matrix

#!modifies | returns int
def reduced_row_echelon(input_matrix):
    matrix = row_echelon(input_matrix)

    for i in range(matrix.row):
        pivot = False
        pivot_j = 1
        #figures out the pivot
        for j in range(matrix.col):
            if matrix.elements[i][j] != 0:
                pivot = True
                pivot_j = j
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
    return matrix

#!modifies | returns int 
def rank(input_matrix):
    matrix = reduced_row_echelon(input_matrix)
    rank = 0

    for i in range(matrix.col):
        if matrix.elements[i][i] == 1:
            rank += 1
    
    return Matrix(rank)

def lu_decomposition(input_matrix):
    low_tri_values = []
    upper = row_echelon(input_matrix, low_tri_values)
    low_tri_values.reverse()

    lower = []
    for i in range(input_matrix.row):
        row = []
        for j in range(input_matrix.col):
            if i == j:
                row.append(1)
            elif i > j:
                try:
                    row.append(low_tri_values.pop())
                except:
                    return -9, upper
            else:
                row.append(0)
        lower.append(row)

    return Matrix(lower), upper

#Ax = b
def solve_problem(input_matrix, b):
    matrix = copy.deepcopy(input_matrix)
    for i in range(matrix.row):
        matrix.elements[i].append(b[i])

    matrix.col = matrix.col+1

    matrix = reduced_row_echelon(matrix)

    return matrix

def qr_decomposition(matrix):
    #Perform QR decomposition of a matrix using Gram-Schmidt orthogonal.
    n = matrix.row
    Q = [[0] * n for _ in range(n)]
    R = [[0] * n for _ in range(n)]

    for j in range(n):
        # Compute the orthogonal vector q_j
        q = [matrix.elements[i][j] for i in range(n)]
        
        for i in range(j):
            r = sum(Q[k][i] * matrix.elements[k][j] for k in range(n))
            R[i][j] = r
            q = [q[k] - r * Q[k][i] for k in range(n)]
        
        norm = sum(x**2 for x in q) ** 0.5
        R[j][j] = norm
        Q = [[q[i] / norm if j == k else Q[i][k] for k in range(n)] for i in range(n)]
    
    return Matrix(Q), Matrix(R)

def eigenvalues(matrix, num_iterations=1000, tolerance=1e-10):
    if (matrix.row != matrix.col) and (matrix.row > 1) :
        return -1
    
    n = matrix.row
    A = matrix
    
    for _ in range(num_iterations):
        Q, R = qr_decomposition(A)
        A_next = R*Q
        
        if all(abs(A_next.elements[i][j]) < tolerance for i in range(n) for j in range(i)):
            break
        
        A = A_next
    
    eigenvalues = [A.elements[i][i] for i in range(n)]

    return Matrix(eigenvalues)