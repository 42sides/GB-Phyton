class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):
        return f"Первоначальный вид матрицы 1: {self.list_1}\nПервоначальный вид матрицы 2: {self.list_2}"

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str("\nПосле сложения: \n" + '\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


matr = Matrix(
    [[5, 18, 11], [6, 17, 23], [41, 50, 9]],
    [[45, 8, 2], [6, 7, 93], [24, 5, 97]]
)

print(matr)
print(matr.__add__())
