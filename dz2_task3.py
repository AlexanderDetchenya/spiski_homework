# #3.	Дана следующая функция y = f(x).
# y = 2x – 10, если x > 0
# y = 0, если x = 0
# y = 2 *|x| - 1, если x < 0
# Примечание: для нахождения модуля используйте встроенную функцию abs(x)

x = int(input("Введите значение переменной х для функции y=f(x): "))
first = 2 * x - 10
second = 2 * abs(x) - 1
third = 0
if x > 0:
    print("y= ", first)
elif x < 0:
    print("y= ", second)
else:
    print("y= ", third)
