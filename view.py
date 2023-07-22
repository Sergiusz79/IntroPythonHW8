def input_num():
    ask = int(input('Выберите действие:\n 1 - Добавить нового абонента\n 2 - Найти данные абонента по хаарктеристике\n 3 - Удалить данные абонента\n 4 - Изменить данные абонента\n 5 - Отсортировать список\n 6 - Выход\n:>'))
    return ask

def input_name():
    id = input('Введите id \n')
    name = input('Введите Ф.И.О. \n')
    phone = input('Введите номер телефона \n')
    res = id + ', ' + name + ', ' + phone + '\n'
    return res

def input_search():
    s = str(input('Введите данные для поиска\n:>'))
    return s

def input_data_del():
    with open("phone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print(*lst, sep='\n')
        print()
        k = int(input('Введите номер записи которую необходимо удалить:\n'))
        return k

def input_number_correct():
    with open("phone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print(*lst, sep='\n')
        print()
        k = int(input('Введите номер записи которую необходимо изменить:\n'))
        return k
    
def input_char_sort_prim():
    sortp = int(input('Выберите параметры сортировки:\n 1 - По id\n 2 - По Ф.И.О.\n 3 - По номеру телефона\n'))
    return sortp

def input_char_sort_sec():
    sorts = int(input('Выберите параметры сортировки:\n 1 - По возрастанию\n 2 - По убыванию\n'))
    return sorts
