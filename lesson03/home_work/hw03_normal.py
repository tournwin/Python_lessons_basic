# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1) + fib(n-2)

def fibonacci(n, m):
	backValue = []
	while n != m:
		backValue.append(fib(n)) 
		n += 1
	backValue.append(fib(n)) 
	return backValue

n = int(input('n = '))
m = int(input('m = '))
print(fibonacci(n, m))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
	n = 1
	while n < len(origin_list):
		for i in range(len(origin_list)-n):
			if origin_list[i] > origin_list[i+1]:
				origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
		n += 1
	return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def new_filter(f, x):
	result = []
	for i in x:
		if f(i):
			result.append(i)
	return set(result)

print('Стандартный filter: ')
print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
print('Переработанный filter: ')
print(list(new_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

t = 0.00001

def getMiddle(x1, y1, x2, y2):
	xs = (x1 + x2) / 2
	ys = (y1 + y2) / 2 
	return [xs, ys]

def abs(n):
	if (n < 0):
		return -n
	else:
		return n

# Вершина 1
x1 = float(input('A1 x = '))
y1 = float(input('A1 y = '))
# Вершина 2
x2 = float(input('A2 x = '))
y2 = float(input('A2 y = '))
# Вершина 3
x3 = float(input('A3 x = '))
y3 = float(input('A3 y = '))
# Вершина 4
x4 = float(input('A4 x = '))
y4 = float(input('A4 y = '))

middle1 = getMiddle(x1, y1, x3, y3)
middle2 = getMiddle(x2, y2, x4, y4)

if ((abs(middle1[0] - middle2[0])) < t) & ((abs(middle1[1] - middle2[1])) < t):
	print('Это параллелограмм')
else:
	print('Это НЕ параллелограмм')