# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите координаты первой точки по оси x: '))
y1 = int(input('Введите координаты первой точки по оси y: '))
x2 = int(input('Введите координаты второй точки по оси x: '))
y2 = int(input('Введите координаты второй точки по оси y: '))

import math
distans = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(f'Растояние между первой и второй точкой = {distans}')
