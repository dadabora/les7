class Dress:

    def __init__(self, jackets, coats, dress_cloth):
        self.cloth_j = jackets
        self.cloth_c = coats
        self.dress_cloth = dress_cloth

    def cloth(self):
        print(f'Всего ткани израсходовано {self.dress_cloth[2]},' \
              f' на пиджаки ушло {self.dress_cloth[0]},' \
              f' на пальто {self.dress_cloth[1]}')

    @property
    def my_method(self):
        return f'Всего ткани израсходовано {dress_cloth[2]},' \
               f' на пиджаки ушло {dress_cloth[0]},' \
               f' на пальто {dress_cloth[1]}'


class Jacket(Dress):
    def cloth(self):
        cloth_j = (self.cloth_j / 6) + 0.5
        cloth_j = round(cloth_j, 2)
        self.dress_cloth[0] = (cloth_j + self.dress_cloth[0])
        self.dress_cloth[2] = (cloth_j + self.dress_cloth[2])
        dress_cloth = self.dress_cloth
        return dress_cloth


class Coat(Dress):
    def cloth(self):
        cloth_c = (self.cloth_c * 2) + 0.3
        cloth_c = round(cloth_c, 2)
        self.dress_cloth[1] = (cloth_c + self.dress_cloth[1])
        self.dress_cloth[2] = (cloth_c + self.dress_cloth[2])
        dress_cloth = self.dress_cloth
        return dress_cloth


dress_cloth = [0, 0, 0]

jackets = int(input('Количество пиджаков '))
coats = int(input('Количество пальто '))

cloth_jacket = Jacket(jackets, coats, dress_cloth)
cloth_jacket.cloth()
cloth_coat = Coat(jackets, coats, dress_cloth)
cloth_coat.cloth()
dress = Dress('', '', '')
print(dress.my_method)



