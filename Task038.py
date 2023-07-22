# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

from database import *
from view import *
            
def main_case():
    while True:
        num = input_num()
        match num:
            case 1:
                n = input_name()
                write_name(n)
                print(print_lst())
                print('Данные сохранены!\n')
            case 2:
                s = input_search()
                search_line(s)
            case 3:
                k = input_data_del()
                delete_data(k)
                print('Данные удалены!\n')
            case 4:
                k = input_number_correct()
                data = input_name()
                correct_data(k, data)
                print('Изменения сохранены!\n')
            case 5:
                sortp = input_char_sort_prim()
                sorts = input_char_sort_sec()
                sort_data(sortp, sorts)
                print('Сортировка завершена!\n')    
            case 6:
                print('До свидания!\n')
                return False


main_case()