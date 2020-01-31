from random import randint

class Matrix:
    def __init__(self,  lin_lin):
        self.lin_lin = lin_lin


    def draw(self):
        print('Матрица')
        for a in range(len(self.lin_lin)):
            lin_ = self.lin_lin[a]
            for a in lin_:
                print (a,  end=" ")
            print('')

    def __add__(self, other):
        print('Сложение матриц')
        for a in range(len(self.lin_lin)):
            lin_1 = self.lin_lin[a]
            lin_2 = other.lin_lin[a]
            for a in range(len(lin_1)):
                print (lin_1[a] + lin_2[a],  end=" ")
            print('')
        return Matrix(self.lin_lin + other.lin_lin)



def mat(z_str, z_stl):
    lin_lin = []
    for a in range(z_stl):
        lin_s = [randint(0, 100) for b in range(z_str)]
        lin_lin.append(lin_s)
    return lin_lin


z_str = int(input('Количество солбцов - '))
z_stl = int(input('Количество строк - '))

matrix1 = Matrix(mat(z_str, z_stl))
matrix1.draw()
matrix2 = Matrix(mat(z_str, z_stl))
matrix2.draw()
sum_mat = (matrix1 + matrix2)
