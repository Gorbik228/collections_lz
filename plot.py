import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 7, 25)  #генерируем 25 точек от 0 до 7
y = x**4 - x**2 + 5*x #координаты y

# Создаем график
plt.plot(x, y, label='f(x) = x^3 - 3x^2 + 2x', color='red') #создаем пометку 
plt.title('График функции y') #подписываем весь график
plt.xlabel('Ось x') #ось x
plt.ylabel('Ось y') #ось y

plt.grid() #устанавливаем сетку

plt.xlim(-2, 10) #устанавливаем начальный вид функции
plt.ylim(0, 25) 

plt.show() #вывод графика