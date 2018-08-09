# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3


import os
import sys
import shutil

print('sys.argv = ', sys.argv)

currentPath = os.path.dirname(os.path.abspath(__file__))


def print_help():
	print()
	print("**********************************")
	print("help - получение справки")
	print("mkdir <dir_name> - создание директории")
	print("ping - возвращает pong")
	print("cp <file_name> - создает копию указанного файла")
	print("rm <file_name> - удаляет указанный файл")
	print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
	print("ls - отображение полного пути текущей директории")
	print("**********************************")
	#print("q - Выход")
	#print("**********************************")
	print()

def make_dir():
	dir_name = arg_sec
	if not dir_name:
		print("Необходимо указать имя директории вторым параметром")
		return
	dir_path = os.path.join(os.getcwd(), dir_name)
	try:
		os.mkdir(dir_path)
		print('директория {} создана'.format(dir_name))
	except FileExistsError:
		print('директория {} уже существует'.format(dir_name))


def ping():
	print("pong")

# копирование файла
def copy_file():
	fileToCopy = arg_sec
	if not fileToCopy:
		print("Необходимо указать имя файла вторым параметром")
		return
	
	pathToFile = os.path.abspath(fileToCopy)
	
	if (os.path.isfile(pathToFile)):
		shutil.copy(pathToFile, pathToFile+"_copy", follow_symlinks = True)	
		print("Копия файла {} создана в той же папке с постфиксом _copy".format(pathToFile))
	else:
		print('Файла не существует.')
	
# Изменение директории. 
# Не совсем понимаю смысл этой команды здесь, когда нет реализации через
# (while True: key = input)
# 
# Если необходимо реализовать через (while True: key = input)
# готов это сделать к след уроку
def change_dir():
	print('change_dir')

# Удаляет заданную в параметре директорию, если такая имеется
def remove_dir():
	dir_name = arg_sec
	if not dir_name:
		print("Необходимо указать имя директории вторым параметром")
		return
	dir_path = os.path.join(os.getcwd(), dir_name)
	if (os.path.isdir(dir_path)):
		shutil.rmtree(dir_path, ignore_errors=True)
		print('Директория {} удалена.'.format(dir_name))
	else:
		print("Директории {} не существует, либо указан путь к файлу.".format(dir_name))


# Возвращает путь к текущей папке
def current_dir():
	print(currentPath)



#########################################
############# Вход в скрипт #############
#########################################

if __name__ == "__main__":
	# "Консольная команда": функция_выполняющая_работу 
	do = {
		"help": print_help,
		"mkdir": make_dir,
		"ping": ping,
		"cp": copy_file,
		"cd": change_dir,
		"rm": remove_dir,
		"ls": current_dir
	}

	# Присваиваем переменной значение второго параметра,
	# если он есть
	try:
		arg_sec = sys.argv[2]
	except IndexError:
		arg_sec = None

	# Ключ команда, передаваемая в скрипт
	try:
		key = sys.argv[1]
	except IndexError:
		key = None

	# Если команда существует, выполняет её, вызывая соответствующую функцию из do
	if key:
		if do.get(key):
			do[key]()
		else:
			print("Задан неверный ключ")
			print("Укажите ключ help для получения справки")
