import os, time
log = open('C:\\Users\\User\\Desktop\\Script_1C\\DB2\\logs.txt', 'a')
src_dir = 'C:\\Users\\User\\Desktop\\Script_1C\\DB2\\'

def sort_day_to_week(main_dir): #Находит самый свежий файл в папке
    min_c_time = 604800
    last_file = ""
    print(f"Содержимое директории {main_dir} : {os.listdir(main_dir)}", file = log)
    for file in os.listdir(main_dir): # Проверяем является ли объект файлом .txt
        if file.endswith(".txt") == True:
            if time.time() - os.path.getctime(main_dir + file) < min_c_time: #Сравниваем время существования файла с мин
                try: #Так как при первой итерации last_file="", исключаем возможные ошибки
                    os.remove(main_dir + last_file)  # Если файл существует дольше min_c_time, то удаляем
                    print(f"Файл {last_file} удален", file = log)
                except:
                    pass
                min_c_time = time.time() - os.path.getctime(main_dir + file) #Присваиваем мин новое значение
                last_file = file

            else:
                os.remove(main_dir + file)
                print(f"Файл {file} удален", file = log)

    try:
        os.rename(main_dir + last_file, main_dir + "Week\\" + last_file) #Перемещаем last_file в Week
    except:
        print(f"Не удалось переместить {last_file} в {main_dir + "Week\\"}", file = log)

def sort_week_to_month(main_dir): #Сортируем Week, удаляем файл, старше одной недели, перемещаем файл за 25 число в Month
    print(f"Содержимое директории {main_dir + "Week\\"} : {os.listdir(main_dir + "Week\\")}", file = log)
    for file in os.listdir(main_dir + "Week\\"):
        if time.time() - os.path.getctime(main_dir + "Week\\" + file) > 604800: #Если файл старше недели
            print(f"Файл {main_dir + "Week\\" + file} удален", file=log)
            os.remove(main_dir + "Week\\" + file)
        elif int(time.strftime("%d" ,time.strptime(time.ctime(os.path.getctime(main_dir + "Week\\" + file))))) \
                == 1:
            os.rename(main_dir + "Week\\" + file, main_dir + "Month\\" + file) #Если файл создан 25, кидаем его в Month
            print(f"Файл {file} перемещен в {main_dir + "Month\\"}", file = log)

for dir in os.listdir(src_dir): №
    if os.path.isdir(src_dir + dir):
        sort_day_to_week(src_dir + dir + "\\")
        sort_week_to_month(src_dir + dir + "\\")