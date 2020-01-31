#kletka = int(input('Каково количество ячеек в клетке '))
#b = kletka // 5
#a = kletka % 5

#print(('*'*5+'\n')*b + '*'*a)


class Kletka:
    def __init__(self, icheek):
        self.icheek = icheek


    def __add__(self, other):
        kl1 = self.icheek
        kl2 = other.icheek
        survive = int(kl1 + kl2)
        kletka = int(survive)
        b = kletka // 5
        a = kletka % 5
        print(('*'*5+'\n')*b + '*'*a)
        return f'Выжившая после бойни клетка состоит из, {survive}'

    def __sub__(self, other):
        kl1 = self.icheek
        kl2 = other.icheek

        if kl1 > kl2:
            survive = int(kl1 - kl2)
            kletka = int(survive)
            b = kletka // 5
            a = kletka % 5
            print(('*' * 5 + '\n') * b + '*' * a)
            return f'Выжившая после бойни клетка состоит из, {survive}'
        elif kl1 == kl2:
            return f'После поглощения первая клетка не выжила'
        else:
            return f'После поглощения первая клетка оставила вторую еще и голодной'


    def __mul__(self, other):
        kl1 = self.icheek
        kl2 = other.icheek
        survive = int(kl1 * kl2)
        kletka = int(survive)
        b = kletka // 5
        a = kletka % 5
        print(('*' * 5 + '\n') * b + '*' * a)
        return f'Стокнувшись воедино клетка обноружила что увеличилась на , {survive},  ячеек'


    def __floordiv__(self, other):
        kl1 = self.icheek
        kl2 = other.icheek

        if kl2 != 0:
            survive = int(kl1 // kl2)
            kletka = int(survive)
            b = kletka // 5
            a = kletka % 5
            print(('*' * 5 + '\n') * b + '*' * a)

            return f'Клетка поделилась как могла, осталось, {survive}, ячеек'
        else:
            return f'Клетка почесала затылок но потом на ноль не стала делиться'

    @property
    def make_order(silf):
        survive = silf.survive
        print(survive)
        return (('*' * 5 + '\n') * (survive//5) + '*' * (survive%5))


klet1 = int(input("Сколько в клетке Бобик жирности, измеряется в ячейках = "))
klet2 = int(input("Сколько в клетке Тазик жирности, измеряется в ячейках = "))
print('\n')
kletka1 = Kletka(klet1)
kletka2 = Kletka(klet2)
print(kletka1 + kletka2 , '\n')

#kletka2.make_order()
print(kletka1 - kletka2, '\n')

print(kletka1 * kletka2, '\n')

print(kletka1 // kletka2, '\n')
