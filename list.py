input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
a = int(data)
list_1 = []

f1 = 0
f2 = 1

list_1.append(f1) #добавлем ноль
list_1.append(f2) #добавлем единицу

b = 0 #количество элементов больше медианного значения
for i in range(1, a-1):

    if i%2 == 0: #если i четное, то мы обноляем s1
        f1=f1+f2
    elif i%2 == 1: #если i нечетное, то мы обноляем s2(чередуем после каждого числа)
        f2=f1+f2
    list_1.append(f1+f2)

for i in range(0, len(list_1)): 
    if list_1[i] % 2 == 0: #проверяем на четное или нечетное
        list_1[i] = list_1[i] * 2 #четное, то умножаем на 2
    else:
        list_1[i] = list_1[i] ** 2 #нечетное, то возводим в квадрат
minel = min(list_1) #мин элемент
maxel= max(list_1) #макс элемент
lenl = len(list_1) #длина
sr_arifm = sum(list_1)/len(list_1) #медианное значение
for i in range(0, len(list_1)):
    if int(list_1[i]) > sr_arifm:
        b += 1 #проверяем, сколько чисел будет больше мидианного значения
output.write(str('min - ') + str(minel) + str('\nmax - ') + str(maxel) + str('\nlen - ') + str(lenl) + str('\n> median - ') + str(b))
input_data.close()
output.close()