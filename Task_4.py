#Задача№4
# Задайте число. Составьте список чисел Фибоначчи, в том числе
#  для отрицательных индексов.

#     *Пример:*

#     - для k = 8 список будет выглядеть так:
#      [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input("Введите число: "))
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

lst = []
lst1 = []

for e in range(1, N):
    lst.append(fib(e))
print(lst) 

for e in range(1,N):
    if e%2 != 0:
        lst1.append(fib(e))
    else: 
        lst1.append(fib(e)*(-1))
print(lst1)
reversed = lst1[::-1]
reversed.append(0)
print(reversed)

print(', '.join(map(str,reversed)) + ', '.join(map(str,lst)))


    