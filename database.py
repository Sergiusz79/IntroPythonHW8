def write_name(n):
    with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "a", encoding="UTF-8") as file:
        file.write(n)

def print_lst():
    with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print(*lst, sep='\n')   

def search_line(s):
    with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        lst = [line.rstrip() for line in lst]
        sd = []
        for row in lst:
            if s in row:
                sd.append(row)
        if len(sd) != 0:
            print('Данные найдены!\n')
            print(*sd, sep='\n')            
        else:
            print('Данные отсутствуют!\n')        

def delete_data(k):
    with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        del lst[k-1]
        print(*lst, sep='\n')
    with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "w", encoding="UTF-8") as file:     
        file.writelines(lst)

def correct_data(k, data):
    with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        lst.insert(k-1,data)
        del lst[k]
        print(*lst, sep='\n')
    with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "w", encoding="UTF-8") as file:    
        file.writelines(lst)    

def sort_data(sortp, sorts):
    with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print(*lst, sep='\n')
        print()
        if sortp == 1 and sorts == 1 or sortp == 3 and sorts == 1:
            lst.sort(key = lambda x: int(x.split(',')[sortp-1]))
        elif sortp == 1 and sorts == 2 or sortp == 3 and sorts == 2:
            lst.sort(reverse = True, key = lambda x: int(x.split(',')[sortp-1]))
        elif sortp == 2 and sorts == 1:
            lst.sort(key = lambda x: x.split(',')[1])
        else:
            lst.sort(reverse = True, key = lambda x: x.split(',')[1])    
        print(*lst, sep='\n')
        print()
        with open("D:\\Users\\Admin\\OneDrive\\Документы\\Учёба\\Programming\\PythonCourse\\Seminar008\\phone.txt", "w", encoding="UTF-8") as file:    
            file.writelines(lst)


