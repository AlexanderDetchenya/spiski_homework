# 4.	Напишите программу, которая выполняет сравнение двух переменных
numb_first = int(input("Vvedite peremennuy a: "))
numb_second = int(input("Vvedite peremennuy b: "))
if numb_first > numb_second:
    print("a>b")
elif numb_first < numb_second:
    print("a<b")
else:
    print("a=b")