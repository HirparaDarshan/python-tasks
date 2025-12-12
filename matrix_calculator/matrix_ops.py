""" Task 9: Maxtrix class with 2x2 and 3x3 basic addition and multiplication operations """
class Matrix:
    """
    A class to represent a mathematical matrix and perform basic operations.
    """
    def __init__(self, data):
        """
        Initializes a Matrix.
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        """
        Performs matrix addition between this matrix and another matrix.
        """
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other):
        """
        Performs matrix multiplication between this matrix and another matrix.
        """
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum_product = 0
                for k in range(self.cols):
                    sum_product += self.data[i][k] * other.data[k][j]
                row.append(sum_product)
            result.append(row)

        return Matrix(result)

    def __str__(self):
        """
        Provide a string representation for printing the matrix.
        """
        s = ""
        for row in self.data:
            s += " ".join(map(str, row)) + "\n"
        return s

# Main program with Examples
if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    print("Matrix 1:")
    print(m1)
    print("Matrix 2:")
    print(m2)

    print("Addition of Matrix 1 and Matrix 2:")
    print(m1 + m2)

    print("Multiplication of Matrix 1 and Matrix 2:")
    print(m1 * m2)

    m3 = Matrix([[1, 2],[3, 4]])
    m4 = Matrix([[4, 3],[2, 1]])

    print("Matrix 3: ")
    print(m3)
    print("Matrix 4: ")
    print(m4)

    print("Addition of Matrix 3 and Matrix 4:")
    print(m3 + m4)

    print("Multiplication of Matrix 3 and Matrix 4:")
    print(m3 * m4)
