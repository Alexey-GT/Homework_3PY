#Задача№2
# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

#     *Пример:*

#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19
max = 0
min = 1
lst = [1.1, 1.2, 3.1, 5.1, 10.01]
for i in range(len(lst)):
    j = lst[i] - int(lst[i])
    if max < j:
        max = j
    #print(round(max,3))
    if min > j:
        min = j 
    #print(round(min,3)) 
diff = max - min
print(round(diff,2))


