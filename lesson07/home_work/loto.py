#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
	9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
	  16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


import os, sys, random

# чистка консоли в зависимости от операционки
# (для красивого вывода)
# windows - 'cls', linux - 'clear'
def cls():
	os.system('cls' if os.name=='nt' else 'clear')

# Создать карточку
def ticket_create():
	a = 0
	ticketNumbers = []
	while a != 3:
		# Список, в котором может быть только 5 значений True из 9
		randBools = [random.choice([True, False]) for _ in range(9)]
		while (randBools.count(True) != 5):
			randBools = [random.choice([True, False]) for _ in range(9)]
		
		# 9 рандомных чисел. Если True, то входит в билет,
		# иначе заменяется на пустое значение
		randNums = [str(random.randint(1, 91)) for _ in range(9)]
		
		outputTicketString = []
		for i, m in enumerate(randNums):
			if randBools[i] == True:
				outputTicketString.append(m)
			else:
				outputTicketString.append('')

		# передача строки в карточку
		ticketNumbers.append(outputTicketString)
		a+=1

	return ticketNumbers

# Вывести карточку
def ticket_print(ticket):
	for line in ticket:
		for el in line:
			print('{:<3}'.format(el), end='')
		print()

# Удалить число из карточки
def removeNumFromTicket(ticket, barrel):
	for line in ticket:
		for i, el in enumerate(line):
			if el == barrel:
				line[i] = '-'
				return True
	return False

# Проверить карточку на пустоту
def ticket_isEmpty(ticket):
	for line in ticket:
		for el in line:
			if el.isdigit():
				return False
	return True



#########################################
############# Вход в скрипт #############
#########################################

if __name__ == "__main__":
	
	# генерируем билеты игроку и компьютеру
	player = ticket_create()
	computer = ticket_create()

	# генерация листа бочонков
	barrels = random.sample(range(1, 91), 90)

	# перебор значений листа
	for i, barrel in enumerate(barrels):

		cls() 

		print('Новый бочонок: {} (осталось {})'.format(barrel, len(barrels)-i-1))
		print('------ Ваша карточка -----')
		ticket_print(player)
		print('--------------------------')
		print('-- Карточка компьютера ---')
		ticket_print(computer)
		print('--------------------------')

		while True:
			answer = input('Зачеркнуть цифру? (y/n) ')
			if answer == 'y':
				if not removeNumFromTicket(player, str(barrel)):
					print('Вы проиграли!')
					sys.exit()
				break
			elif answer == 'n':
				if removeNumFromTicket(player, str(barrel)):
					print('Вы проиграли!')
					sys.exit()
				break
			else:
				print('Введите y или n')
		if ticket_isEmpty(player):
			print('Поздравляем, вы выиграли!')
			sys.exit()
		removeNumFromTicket(computer, str(barrel))
		if ticket_isEmpty(computer):
			print('Вы проиграли!')
			sys.exit()