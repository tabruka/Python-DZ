# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

numberN = int(input('Введите число: '))
list = [1]
for i in range (1, numberN):
    list.append ((i+1) * list [i-1])
print(list)
