import os, time

main_path = 'C:\\Users\\User\\Desktop\\Script_1C\\DB\\'
def make_dir(name): #Создаем директорию
    try: #Чтобы не вылетала ошибка, если директория уже создана
        os.mkdir(name) #Поменять значение на время создания файла
    except:
        pass

#def sort_month(dir): # Допилить и прикрутить сортировку по месяцам
#    print(dir)
#    print(os.listdir(dir))
#    for day in os.listdir(dir):
#        print("----------")
#        print(dir + day)
#       if os.path.isdir(dir + day):
#           try:
#               print(os.path.dirname(dir + day))
#           except:
#               pass

def sort_files(current_dir): #Получаем список файлов в текущей директории, вызываем функцию make_dir(создаем директорию)  и перемещаем файл в новую директорию
    print(os.listdir(current_dir))
    for file in os.listdir(current_dir): #Листдир выводит список файлов и директорий в текущей директории
        print(file)
        if file[-4:] == ".txt":
            make_dir(current_dir + time.strftime("%Y-%m-%d" ,time.strptime(time.ctime(int(os.path.getctime(current_dir + file)))))) #Ебанутая конструкция, по кускам собрал. Надо попроще че-нить найти. Передаем функции make_dir имя новой директории
            os.rename(current_dir + file, current_dir + time.strftime("%Y-%m-%d" ,time.strptime(time.ctime(int(os.path.getctime(current_dir + file))))) + "\\" + file)# Опять громоздкая конструкция перекидывает файлы из текущей директории в созданную


for dir in os.listdir(main_path): #Проверяем, является ли объект в исходной директории файлом и передаем его функции sort_files
    if os.path.isdir(main_path + dir):
        sort_files(main_path + dir + "\\")

sort_month(main_path)