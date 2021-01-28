if __name__ =='__main__':# задача 6 урока 3
    def func(my_str):
        latin='qwertyuiopasdfghjklzxcvbnm,./;:-_@ '
        i=0
        while i<len(my_str):
            for l in my_str:
                if latin.count(l)==0:
                    break
                else:i+=1
            if i<(len(my_str)-1):
                break
            elif i==(len(my_str)-1):
                break
        if i<(len(my_str)-1):
            return('необходимо ввести текст латинскими буквами нижнего регистра')
        else:
            return (my_str.title())

    my_str=input('введите строку латинскими буквами нижнего регистра, любые знаки препинания допускаются: ')

    print(func(my_str))

