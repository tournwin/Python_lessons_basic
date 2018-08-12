import sys
import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
	# функция-конструктор - запускается автоматически при создании объекта (экземпляра класса)
	def __init__(self, point1, point2, point3):
		self.x1 = float(point1[0])
		self.y1 = float(point1[1])
		self.x2 = float(point2[0])
		self.y2 = float(point2[1])
		self.x3 = float(point3[0])
		self.y3 = float(point3[1])
		self.a = math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		self.b = math.sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
		self.c = math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)

	# методы
	def get_area(self):
		Area = math.fabs(self.x1*(self.y2-self.y3) + self.x2*(self.y3-self.y1) + self.x3*(self.y1-self.y2)) / 2.0
		return Area

	def get_heights(self):
		ha = 2*self.get_area() / self.a
		hb = 2*self.get_area() / self.b
		hc = 2*self.get_area() / self.c
		return [ha, hb, hc]

	def get_perimeter(self):
		return self.a + self.b + self.c

# Задача-2: Написать Класс 'Равнобочная трапеция', заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
	# функция-конструктор - запускается автоматически при создании объекта (экземпляра класса)
	def __init__(self, point1, point2, point3, point4):
		self.x1 = float(point1[0])
		self.y1 = float(point1[1])
		self.x2 = float(point2[0])
		self.y2 = float(point2[1])
		self.x3 = float(point3[0])
		self.y3 = float(point3[1])
		self.x4 = float(point4[0])
		self.y4 = float(point4[1])
		
	# методы

	# проверка, является ли фигура равнобочной трапецией
	def trapezoid_test(self):
		c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
		d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
  
		if c == d:
			return 'Трапеция равнобочная'
		else:
			return 'Трапеция не равнобочная'

	def get_sides(self):
		c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
		d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
		a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
		b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
		#print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)
		return [a, b, c, d]
		
	def get_perimeter(self):
		c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
		d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
		a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
		b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
		P = a+b+c+d
		return P   
	
	def get_area(self):
		c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
		d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
		a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
		b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
		S = ((a+b)/2)*(math.sqrt((c**2)-((((b-a)**2)+(c**2)-(d**2))/(2*(b-a)))))
		return S


########################################################################################

def exercise01():
	
	# Ввод координат
	coordsNotFound = True
	while coordsNotFound:
		print('Введите координаты точек треугольника через пробел')
		point1 = input('1 точка: x y = ').split()
		point2 = input('2 точка: x y = ').split()
		point3 = input('3 точка: x y = ').split()
		
		# количество элементов при введении координат точек
		if (len(point1)==2 & len(point2)==2 & len(point3)==2):
			# проверка, что все введённые координаты - числа
			if ((point1[0].isdigit() & point1[1].isdigit()) & (point2[0].isdigit() & point2[1].isdigit()) & (point3[0].isdigit() & point3[1].isdigit())):
				coordsNotFound = False
			else: 
				print('Не все введённые координаты - числа')
		else:
			print('Координаты были введены не верно. Необходимо ввести координаты x и y каждой точки через пробел')
	
	# работа класса и его методов
	triangle = Triangle(point1, point2, point3)
		
	inExercise = True
	while inExercise:
		
		print('\nКоординаты точек: \n1: {}, 2: {}, 3: {}\n'.format(point1, point2, point3)) 
		
		print('**********************************')
		print('Треугольник - Получить:')
		print('1 - Площадь')
		print('2 - Высота')
		print('3 - Периметр')
		print('q - Назад')
		print('**********************************')

		keyInEx1 = input('Ваш выбор: ')
		
		if keyInEx1 == 'q' or keyInEx1 == 'й':
			inExercise = False
		elif keyInEx1 == '1':
			print('Площадь треугольника = ' + str(triangle.get_area()))
		elif keyInEx1 == '2':
			print('В треугольнике 3 высоты: ')
			heights = triangle.get_heights()
			for i, height in enumerate(heights):
				print(str(i) + '. ' + str(height))
		elif keyInEx1 == '3':
			print('Периметр = ' + str(triangle.get_perimeter()))

def exercise02():
	# Ввод координат
	coordsNotFound = True
	while coordsNotFound:
		print('Введите координаты точек равнобочной трапеции через пробел')
		point1 = input('1 точка: x y = ').split()
		point2 = input('2 точка: x y = ').split()
		point3 = input('3 точка: x y = ').split()
		point4 = input('4 точка: x y = ').split()
		
		# количество элементов при введении координат точек
		if (len(point1)==2 & len(point2)==2 & len(point3)==2 & len(point4)==2):
			# проверка, что все введённые координаты - числа
			if ((point1[0].isdigit() & point1[1].isdigit()) & (point2[0].isdigit() & point2[1].isdigit()) & (point3[0].isdigit() & point3[1].isdigit()) & (point4[0].isdigit() & point4[1].isdigit())):
				coordsNotFound = False
			else: 
				print('Не все введённые координаты - числа')
		else:
			print('Координаты были введены не верно. Необходимо ввести координаты x и y каждой точки через пробел')
	
	# работа класса и его методов
	trapezoid = Trapezoid(point1, point2, point3, point4)
		
	inExercise = True
	while inExercise:

		print('\nКоординаты точек: \n1: {}, 2: {}, 3: {}, 4: {}\n'.format(point1, point2, point3, point4))  
		
		print('**********************************')
		print('Равнобочная трапеция - Получить:')
		print('1 - Проверка равнобочности')
		print('2 - Длины сторон')
		print('3 - Периметр')
		print('4 - Площадь')
		print('q - Назад')
		print('**********************************')

		keyInEx2 = input('Ваш выбор: ')
		
		if keyInEx2 == 'q' or keyInEx2 == 'й':
			inExercise = False
		elif keyInEx2 == '1':
			print(trapezoid.trapezoid_test())
		elif keyInEx2 == '2':
			print('Стороны трапеции:')
			sides = trapezoid.get_sides()
			for i, side in enumerate(sides):
				print(str(i) + '. ' + str(side))
		elif keyInEx2 == '3':
			print('Периметр трапеции = ' + str(trapezoid.get_perimeter()))
		elif keyInEx2 == '4':
			print('Площадь трапеции = ' + str(trapezoid.get_area()))


#########################################
############# Вход в скрипт #############
#########################################

if __name__ == '__main__':
	while True:
		
		print('**********************************')
		print('Выберите фигуру:')
		print('1 - Треугольник')
		print('2 - Равнобочная трапеция')
		print('q - Выход')
		print('**********************************')

		key = input('Ваш выбор: ')

		if key == 'q' or key == 'й':
			sys.exit()
		elif key == '1':
			exercise01()
		elif key == '2':
			exercise02()