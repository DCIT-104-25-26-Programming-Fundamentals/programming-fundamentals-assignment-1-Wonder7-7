# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(name):
    """Prompt the user to enter a matrix called `name` and return it as a
    list of lists of ints."""
    print(f"\n--- Enter matrix {name} ---")

    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                continue
            break
        except ValueError:
            print("Please enter valid whole numbers.")

    matrix = []
    for r in range(rows):
        while True:
            raw = input(f"Enter row {r + 1}: ")
            values = raw.split()
            if len(values) != cols:
                print(f"Expected {cols} values, got {len(values)}. Try again.")
                continue
            try:
                matrix.append([int(v) for v in values])
                break
            except ValueError:
                print("Please enter valid whole numbers separated by spaces.")

    return matrix


def print_matrix(matrix, title="Matrix"):
    """Display `matrix` in a neat, aligned grid."""
    print(f"\n{title}:")

    # Find the widest number so every column lines up.
    widest = 1
    for row in matrix:
        for value in row:
            widest = max(widest, len(str(value)))

    for row in matrix:
        line = "  ".join(str(value).rjust(widest) for value in row)
        print(line)


def transpose_matrix(matrix):
    """Return the transpose of `matrix` (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product A x B."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    matrix = read_matrix("M")
    print_matrix(matrix, "Original Matrix")
    print_matrix(transpose_matrix(matrix), "Transposed Matrix")


def part_b_addition():
    print("\nBoth matrices must be the same size (M x N).")
    matrix_a = read_matrix("A")
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    while True:
        matrix_b = read_matrix(f"B ({rows} x {cols})")
        if len(matrix_b) == rows and len(matrix_b[0]) == cols:
            break
        print(f"Matrix B must be {rows} x {cols}. Please re-enter it.")

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(add_matrices(matrix_a, matrix_b), "A + B")


def part_c_multiplication():
    print("\nColumns of A must equal rows of B.")
    matrix_a = read_matrix("A")
    cols_a = len(matrix_a[0])

    while True:
        matrix_b = read_matrix("B")
        if len(matrix_b) == cols_a:
            break
        print(f"Matrix B must have {cols_a} rows to match A's columns. Please re-enter it.")

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(multiply_matrices(matrix_a, matrix_b), "A x B")


def main():
    print("=== Matrix Operations ===")
    print("1. Transpose a matrix")
    print("2. Add two matrices")
    print("3. Multiply two matrices")

    choice = input("Choose an operation (1-3): ").strip()

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_addition()
    elif choice == "3":
        part_c_multiplication()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()