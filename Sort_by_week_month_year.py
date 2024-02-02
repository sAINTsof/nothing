import os, time
log = open('C:\\Users\\User\\Desktop\\Script_1C\\DB2\\logs.txt', 'a') #Указываем путь до логов
src_dir = 'C:\\Users\\User\\Desktop\\Script_1C\\DB2\\' #Указываем путь до базы бэкапов 

def sort_by_mtime(main_dir): #Сортируем файлы определенной директории в базе(Например C:\\Us.....1C\\DB2\\IvanovBackups в заранее созданные папки Week,Month и Year
    min_c_time = 604800
    last_file = ""
    print(f"Содержимое директории {main_dir} : {os.listdir(main_dir)}", file=log)
    for file in os.listdir(main_dir):
        if file.endswith(".txt") == True:
            if time.strftime("%d", time.strptime(time.ctime(os.path.getmtime(main_dir + file)))) \
                    == '01':
                os.rename(main_dir + file, main_dir + "Month\\" + file)  # Если файл создан 1 числа, кидаем его в Month
                print(f"Файл {file} перемещен в {main_dir + "Month\\"}", file = log)
            elif time.strftime("%d-%m", time.strptime(time.ctime(os.path.getmtime(main_dir + file)))) \
                    == '02-02': 
                os.rename(main_dir + file, main_dir + "Year\\" + file)  # Если файл создан 02.02, кидаем его в Year
                print(f"Файл {file} перемещен в {main_dir + "Year\\"}", file=log)
            elif time.time() - os.path.getmtime(main_dir + file) < min_c_time:  # Сравниваем время существования файла с мин
                try:  # Так как при первой итерации last_file="", исключаем возможные ошибки
                    os.remove(main_dir + last_file)  # Если файл существует дольше min_c_time, то удаляем
                    print(f"Файл {last_file} удален", file=log)
                except:
                    pass
                min_c_time = time.time() - os.path.getmtime(main_dir + file)  # Присваиваем мин новое значение
                last_file = file
            else:
                os.remove(main_dir + file)
                print(f"Файл {file} удален", file=log)
    try: # На случай,если все так же last_file="", исключаем возможные ошибки
        os.rename(main_dir + last_file, main_dir + "Week\\" + last_file)
    except:
        print(f'Не удалось переместить файл {last_file} в {main_dir + "Week\\"}', file=log)
    print(f'Файл {last_file} перемещен в {main_dir + "Week\\"}', file=log)

def sort_week(main_dir): #Сортируем папку Week, удаляем файлы старше недели
    for file in os.listdir(main_dir + "Week\\"):
        if time.time() - os.path.getmtime(main_dir + "Week\\" + file) > 604800:
            os.remove(main_dir + "Week\\" + file)
            print(f'Файл {file} удален из {main_dir + "Week\\"}', file=log)

for dir in os.listdir(src_dir): #Проходим все директории в базе бэкапов и передаем каждую директории функциям sort_week и sort_by_mtime
    if os.path.isdir(src_dir + dir):
        print(f"_________Директория {src_dir + dir} ____________", file=log)
        sort_week(src_dir + dir + "\\")
        sort_by_mtime(src_dir + dir + "\\")
log.close()
