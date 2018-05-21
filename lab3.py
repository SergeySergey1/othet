u=[]
l=[]
p=[]
import os
def cls():
    os.system("CLS")
while 1:
    print(" Выбирите действие:\n 1 - создать нового пользователя\n 2 - войти в систему\n 0 - выход из системы ")
    flag = input()
    if flag == '1':
        print(" Придумайте логин:")
        log = input()
        l.append(log)
        l.index(log)
        x=l.index(log)
        print(" Придумайте пароль:")
        pas = input()
        p.append(pas)
        p.index(pas)
        y=p.index(pas)
        #u.append(l+p)
        cls()
        print(u)
    elif flag == '2':
        while flag!='0':
            print(l, p)
            print(" Введите логин:")
            log = input()
            if log in l:
                #print(" Введите пароль для", l.index(log),"- пользователя, отчёт начинается с нуля!")
                x=l.index(log)
                print(" Введите пароль:")
                pas = input()
                cls()
                if log == l[x] and pas == p[x]:
                    print(" Вы вошли в систему под иминем:", log)
                    print (' Выбирите дайствие:\n 1 - изменить логин \n 2 - изменить пароль\n 3 - выход из учётной записи\n 0 - выход из программы ')
                    flag = input()
                    if flag == '1':
                        cls()
                        print(" Придумайте новый логин:")
                        log = input()
                        if log in l:
                            print('Данный логин уже используется')
                        else:
                            l[x] = log
                            cls()
                    elif flag == '2':
                        print(' Введите старый пароль:')
                        pas = input()
                        cls()
                        if pas in p:
                            print(" Придумайте новый пароль:")
                            pas = input()
                            p[x] = pas
                            cls()
                        else:
                            print('Неверный пароль!\n')
                    elif flag == '3':
                        print (' Вы вышли из учётной записи!\n')
                        cls()
                        break;
                    elif flag == '0':
                        exit()
                else:
                    print(" Неверный пароль!\n")
            else:
                print(" Неверный логин!\n")
    elif flag == '0':
        exit()
