if __name__ == '__main__':# задача 4 урока 3
    def my_func(x, y):
        if y==0:
            return 1
        else:
            return my_func(x, y + 1) * (1 / x)


    x=float(input('Введите произволное действительное число x '))
    y=int(input('Введите отрицательную целую степень числа x,число y '))
    print(my_func(x,y))