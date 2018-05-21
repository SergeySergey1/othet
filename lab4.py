l={}
r={}
import os
def cls():
    os.system("CLS")
while 1:
    print(" Выбирите действие:\n 1 - создать нового пользователя\n 2 - войти в систему\n 0 - выход из системы ")
    flag = input()
    cls()
    if flag == '1':
        print(" Придумайте логин:")
        log = input()
        print(" Придумайте пароль:")
        pas = input()
        l[log]=pas
        print(l);
        print(" Выбирите роль: admin(1) или user(2)")
        role = input()
        if role=='1':
            print( log, '- Сохранён как admin')
        elif role=='2':
            print( log, '- Сохранён как user')
        r[log]=role
    elif flag == '2':
        while 2:
            print(" Введите логин:")
            print(l);
            log = input()
            if log in l:
                    print(" Введите пароль:")
                    pas = input()
                    if pas==l[log] or pas==l[log1]:
                        if role==r[log]:
                            if role=='1':
                                while flag=='2' or flag=='3' or flag=='4' or flag=='6' or flag=='1':
                                    print(" Вы вошли в систему как администратор, под иминем:", log)
                                    print (' Выбирите дайствие:\n 1 - создать нового пользователя \n 2 - изменить логин\n 3 - изменить пароль\n 4 - сбросить пароль \n 5 - список пользователей \n 6 - изменить роль пользователя \n 7 - выход из учётной записи \n 0 - выход из программы ')
                                    flag = input()
                                    cls()
                                    if flag == '1':
                                        print(" Придумайте логин:")
                                        log = input()
                                        pas = input()
                                        l[log]=pas
                                        print(" Выбирите роль: admin(1) или user(2)")
                                        role = input()
                                        if role=='1':
                                           print( log, '- Сохранён как admin')
                                        elif role=='2':
                                           print( log, '- Сохранён как user')
                                        r[log]=role
                                    elif flag == '2':
                                        print(" Придумайте новый логин:")
                                        log1 = input()
                                        if log1 in l[log]:
                                            print('Данный логин уже занят')
                                        else:
                                            print ("Логин изменён")
                                            l[log1]=l.pop(log)
                                            r[log1]=r.pop(log)
                                    elif flag == '3':
                                        print(' Введите старый пароль:')
                                        pas = input()
                                        if pas in l[log] or pas in l[log1]:
                                            print(" Придумайте новый пароль:")
                                            pas = input()
                                            l.pop(log)
                                            l[log]=pas
                                        else:
                                            print("Неверный пароль")
                                    elif flag == '4':
                                        print(' Введите старый пароль:')
                                        pas = input()
                                        if pas in l[log] or pas in l[log1]:
                                            print(" Пароль удалён.\n")
                                            l.pop(log)
                                        else:
                                            print("Операция не возможна")
                                    elif flag == '5':
                                        print(" Пользователи:", l)
                                    elif flag == '6':
                                        print(" Выбирите новую роль: admin или user")
                                        role = input()
                                        if role=='1':
                                            print( log, '- Сохранён как admin')
                                        elif role=='2':
                                            print( log, '- Сохранён как user')
                                        r[log]=role
                                    elif flag == '7':
                                        print (' Вы вышли из учётной записи!\n')
                                        break;
                                    elif flag == '0':
                                        exit()
                            elif role=='2':
                                print(" Вы вошли в систему как пользователь под иминем: ", log)
                                print (' Выбирите действие:\n 1 - изменить логин\n 2 - изменить пароль \n 3 - выход из учётной записи \n 0 - выход из программы')
                                flag = input()
                                if flag == '1':
                                    print(" Придумайте новый логин:")
                                    log = input()
                                    l[log1]=l.pop(log)
                                    r[log1]=r.pop(log)
                                elif flag == '2':
                                    print(' Введите старый пароль:')
                                    pas = input()
                                    if pas in l[log] or pas in l[log1]:
                                        print(" Придумайте новый пароль:")
                                        pas = input()
                                        l.pop(log)
                                        l[log]=pas
                                    else:
                                        print("Неверный пароль!")
                                elif flag == '3':
                                    print (' Вы вышли из учётной записи!\n')
                                    break;
                                elif flag == '0':
                                    exit()
                    else:
                        print(" Неверный пароль!\n")
            else:
                print(" Неверный логин!\n")
    elif flag == '0':
        exit()
