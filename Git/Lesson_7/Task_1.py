class Matrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def __add__(self):
        matrix = []

        for i in range(len(self.matrix_1)):
            dict = []
            for j in range(len(self.matrix_2[i])):
                dict.append(self.matrix_1[i][j] + self.matrix_2[i][j])
            matrix.append(dict)


        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[12, 11, 17],
                    [22, 21, 27],
                    [31, 30, 39]],
                   [[41, 48, 42],
                    [53, 57, 58],
                    [64, 65, 66]])



print(my_matrix.__add__())