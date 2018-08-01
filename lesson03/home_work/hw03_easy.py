# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
	strNumber = str(number)
	dotPos = strNumber.find('.')
	if (dotPos != -1): # Если есть точка в строке
		strBeforeDot = strNumber[:dotPos] # Строка до точки
		strAfterDot = strNumber[dotPos+1::] # строка после точки
		if (ndigits > 0):
			if (len(strAfterDot) != ndigits):
				if (len(strAfterDot) > ndigits):
					# Если номер ndigits элемента строки > 5,
					# то +1 предыдущему символу
					# Иначе -1
					afterLastNum = int(strAfterDot[ndigits])
					strRoundNum = strAfterDot[:ndigits]
					lastNum = int(strRoundNum[-1])
					if (afterLastNum >= 5):
						strRoundNum = strRoundNum[:-1] + str(lastNum+1)
					else:
						strRoundNum = strRoundNum[:-1] + str(lastNum-1)
					return float(strNumber[:dotPos+1]+strRoundNum)
				else:
					### Дописать нулями
					#while len(strAfterDot) != ndigits:
					#	strAfterDot += "0"
					#return float(strNumber[:dotPos+1]+strAfterDot)
					return number
			else:
				return number
		else:
			return int(strBeforeDot)
	else:
		return number

print(my_round(2.1234567, 0))
#print(my_round(2.1999967, 5))
#print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


#print(lucky_ticket(123006))
#print(lucky_ticket(12321))
#print(lucky_ticket(436751))
