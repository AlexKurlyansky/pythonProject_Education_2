import numpy as np
import random

class Matrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def get_matrix_1(self):
        my_matrix_1 = []
        # my_matrix_1 = [[random.random() for e in range(3)] for e in range(3)]
        my_matrix_1.append(np.random.randint(0, 10, (3, 3)))
        print(my_matrix_1)
        # return f"{self.my_matrix_1}"
        return my_matrix_1
# my_matrix_1.append(np.random.randint(0, 100, (3, 3)))
        print(my_matrix_1)

#     def get_matrix_2(self):
#         np.random.randint(0, 100, (3, 3))
#         return f"{self.matrix_2}"
# # my_matrix = Matrix(get_matrix_1, get_matrix_2)
# # print(my_matrix)