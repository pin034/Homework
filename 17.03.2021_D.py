from random import randint
a = randint (100,999)
b = a // 100
c = a % 100 // 10
d = a % 10
print("Выпало число",a)
print("Сотни:",b)
print("Десятки:",c)
print("Единицы:",d)
