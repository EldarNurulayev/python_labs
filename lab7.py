import math

#1
print("Задание 7.1. НОД и НОК чисел A и B")

def NOD(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a > b:
        return NOD(a - b, b)
    else:
        return NOD(a, b - a)

a = int(input("Введите A: "))

b = int(input("Введите B: "))

nod = NOD(a, b)
nok = a * b / nod

print(f"НОД: {nod}")
print(f"НОК: {nok}")

#2
print("\n\nЗадание 7.2. Площадь выпуклого четырехугольника")
def space(s1, s2, s3, s4, d):
    p1 = (ab + bc + ac) / 2
    p2 = (ad + cd + ac) / 2
    space1 = math.sqrt(p1 * (p1 - ab) * (p1 - bc) * (p1 - ac)) + math.sqrt(p2 * (p2 - ad)*(p2 - cd) * (p2 - ac))
    return space1


ab = int (input('Введите длину стороны 1: '))
bc = int (input('Введите длину стороны 2: '))
cd = int (input('Введите длину стороны 3: '))
ad = int (input('Введите длину стороны 4: '))
ac = int (input('Введите длину диагонали: '))


 

print(f"Площадь выпуклого 4-угольника = {space(ab, bc, cd, ad, ac)}")