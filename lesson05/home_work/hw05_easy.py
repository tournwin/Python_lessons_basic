import sys, os, shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def exercise01():
	print('\n*** Задание 1')
	# Создание папок в цикле
	for i in range(1, 10):
		dirName = 'dir_'+str(i)
		if not os.path.exists(dirName):
			os.makedirs(dirName)
			print('+ ' + dirName + ' (папка создана)')

	input("*** Папки были созданы. Нажмите Enter, чтобы удалить созданные папки")

	# Удаление папок
	for i in range(1, 10):
		dirName = 'dir_'+str(i)
		if os.path.exists(dirName):
			os.rmdir(dirName)
			print('- ' + dirName + ' (папка удалена)')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def exercise02():
	print('\n*** Задание 2')
	dir_list = [d for d in os.listdir(path=".") if os.path.isdir(d)] # len(d.split('.')) == 1 -- не работает
	if (len(dir_list) == 0):
		print('В папке со скриптом нет ни одной папки!')
	else:
		print('Список папок в папке со скриптом: ')
		for i, folder in enumerate(dir_list):
			print(str(i+1) + '. ' + folder)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def exercise03():
	print('\n*** Задание 3')
	
	pathToFile = os.path.abspath(__file__)
	
	if (os.path.isfile(pathToFile)):
		shutil.copy(pathToFile, pathToFile+"_copy.py", follow_symlinks = True)	
	else:
		print('Файл скрипта унесли. Куда - неизвестно.')


#########################################
############# Вход в скрипт #############
#########################################

if __name__ == "__main__":
	while True:
		
		# **********************************
		# Выберите задание для проверки:
		# 1 - Задание 1
		# 2 - Задание 2
		# 3 - Задание 3
		# q - Выход
		# **********************************
		# Ваш выбор: 
		
		key = input("\n**********************************\nВыберите задание для проверки:\n1 - Задание 1\n2 - Задание 2\n3 - Задание 3\nq - Выход\n**********************************\nВаш выбор: ")

		if key == 'q' or key == 'й':
			sys.exit()
		elif key == '1':
			exercise01()
		elif key == '2':
			exercise02()
		elif key == '3':
			exercise03()

########################################################################################

# Для импортирования в normal #

# изменение рабочей директории
def change_dir(currentFolder):
	print("Текущая директория: "+currentFolder)
	return input("Новая директория: ")

# содержимое папки
def folder_contains(currentFolder):
	
	print('Текущая директория: '+currentFolder)
	dir_list = [d for d in os.listdir(path=currentFolder) if os.path.isdir(d)] # len(d.split('.')) == 1 -- не работает
	file_list = [d for d in os.listdir(path=currentFolder) if os.path.isfile(d)] # len(d.split('.')) == 1 -- не работает

	if (len(dir_list) == 0):
		print('В папке нет ни одной папки!')
	else:
		print('Список папок: ')
		for i, folder in enumerate(dir_list):
			print(str(i+1) + '. ' + folder)

	if (len(file_list) == 0):
		print('В папке нет ни одного файла!')
	else:
		print('Список файлов: ')
		for i, filename in enumerate(file_list):
			print(str(i+1) + '. ' + filename)

# Создать папку
def make_dir(currentFolder):
	dir_name = input('Новая папка: ')
	if not dir_name:
		print("Необходимо указать имя папки")
		return
	dir_path = os.path.join(currentFolder, dir_name)
	try:
		os.mkdir(dir_path)
		print('директория {} создана'.format(dir_name))
	except FileExistsError:
		print('директория {} уже существует'.format(dir_name))

# Удалить папку
def remove_dir(currentFolder):
	dir_name = input('Папка для удаления: ')
	if not dir_name:
		print("Не указана папка для удаления")
		return
	dir_path = os.path.join(currentFolder, dir_name)
	if (os.path.isdir(dir_path)):
		shutil.rmtree(dir_path, ignore_errors=True)
		print('Директория {} удалена.'.format(dir_name))
	else:
		print("Директории {} не существует, либо указан путь к файлу.".format(dir_name))


#### На будущее
# путь к папке со скриптом
# currentFolder = os.path.dirname(os.path.abspath(__file__)) 